# Certificado de cliente no Chromium headless

O Chromium usa um banco NSS no perfil do usuário. Mantenha o perfil e o
arquivo PKCS#12 protegidos: ambos podem dar acesso a sistemas que confiam no
certificado.

## 1. Criar um perfil isolado

```bash
umask 077
export CHROMIUM_PROFILE="$HOME/.local/share/chromium-client-profile"
mkdir -p "$CHROMIUM_PROFILE"
```

## 2. Instalar as ferramentas NSS

Em distribuições RHEL-like:

```bash
sudo dnf install -y nss-tools
```

## 3. Importar o PKCS#12

```bash
pk12util -d "sql:$CHROMIUM_PROFILE" -i client-certificate.p12
```

Digite a senha quando solicitado. Evite passá-la diretamente na linha de
comando, pois ela pode ficar registrada no histórico do shell ou ser visível
na lista de processos.

Confira o resultado:

```bash
certutil -L -d "sql:$CHROMIUM_PROFILE"
```

## 4. Abrir o Chromium com o perfil

O nome do executável varia entre distribuições:

```bash
chromium \
  --user-data-dir="$CHROMIUM_PROFILE" \
  --headless=new \
  https://secure-site.example
```

Em ambientes corporativos, a escolha automática do certificado deve ser
configurada por uma política gerenciada do Chromium e limitada às URLs
necessárias. Não desative o sandbox ou a validação TLS para contornar erros.

## Importar uma CA interna

Faça isso apenas depois de validar a origem e a impressão digital da CA:

```bash
certutil -A -d "sql:$CHROMIUM_PROFILE" \
  -n "Internal CA" \
  -t "CT,C,C" \
  -a -i internal-ca.pem
```

Nunca envie certificados privados, senhas ou o diretório do perfil para o
Git.
