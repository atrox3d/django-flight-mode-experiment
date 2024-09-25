import os
import django


if __name__ == '__main__':  
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flightmode.settings')
    django.setup()

    from myapp.helpers import db

    db.create_initial_data()


