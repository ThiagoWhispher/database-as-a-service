# -*- coding:utf-8 -*-
# Django settings for dbaas project.
import os.path
import sys

# If is running on CI: if CI=1 or running inside jenkins
CI = os.getenv('CI', '0') == '1'

# Include base path in system path for Python old.
syspath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if not syspath in sys.path:
    sys.path.insert(0, syspath)
    
def LOCAL_FILES(path):
    new_path = os.path.abspath(os.path.join(__file__, path))
    return new_path

try:
    from version import RELEASE
except ImportError:
    RELEASE = 'dev'

# Armazena a raiz do projeto.
SITE_ROOT = LOCAL_FILES('../')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#get environment variables for the database
DB_ENGINE = os.getenv('DBAAS_DATABASE_ENGINE', 'django.db.backends.mysql')
DB_NAME = os.getenv('DBAAS_DATABASE_NAME', 'dbaas')
DB_USER = os.getenv('DBAAS_DATABASE_USER', 'root')
DB_PASSWORD = os.getenv('DBAAS_DATABASE_PASSWORD', '')
DB_HOST = os.getenv('DBAAS_DATABASE_HOST', '')
DB_PORT = os.getenv('DBAAS_DATABASE_PORT', '')

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': DB_PORT,                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/%s/' % RELEASE)

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/%s/' % RELEASE

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'media'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n3#i=z^st83t5-k_xw!v9t_ey@h=!&6!3e$l6n&sn^o9@f&jxv'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dbaas.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dbaas.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'base',
    'business',
    'django_services',
    'rest_framework',
    # Uncomment the next line to enable admin documentation:
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_COOKIE_AGE = 43200  # 12 hours
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expire session when browser is closed
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

TEST_DISCOVER_ROOT = os.path.abspath(os.path.join(__file__, '../..'))
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-verbosity 2', '-s', '--no-byte-compile', '-d']
if CI:
    NOSE_ARGS += ['--with-coverage', '--cover-package=application',
                  '--with-xunit', '--xunit-file=test-report.xml', '--cover-xml', '--cover-xml-file=coverage.xml']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING_APP = os.getenv('LOGGING_APP', 'dbaas')
SYSLOG_FILE = None
if os.path.exists('/var/run/syslog'):
    SYSLOG_FILE = '/var/run/syslog'
else:
    SYSLOG_FILE = '/dev/log'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)-23s %(levelname)-7s %(name)s \t %(message)s'
        },
        'syslog_formatter': {
            'format': '%s: #%%(name)s %%(message)s' % LOGGING_APP
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'INFO'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    }
}
