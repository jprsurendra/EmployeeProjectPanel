# import os
# from django.utils.translation import ugettext_lazy as _
# DEBUG = True
# LOCAL_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://127.0.0.1:8000'
# APP_URL = 'http://192.168.0.205:8000'
APP_URL = 'http://192.168.29.213:8000'

USE_I18N = True
EMAIL_PREFIX = 'DEV-DFF-SSR-'


# STATIC_ROOT = (LOCAL_BASE_DIR + '/static/')

# Paypal live account
# PAYPAL_TEST = False
# PAYPAL_RECEIVER_EMAIL = "rahul@jiffyship.in"
# PAYPAL_IDENTITY_TOKEN = "AORtxI9qfzr2gjl1w3OZCeVUVeFnx5f6VN_3EQJSpU9cNw2XADrYKbiG4gy"
# ACTION_NAME = "https://www.paypal.com/cgi-bin/webscr"

# Paypal Sandbox Account Details -Don't override these details
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = "operations@freightmango.com" #"tech@jiffyship.in"
PAYPAL_IDENTITY_TOKEN = "LyJojT0ip_DbfPW-nNmdY6HmO1y_wdBcc5IY3vdTJ3eoYH2wyQchxAwHRoq"
ACTION_NAME = "https://www.sandbox.paypal.com/cgi-bin/webscr"

SKIP_PAYMENT=True

# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_BROKER_URL = 'redis://localhost'
# CELERY_RESULT_BACKEND = 'redis://localhost'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Africa/Nairobi'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_fm_20201115_1_uat3',
        # 'NAME': 'db_fm_uat_20201115_1',
        # 'NAME': 'db_fm_20201115_1_uat',
        'OPTIONS': {
            # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER'",
            'charset': 'utf8'
        },
        'USER': 'root',
        'PASSWORD': 'Admin@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


FONT_DIRCTORY_PATH ="/home/jiffy/JiffyHome/dff_venv3/lib/python3.6/site-packages/fpdf/font/"

ENCRYPT_KEY = 'DHLrbx592iBnOv41gpstHhN8kK9HzUM2qgfys2d7MaQ='

IP_FOR_PAYPAL = 'http://192.168.29.213:8000'

SKIP_PAYMENT = True

CURRENCY_UPLIFT = 0

CURRENCY_UPLIFT_UPLOAD = 0.2

BCC_EMAIL = 'surendra.rathore@freightmango.com' # noreply@freightmango.com
SUPPORT_EMAIL = 'surendra.rathore@freightmango.com'
# DEFAULT_SALES_MANAGER_EMAIL = 'sales.jiffyship@protonmail.com'
# DEFAULT_OPERATION_MANAGER_EMAIL = 'operations.jiffyship@protonmail.com'
DEFAULT_SALES_MANAGER_EMAIL = 'sales@testfreightmango.com'
DEFAULT_OPERATION_MANAGER_EMAIL = 'operations@testfreightmango.com'

BOOKING_EXPIRY_REMINDER_CC_EMAIL = 'surendra.rathore@jiffyship.in'

FINANCE_EMAIL = 'sanjoy.de.123@jiffyship.in, aa@aa.com'
AMOUNT_MISMATCH_SCHEDULER_EMAILS = ['sushmita.alreja@jiffyship.in']
CONTACT_US = ['surendra.rathore@freightmango.com', 'pradeep.sharma@freightmango.com']
IMAP_EMAIL = 'jiffyship.currency.exchange@gmail.com'
IMAP_EMAIL_PASSWORD = 'zzzz'

TASK_INVOKE_INTERVAL = 20 # in Seconds

IS_UAT_ENV = False

ENABLE_GA_CODE = False

