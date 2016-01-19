# Eventex

Sistema de Eventos encomendado pela Morena

[![Code Climate](https://codeclimate.com/github/gigante/eventex/badges/gpa.svg)](https://codeclimate.com/github/gigante/eventex)
[![Build Status](https://travis-ci.org/gigante/eventex.svg?branch=master)](https://travis-ci.org/gigante/eventex)

## Como Desenvolver

1. Clone o repositório
2. Crie um VirtualEnv com python 3.5
3. Ative o seu VirtualEnv
4. Instale as dependências
5. Configure a instância de desenvolvimento com o .env
6. Execute os Testes

```console
git clone git@github.com:gigante/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o Deploy

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```