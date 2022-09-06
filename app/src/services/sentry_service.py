
import logging
from utils import string_to_bool
import sentry_sdk
from sentry_sdk import (capture_exception,capture_message,set_level)
from common.constants import LOG_FORMAT
from decouple import config
from functools import wraps

logging.basicConfig(format=LOG_FORMAT)
log = logging.getLogger(__name__)

# environmental variable setup
SENTRY_DNS = config('SENTRY_DNS')
SENTRY_RELEASE = config('SENTRY_RELEASE')
SENTRY_SAMPLE_RATE = config('SENTRY_SAMPLE_RATE') 
SENTRY_ENVIRONMENT = config('SENTRY_ENVIRONMENT')
SENTRY_REQUEST_BODY = config('SENTRY_REQUEST_BODY')
SENTRY_DEBUG = config("SENTRY_DEBUG")
SENTRY_LEVEL = config("SENTRY_LEVEL")

class SentryService:
    """
        Sentry service integrates the Sentry to provide more insight on logs
        and exceptions that might occur while run this application
    """
    def __init__(self) -> None:
        pass

    def init(self) -> None :
        sentry_sdk.init(
            dsn=SENTRY_DNS,
            debug=string_to_bool(SENTRY_DEBUG) ,
            release=SENTRY_RELEASE,
            environment=SENTRY_ENVIRONMENT,
            sample_rate=float(SENTRY_SAMPLE_RATE),
            attach_stacktrace=True,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0
        )
        set_level(SENTRY_LEVEL)

def capture_expection_with_sentry(func):
    @wraps(func)
    def decorate(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            log.error(
                "::.. capturing error message { %s :: %s }",
                func.__name__, e)
            capture_exception(e)
    return decorate

def capture_message_with_sentry(func):
    @wraps(func)
    def decorate(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            log.error(
                "::.. capturing error message { %s :: %s }",
                func.__name__, e)
            capture_message(e)
    return decorate




if __name__ == "__main__":
    @capture_expection_with_sentry
    def fx(a):
        print(f"a : {a} ")
        division_by_zero = a / 0
    try:
        SentryService().init()
        fx(2)
    except ZeroDivisionError as e:
        log.error(e)

