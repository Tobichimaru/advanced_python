
class PropertyCreator(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        prefixes = ["get_", "set_", "del_"]
        accessors = {}
        for key in d.keys():
            value = getattr(cls, key)
            for i in range(3):
                if key.startswith(prefixes[i]):
                    accessors.setdefault(
                        key[4:],
                        [None, None, None]
                    )[i] = value
        for name, (getter, setter, deleter) in accessors.items():
            setattr(cls, name, property(getter, setter, deleter, ""))


class Example(metaclass=PropertyCreator):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


if __name__ == "__main__":
    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
