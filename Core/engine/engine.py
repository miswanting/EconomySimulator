from .prototypes import singleton
from .managers import map


class Engine(singleton.Singleton):
    def __init__(self):
        e = map.Place()
        print(e.id)
