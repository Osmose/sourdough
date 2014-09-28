"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py

To extend any settings from settings/base.py here's an example:
INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']
"""
from . import base


# Database
########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sourdough',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
        },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    }
}


# Environment-specific Settings
########################################################################

# Debugging displays nice error messages, but leaks memory. Set this to
# False on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# Hosts that this site is allowed to be run on. Do not keep this blank
# in production.
ALLOWED_HOSTS = []

# Time zone for the current installation. Default is UTC.
# See http://en.wikipedia.org/wiki/List_of_tz_database_time_zones for a
# list of valid timezone values.
#TIME_ZONE = 'UTC'

# Uncomment this line if you are running a local development install
# without HTTPS to disable HTTPS-only cookies.
#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False

# Uncomment to send email to the console, usually only for local
# development.
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Error Reporting
########################################################################

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS


# Security
########################################################################

# Make this unique, and don't share it with anybody. It cannot be blank.
SECRET_KEY = '{{ secret_key }}'
