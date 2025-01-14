from .base import *

# Configure the DATABASES setting
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }  
}
# Email Configuration
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# DEFAULT_FROM_EMAIL = "shankar.wxit@gmail.com"
# DOMAIN = os.getenv('DOMAIN')
# SITE_NAME = "Scrum App"


