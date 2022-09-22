# Payment System
## Description
This web app allows to pay for items using Stripe


## Installation
1) git clone https://github.com/margulanz/payment.git
2) cd payment
3) pip install pipenv
4) pipenv install
5) pipenv shell
6) python Test/manage.py migrate
7) python Test/manage.py createsuperuser` & create a django admin account for you to use locally
8) python Test/manage.py runserver

## Endpoints
- /buy/{id}/
get -> returns session id

- /item/{id}
get -> uses 'buy/{id}/' to get session id and redirects to stripe web app


