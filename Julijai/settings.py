"""
*_________________INSTRUCTION__________________
! \-O-/ !!!!!!!!!Attention!!!!!!!!! pleas \-O-/
! If you create a profile through the console,
! then do not forget to go to the admin panel and, more precisely, to Profile users and add your user there, the main thing is to select the name of your user in the first User form, everything else is not important

? Why should I do this? I'm lazy...

TODO: If you don’t do this, then the celiks that will be added through the site will have a lower id (since your profile is not there (when you register on the site, everything is automatically done there, as you register, before you are thrown to the profile page, your the name goes to the profile form, so everything works there :] ) ) and the least that comes out of it is jumping on profiles, Regarded as Kolya, and Olya in the profile, or even an error :/

!!!! SIGN UP!!!!!

? I want to make SOMEONE (not me) able to add posts/story/tags but not through the admin panel, but on the site itself?

TODO: just give this user the status of a super user in the admin panel and that's it, voila, he can freely add / edit posts / stories.

*__________________ИНСТРУКЦИИ___________________

! \-O-/ !!!!!!!!!ВНИМАНИЕ!!!!!!!!! плиз \-O-/
! Если вы будете создавать профиль через консоль, 
! то не забудьте потом перейти в админку и а точнее в Profile users и добавить туда своего юзера, главное выбрать имя своего юзера в первой формочке User все остальное не важно

? Почему я должен сделать это ? Мне лень...

TODO: Если вы этого не сделаете, то челики которые будут добавляться через сайт будут иметь меньший id(так как вашего профиля нет(когда регаешься на сайте, там все автоматом сделано, как регаешься, перед тем как тебя кинут на страницу с профилем, твое имя идет в формочку профиля, так что все там работает :] ) ) и меньшее что из этого выйдет - скачки по профилям, Регались как Коля, а в профиле Оля, или вообще еррор :/ 

!!!!    ЗАРЕГАЙТЕСЬ !!!!!
//and let me sleap

? Я хочу сделать так что бы КТО-ТО(не я) мог добавлять посты/story/теги но не через админку, а на самом сайте ?

TODO: просто дайте этому пользователю статус супер юзера в админке и все, вуаля, он свободно может добавлять/редактировать посты/сторисы.

"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5lm-ij_2i_1#c+p3z#^xj20dl=h&c3eq#2pn_ki^ml*+$c8c1_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# DEBUG = False
# ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',
    
    'ckeditor',
    'corsheaders',
    'django_social_share',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Julijai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'Julijai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_ROOT = BASE_DIR / 'static/images'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'custom',
        'skin': 'moono', #! moono
        'height': 400,
        'width': '100%',
        'codeSnippet_theme': 'monokai',
        'toolbar': 'MyCustomToolbar',
    },
}

CSRF_COOKIE_SECURE = True