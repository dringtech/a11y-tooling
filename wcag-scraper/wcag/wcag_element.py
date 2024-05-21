import re

from .wcag_base import WCAGBase


class WCAGElement(WCAGBase):
    _private = ['_soup']

    def __init__(self, soup, title_element):
        self._soup = soup
        self.id = self._soup['id']
        label = self._soup.find(class_='secno').text
        self.label = re.sub(r'[\.\s]+$', '', label)
        self.title = self._soup.find(
            title_element).text.replace(label, '').strip()
        self.description = re.sub(
            r'\s+', ' ', string=self._soup.p.text).strip()
