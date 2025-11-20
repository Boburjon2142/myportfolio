# Portfolio Achievements (Django 5, Python 3.10, PythonAnywhere-ready)

Ushbu loyiha shaxsiy yutuqlar, ko'nikmalar va kontaktlarni boshqarish uchun yaratilgan. Django 5, SQLite, Bootstrap 5 va tayyor statik/media konfiguratsiyasi bilan PythonAnywhere'ga to'g'ridan-to'g'ri deploy qilishga moslangan.

## Xususiyatlar
- Yutuqlar ro'yxati, filtr, qidiruv, paginatsiya
- Batafsil sahifa: rasm, fayl yuklab olish, tashqi havola
- Vaqt jadvali ko'rinishi (yillar bo'yicha guruhlangan)
- Ko'nikmalar (kategoriya + progress bar)
- Kontakt formasi (DB'ga saqlanadi, xabarlar admin panelda)
- Demo ma'lumotlar uchun `seed_demo_data` komandasi
- Static va media sozlamalari PythonAnywhere uchun tayyor

## Mahalliy o'rnatish
1. `python3.10 -m venv venv`
2. `venv\Scripts\activate` (Linux/macOS: `source venv/bin/activate`)
3. `pip install -r requirements.txt`
4. `copy .env.example .env` (Linux/macOS: `cp .env.example .env`)
5. `.env` faylda `SECRET_KEY` qiymatini sozlang, `DEBUG=True` qoldiring
6. `python manage.py migrate`
7. `python manage.py seed_demo_data`
8. `python manage.py runserver`
9. Brauzerda `http://127.0.0.1:8000/` manziliga o'ting

## Muhim sozlamalar (`portfolio_site/settings.py`)
- `DATABASES` SQLite bilan (`db.sqlite3`)
- `STATIC_URL = "/static/"`, `STATIC_ROOT = BASE_DIR / "staticfiles"`, `STATICFILES_DIRS = [BASE_DIR / "static"]`
- `MEDIA_URL = "/media/"`, `MEDIA_ROOT = BASE_DIR / "media"`
- `ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".pythonanywhere.com"]`
- `CSRF_TRUSTED_ORIGINS = ["https://*.pythonanywhere.com"]`
- `.env` fayli `python-dotenv` orqali yuklanadi

## PythonAnywhere deploy
1. PythonAnywhere'da hisob yarating.
2. Kodingizni yuklang yoki GitHub'dan klon qiling: `/home/<username>/portfolio_site` yo'lida bo'lsin.
3. Virtualenv yarating: `python3.10 -m venv /home/<username>/portfolio_site/venv`
4. Aktivlashtiring: `source /home/<username>/portfolio_site/venv/bin/activate`
5. Talablar: `pip install -r /home/<username>/portfolio_site/requirements.txt`
6. `.env` faylini yarating (copy `.env.example`), `DEBUG=False` va kuchli `SECRET_KEY` qo'ying.
7. Migratsiya: `cd /home/<username>/portfolio_site && python manage.py migrate`
8. Demo ma'lumot: `python manage.py seed_demo_data` (ixtiyoriy)
9. Statik fayllar: `python manage.py collectstatic`
10. PythonAnywhere "Web" bo'limida yangi Django app yarating, kod yo'lini `/home/<username>/portfolio_site` qilib belgilang.
11. WSGI fayli (`/var/www/<username>_pythonanywhere_com_wsgi.py`) ichiga quyidagilarni kiriting yoki mavjudini moslang:
    ```python
    import os
    import sys

    path = "/home/<username>/portfolio_site"
    if path not in sys.path:
        sys.path.append(path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
12. Static va media mappingni sozlang (Web > Static files):
    - URL: `/static/` → Path: `/home/<username>/portfolio_site/staticfiles`
    - URL: `/media/` → Path: `/home/<username>/portfolio_site/media`
13. Web app'ni "Reload" qiling.

## Foydali komandalar
- `python manage.py seed_demo_data` — demo ma'lumotlar yaratish
- `python manage.py createsuperuser` — admin foydalanuvchi yaratish
- `python manage.py collectstatic` — statik fayllarni `staticfiles` papkasiga yig'ish

## Tuzilma (asosiy)
```
portfolio_site/
├─ manage.py
├─ portfolio_site/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ achievements/
│  ├─ models.py
│  ├─ views.py
│  ├─ admin.py
│  ├─ forms.py
│  └─ management/commands/seed_demo_data.py
├─ templates/
│  ├─ base.html
│  ├─ home.html
│  ├─ timeline.html
│  ├─ skills.html
│  └─ contact.html
├─ static/
│  ├─ css/style.css
│  ├─ js/main.js
│  └─ images/
└─ media/
```

## Eslatma
- `DEBUG=False` holatida media fayllarni PythonAnywhere static mapping orqali xizmat qiling (`/media/` → `media`).
- MySQL yoki gunicorn, whitenoise ishlatilmaydi; PythonAnywhere'ning standart WSGI serveri qo'llaniladi.
