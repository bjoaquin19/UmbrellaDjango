rmdir /s /q .venv
call py -m pip install --upgrade pip
call pip install --upgrade virtualenv
call py -m venv .venv
call .venv\Scripts\activate.bat
call py -m pip install --upgrade pip
call pip install django
call pip install pillow
call pip install djangorestframework
call pip install transbank-sdk
call pip install django-extensions
call pip install -r requirements.txt