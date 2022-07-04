import hmac
import logging
from hashlib import sha256
from mimetypes import guess_extension
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible
from requests import get


logger = logging.getLogger(__name__)
TOKEN_FILE = settings.SECRETS.SECRET_TOKEN_FILE.encode('UTF-8')


def get_hased_item(item) -> str:
    return hmac.new(
        TOKEN_FILE,
        str(item).encode('UTF-8'),
        digestmod=sha256
    ).hexdigest()


def get_ext(filename: str) -> str:
    if filename.rfind('.') == -1:
        return ''
    else:
        return filename.split('.')[-1]


@deconstructible
class file_path(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename: str):
        ext = get_ext(filename)
        name = get_random_string(20)
        return Path(self.path) / f'{name}.{ext}'


@deconstructible
class hashed_path:

    def __init__(self, sub_path, attr):
        self.path = sub_path
        self.attr = attr

    def __call__(self, instance, filename: str):
        ext = get_ext(filename)
        name = get_hased_item(getattr(instance, self.attr))

        return Path(self.path) / f'{name}.{ext}'


def download_file(url: str | None) -> File | None:
    try:
        if not url:
            return

        with get(url, allow_redirects=True, stream=True) as res:

            if res.status_code != 200:
                return

            content_type = res.headers.get('Content-Type')
            ext = guess_extension(content_type)
            temp = NamedTemporaryFile(suffix=ext)

            for chunk in res.iter_content(8192):  # 1024 * 8
                temp.write(chunk)

        return File(temp)
    except Exception as e:
        logger.exception(e)
