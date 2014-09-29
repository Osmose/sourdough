"""
Base django settings for sourdough.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Django Settings
########################################################################

INSTALLED_APPS = (
    # Project-specific apps
    'sourdough.base',

    # Third-party apps
    'django_nose',
    'pipeline',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
)

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'sourdough.urls'

WSGI_APPLICATION = 'sourdough.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Test config
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Third-party Libary Settings
########################################################################
# Add any settings for third-party libraries here.

# Jinja environment config (via jingo)
JINJA_CONFIG = {
    'extensions': [
        'pipeline.jinja2.ext.PipelineExtension',
    ],
}

# Content Security Policy (via django-csp)
CSP_SCRIPT_SRC = (
    '"self"',
)
CSP_STYLE_SRC = (
    '"self"',
)


# Project-specific Settings
########################################################################
# Add any project-specific settings here.

# CSS bundles
PIPELINE_CSS = {
    'common': {
        'source_filenames': (
          'css/base.css',
        ),
        'output_filename': 'css/common.css',
        'extra_context': {
            'media': 'screen,projection,tv',
        },
    },
}

# JS Bundles
PIPELINE_JS = {}
