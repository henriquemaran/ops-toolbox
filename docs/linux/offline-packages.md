# Download de pacotes para instalação offline

Pacotes baixados em uma máquina devem ser usados em outra máquina com a mesma
versão de distribuição e arquitetura. Misturar versões pode quebrar
dependências.

## RHEL, Rocky Linux e derivados 8+

Na máquina com acesso à internet:

```bash
sudo dnf install -y dnf-plugins-core
mkdir -p packages
dnf download --resolve --alldeps --destdir ./packages NOME_DO_PACOTE
```

Transfira `packages/` para a máquina isolada e instale:

```bash
sudo dnf install ./packages/*.rpm
```

## Sistemas baseados em YUM

Para ambientes legados que ainda oferecem `yumdownloader`:

```bash
sudo yum install -y yum-utils
mkdir -p packages
yumdownloader --resolve --destdir ./packages NOME_DO_PACOTE
sudo yum localinstall ./packages/*.rpm
```

## Validações recomendadas

Antes da instalação, confirme a arquitetura e valide as assinaturas:

```bash
uname -m
rpm --checksig ./packages/*.rpm
```
