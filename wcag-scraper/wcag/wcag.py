import json

import requests
from bs4 import BeautifulSoup

from .principle import Principle
from .wcag_base import WCAGBase


class WCAG(WCAGBase):
    _private = ['_soup']

    def __init__(self, url):
        r = requests.get(url)
        self._soup = BeautifulSoup(r.text, 'html.parser')
        self.principles = [Principle(p).as_dict() for p in self._soup.body.find_all(
            'section', class_='principle')]

    def to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.as_dict(), f, indent=2)
