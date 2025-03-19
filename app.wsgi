import os
from app import app  # تأكد من أن اسم الملف الذي يحتوي على التطبيق هو main.py

# تعيين التطبيق كمتغير WSGI الذي ستستخدمه خوادم WSGI
application = app
