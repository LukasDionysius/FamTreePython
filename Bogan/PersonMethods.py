class Person:
    name = ""
    parentA = None
    parentB = None
    validAncestor = True
    people = {}

    def Person(self, name):
        self.name = name

    def setParentA (self, parentA):
        self.parentA = parentA
        validAncestor = False

    def setParentB (self, parentB):
        self.parentB = parentB
        validAncestor = False

    def getUnrelated(self):
        unrelated = set([])
       # unrelated.addAll(Lukas.familyMember.keySet());
       # unrelated.removeAll(Lukas.familyMember.get(name).getAllRelatives());
        return unrelated;

    def getAllAncestors(self):
        ancestors = set([])
        result = []
        personSet = set()

        if self.parentA == None:
            return ancestors;
        if self.parentB == None
            return ancestors;
        if self.validAncestor == True:
            if 'name' in ancestors == False:
                ancestors.add(self.name)

        ancestors.add(self.parentA)
        ancestors.add(self.parentB)

        #   parent1 = Lukas.familyMember.get(parentA)
        #  parent2 = Lukas.familyMember.get(parentB)
        #  ancestors.addAll(parent1.getAllAncestors());
        #  ancestors.addAll(parent2.getAllAncestors());

        for x in ancestors:
            if x in personSet == False:
                result.append(x)
                set.add(x)
        return ancestors;


ANY LINE WITH A # IN FRONT OF IT IS SOMETHING WE HAVE NOT FIGURED OUT YET
