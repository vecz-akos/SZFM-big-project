# szfm-nagy-project

__Projekt téma:__ Ajánlórendszer

Webes felület, ahol felhasználók értékelnek mintákat, majd ezek alapján új ajánlásokat kapnak.

__Közreműködők:__
 - Bródi Máté Gábor
 - Kerekes Konrád Péter
 - Oravecz Ákos

__Start:__
 1. Clone this repository.
 2. Run:
 ```bash
 $ python -m venv venv
 $ source venv/bin/activate
 $ pip install -r requirements.txt
 $ cd ./SZFM-big-project/src
 $ python manage.py migrate
 $ python manage.py makemigrations
 $ python manage.py createsuperuser
 $ python manage.py runserver
 ```
 3. At first, go to `http://127.0.0.1:8000/admin`, log in, create categories and samples.
 4. Go to `http://127.0.0.1:8000`. Now, you can use the webapp!
