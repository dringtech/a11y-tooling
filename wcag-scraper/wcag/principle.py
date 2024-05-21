from .guideline import Guideline
from .wcag_element import WCAGElement


class Principle(WCAGElement):
    def __init__(self, soup):
        super().__init__(soup, 'h2')
        guidelines = self._soup.find_all(
            'section', class_="guideline", recursive=False)
        self.guidelines = [Guideline(g).as_dict() for g in guidelines]
