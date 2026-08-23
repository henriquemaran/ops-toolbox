# Laboratórios Rocky Linux no Docker

Use containers descartáveis para testar comandos sem alterar a máquina host.
O exemplo abaixo abre um shell interativo e remove o container ao sair:

```powershell
docker run --rm -it --name rocky-lab rockylinux:9
```

Para manter o container após o encerramento:

```powershell
docker run -it --name rocky-lab rockylinux:9
docker start -ai rocky-lab
```

Depois da primeira execução, o container também aparecerá no Docker Desktop.

## Pacotes do EPEL

Dentro do container:

```bash
dnf install -y epel-release
dnf makecache
```

O EPEL complementa os repositórios do Rocky Linux, mas não deve ser tratado
como origem automática para qualquer software de terceiros. Consulte a origem
e a assinatura do pacote antes de instalá-lo.

## Imagens legadas

CentOS Linux 7 e 8 chegaram ao fim do suporte. Use essas imagens apenas para
reproduzir sistemas legados em laboratórios isolados; para novos trabalhos,
prefira uma distribuição com atualizações de segurança ativas.
