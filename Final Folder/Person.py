class Person(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.spouses = []
        self.firstDescendants = True

    def getname(self):
        return self.name

    def getparents(self):
        return self.parents

    def setparents(self, parent1, parent2):
        if parent1 not in self.parents:
            self.parents.append(parent1)
        if parent2 not in self.parents:
            self.parents.append(parent2)
        self.firstDescendants = False

    def getchildren(self):
        return self.children

    def addchild(self, child):
        if child not in self.children:
            self.children.append(child)

    def getspouses(self):
        return self.spouses

    def addspouse(self, spouse):
        if spouse not in self.spouses:
            self.spouses.append(spouse)

    def isFD(self):
        return self.firstDescendants
