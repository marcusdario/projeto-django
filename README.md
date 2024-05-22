# projeto-django


python3 -m venv .venv # cria o ambiente pra não confundir o local
source .venv/bin/activate # ativa o ambiente que acabou de ser criado
pip install django


django-admin startproject mysite . # criar a aplicação
python manage.py migrate # cria o banco de dados para a aplicação
python manage.py runserver

