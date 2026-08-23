# Ops Toolbox

[![Quality checks](https://github.com/henriquemaran/ops-toolbox/actions/workflows/quality.yml/badge.svg)](https://github.com/henriquemaran/ops-toolbox/actions/workflows/quality.yml)

Notas técnicas e pequenos utilitários para rotinas de Linux, containers e
automação. O conteúdo prioriza exemplos reproduzíveis, avisos de segurança e
comandos que possam ser adaptados a ambientes reais.

## Conteúdo

| Área | Material |
| --- | --- |
| Containers | [Laboratórios com Rocky Linux no Docker](docs/containers/rocky-linux-docker.md) |
| Linux | [Download de pacotes para instalação offline](docs/linux/offline-packages.md) |
| Linux | [Serviço Python com systemd](docs/linux/systemd-python-service.md) |
| Linux legado | [Repositórios Vault do CentOS 7](docs/linux/centos-7-vault.md) |
| Segurança | [Certificado de cliente no Chromium headless](docs/security/chromium-client-certificate.md) |
| Rede | [Transferência de arquivos entre máquinas](docs/network/file-transfer.md) |
| Python | [`http_probe.py`](scripts/http_probe.py): verifica uma URL sem imprimir seu conteúdo |
| Python | [`tibia_characters.py`](scripts/tibia_characters.py): consulta personagens pela API TibiaData |

## Início rápido

Requisitos: Python 3.11 ou mais recente.

```bash
python -m venv .venv
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Exemplos:

```bash
python scripts/http_probe.py https://example.com
python scripts/tibia_characters.py "Bubble"
python -m unittest discover -s tests -v
```

## Princípios do repositório

- Teste comandos em um ambiente descartável antes de usá-los em produção.
- Não armazene senhas, tokens, certificados ou dados internos no Git.
- Exemplos para sistemas fora de suporte são identificados como legados.
- Prefira o princípio do menor privilégio: serviços não devem executar como
  `root` sem necessidade.

## Escopo

Este repositório é um caderno técnico, não uma biblioteca de produção. Os
exemplos são revisados para serem claros e seguros, mas precisam ser adaptados
ao sistema operacional, à rede e às políticas de cada ambiente.
