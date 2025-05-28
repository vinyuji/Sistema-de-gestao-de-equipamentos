# Sistema-de-gestao-de-equipamentos
Esse sistema tende a ajudar as pessoas a fazer gerenciamento de equipamentos de forma simples  e interativo


gerar o ambiente virtual

    python -m venv venv

entrar no modo venv no Windowns

    .\venv\Scripts\activate

Caso nao ative o ambiente virtual no powershell, rode antes de ativar

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


Instalar o django 

    pip install django

Criar Projeto Python

    django-admin startproject meu_site

# Para rodar o server teste

Entre no diretorio do projeto

    Cd .\Meu_projeto\

Rode no terminal o bash abaixo para rodar o servidor

    python manage.py runserver

Sair do Ambiente virtual

    deactivate

# Para instalar as dependencias em outras maquinas 

    pip install -r requirements.txt

# Criar apps (funcionalidas)

    python manage.py startapp nome_do_app
