# Serviço Python com systemd

Este exemplo registra `/opt/receiver/receiver.py` como um serviço. Ele usa um
usuário dedicado em vez de executar a aplicação como `root`.

## 1. Preparar usuário e diretórios

```bash
sudo useradd --system --home-dir /opt/receiver --shell /usr/sbin/nologin receiver
sudo install -d -o receiver -g receiver /opt/receiver /opt/receiver/uploads
sudo install -o receiver -g receiver -m 0755 receiver.py /opt/receiver/receiver.py
```

Confirme o caminho do Python:

```bash
command -v python3
```

## 2. Criar a unidade

Crie `/etc/systemd/system/receiver.service`:

```ini
[Unit]
Description=Python receiver service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=receiver
Group=receiver
WorkingDirectory=/opt/receiver
ExecStart=/usr/bin/python3 /opt/receiver/receiver.py
Restart=on-failure
RestartSec=5s
NoNewPrivileges=true
PrivateTmp=true
ProtectHome=true
ProtectSystem=strict
ReadWritePaths=/opt/receiver/uploads

[Install]
WantedBy=multi-user.target
```

Se `command -v python3` retornar outro caminho, ajuste `ExecStart`.

## 3. Validar e iniciar

```bash
sudo systemd-analyze verify /etc/systemd/system/receiver.service
sudo systemctl daemon-reload
sudo systemctl enable --now receiver.service
sudo systemctl status receiver.service
```

Logs recentes:

```bash
journalctl -u receiver.service -n 50 --no-pager
```

Após alterar o script ou a unidade:

```bash
sudo systemctl daemon-reload
sudo systemctl restart receiver.service
```
