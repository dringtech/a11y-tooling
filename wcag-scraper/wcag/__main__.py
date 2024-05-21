import sys
from . import WCAG



try:
    (url, target) = sys.argv[1:3]
except ValueError:
    print('Please provide url and target file as parameters')    


WCAG(url).to_json(target)


