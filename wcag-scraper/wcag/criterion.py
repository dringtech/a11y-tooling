import re

from .wcag_element import WCAGElement


class Criterion(WCAGElement):
    def __init__(self, soup):
        super().__init__(soup, 'h4')
        try:
            self.level = re.sub(pattern=r'^.*?(A+).*$',
                                repl='\g<1>',
                                string=self._soup.find(
                                    'p', class_="conformance-level").text
                                )
        except:
            print(f"{self.title} has no level")
            self.level = None

        self.description = re.sub(
            r'\s+', ' ', string=self._soup.find('p', class_="").text).strip()
