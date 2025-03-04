import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Basic settings
SECRET_KEY = 'your-secret-key-here'  # You should generate a unique secret key for security
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Modify as necessary for deployment

# Media files settings (for uploading and serving 3D models)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files settings (optional, for serving CSS, JS, etc.)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # Limit file upload size to 10 MB

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Ensure your app is listed here
]

# Database configuration (using SQLite as an example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # You can use PostgreSQL, MySQL, etc. here
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Authentication settings (optional, for login and user authentication)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Middleware settings (ensure to keep the default ones for security and performance)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'LINKSHUB.urls'

# WSGI application (to run the application in production)
# settings.py
WSGI_APPLICATION = 'LINKSHUB.wsgi.application'

# Templating settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],      # Point to the templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation settings (you can adjust these for security)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Add custom settings if needed (e.g., logging, email configuration, etc.)

