#!/bin/bash

# Substitui as variáveis de ambiente no arquivo de configuração
envsubst < /etc/presto/templates/hive.properties.template > /etc/presto/catalog/hive.properties

# Executa o comando original do contêiner
exec "$@"
