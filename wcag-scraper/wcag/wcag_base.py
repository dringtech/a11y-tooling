import json


class WCAGBase(object):
    _private = []

    def as_dict(self):
        safe_dict = {
            k: self.__dict__[k]
            for k
            in self.__dict__ if k not in self._private + ['_private']
        }
        return safe_dict

    def __repr__(self):
        return json.dumps(self.as_dict())
