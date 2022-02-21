

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


if __name__ == '__main__':
    a = Circle(998)
    print(a.radius)
    a.radius = 2000
    print(a.radius)

