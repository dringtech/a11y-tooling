from .criterion import Criterion
from .wcag_element import WCAGElement


class Guideline(WCAGElement):
    def __init__(self, soup):
        super().__init__(soup, 'h3')
        criteria = self._soup.find_all(
            'section', class_="guideline", recursive=False)
        self.criteria = [Criterion(c).as_dict() for c in criteria]
