from pathlib import Path
from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible


@deconstructible
class file_path(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        name = get_random_string(20)
        return Path(self.path) / f'{name}.{ext}'
