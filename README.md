# Пример базового проекта Django + Dokku + Poetry + DRF
### Установленные зависимости:
Весь список - см. pyproject.toml

- DRF Spectacular для Swagger + Schema + Docs

- Jazzmin Для админки

- Whitenoise обслуживает статику

- Включен Lint on save

- Проект включает кастомную модель пользователя без Username

- Для обслуживания JWT авторизации, регистрации, отправки email используется Djoser

- Логирование в файл debug.log

Для установки зависимостей и VENV
```
poetry install
```

## Запуск проекта на локалке
0. Создаем БД в pg_admin у указываем доступы в docker/env/local.env
1. Устанавливаем зависимости и миграции через Makefile
```
make init
```
2. Запускаем dev server через VS code
```
F5 на клавиатуре :)
```

## Деплой на сервер с установленным Dokku
### Если приложение уже создано на сервере
1. Добавляем удаленный репозиторий и связываем с репу SSH ключем
```
git remote add dokku dokku@178.57.218.178:django-boilerplate
git config core.sshCommand 'ssh -i $HOME/.ssh/id_rsa_apps' 

```
2. Пушим - дальше докку все делает сам
```
git push dokku master
```
### Создание приложения и БД на сервере
1. Создаем приложение
```
dokku apps:create django-boilerplate
```
2. Создаем БД и связываем с приложением
```
dokku postgres:create django-boilerplate-pg
dokku postgres:link django-boilerplate-pg django-boilerplate
```
3. Устанавливаем конфиги
```
dokku config:set --no-restart django-boilerplate DEBUG=False
dokku config:set --no-restart django-boilerplate DJANGO_ALLOWED_HOSTS=*
dokku config:set --no-restart django-boilerplate DJANGO_SECRET_KEY=$(echo `openssl rand -base64 100` | tr -d \=+ | cut -c 1-64)
dokku config:set --no-restart django-boilerplate EMAIL_HOST="smtp.yandex.ru"
dokku config:set --no-restart django-boilerplate EMAIL_PORT=465
dokku config:set --no-restart django-boilerplate EMAIL_HOST_USER="example_user"
dokku config:set --no-restart django-boilerplate EMAIL_HOST_PASSWORD="example_password"
dokku config:set --no-restart django-boilerplate EMAIL_USE_SSL="True"
dokku config:set --no-restart django-boilerplate DEFAULT_FROM_EMAIL="example_email@yandex.ru"
dokku config:set --no-restart django-boilerplate DOKKU_LETSENCRYPT_EMAIL=info@webtronics.ru
dokku dockerfile:set django-boilerplate docker/dokku/Dockerfile
```
4. После первого деплоя устанавливаем SSL
```
dokku letsencrypt:enable django-boilerplate
```