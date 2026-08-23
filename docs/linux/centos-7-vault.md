# Repositórios Vault do CentOS 7

> [!WARNING]
> CentOS Linux 7 está fora de suporte. O Vault preserva pacotes históricos,
> mas não oferece novas correções de segurança. Use este procedimento somente
> para recuperação ou migração de ambientes legados.

O arquivo de exemplo está em
[`examples/yum/centos-7-vault.repo`](../../examples/yum/centos-7-vault.repo).

Faça backup da configuração atual e instale o arquivo:

```bash
sudo cp -a /etc/yum.repos.d /etc/yum.repos.d.backup
sudo install -m 0644 examples/yum/centos-7-vault.repo \
  /etc/yum.repos.d/centos-7-vault.repo
sudo yum clean all
sudo yum makecache
```

O objetivo deve ser estabilizar temporariamente o sistema e planejar a
migração para uma distribuição suportada.
