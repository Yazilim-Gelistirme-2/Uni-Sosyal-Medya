class Node:
    def __init__(self, id, name, properties=None):
        self.id = id
        self.name = name
        self.properties = properties or {}
        self.neighbors = []

