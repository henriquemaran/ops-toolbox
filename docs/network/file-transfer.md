# Transferência de arquivos entre máquinas

Prefira protocolos autenticados e criptografados. Um servidor HTTP improvisado
sem autenticação pode expor arquivos e permitir gravações não autorizadas.

## Arquivo individual com SCP

```bash
scp ./arquivo.txt usuario@servidor:/opt/destino/
```

No PowerShell, o comando é igual quando o cliente OpenSSH está instalado:

```powershell
scp .\arquivo.txt usuario@servidor:/opt/destino/
```

## Diretório completo

```bash
scp -r ./diretorio usuario@servidor:/opt/destino/
```

Para transferências repetidas, `rsync` evita reenviar arquivos inalterados:

```bash
rsync -av --progress -e ssh ./diretorio/ usuario@servidor:/opt/destino/
```

## Quando o SSH usa outra porta

```bash
scp -P 2222 ./arquivo.txt usuario@servidor:/opt/destino/
rsync -av -e "ssh -p 2222" ./diretorio/ usuario@servidor:/opt/destino/
```

## Boas práticas

- Use chaves SSH protegidas por senha e limite as permissões da conta remota.
- Confirme a fingerprint do servidor no primeiro acesso.
- Não coloque IPs internos, usuários reais ou chaves privadas em exemplos
  públicos.
- Valide o checksum depois de transferências importantes:

```bash
sha256sum arquivo.txt
```
