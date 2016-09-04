# Eventex

Sistema de Eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.2
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:RamiroAlvaro/wttd-eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.X/bin
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?

1. Crie um instância no heroku.
2. Envie as configuraçōes para o heroku.
3. Define una SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```