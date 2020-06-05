from .. import lib


class MapManager:
    def __init__(self):
        self.__data = {
            children: {}
        }

    @classmethod
    def new_place(self, name=None, parent=None, children=None, neighbors=None):
        return Place(name, parent, children, neighbors)

    def append(self, place):
        self.__data['children'][place.id] = place.dump()

    def reset(self):
        pass

    def load(self, data):
        pass

    def dump(self):
        data = {
            'children': []
        }
        for key in self.__data.keys():
            data['children'][key] = self.__data[key].dump()
        return data


class Place:
    def __init__(self, name=None, parent=None, children=None, neighbors=None):
        self.id = lib.random_hash()
        self.name = name
        self.parent = parent
        self.children = children
        self.neighbors = neighbors

    def load(self, data):
        self.id = data['id']
        self.name = data['name']
        self.parent = data['parent']
        self.children = data['children']
        self.neighbors = data['neighbors']

    def dump(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent': self.parent,
            'children': self.children,
            'neighbors': self.neighbors,
        }


if __name__ == "__main__":
    p = Place()
