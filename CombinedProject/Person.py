class Person:
    name = ""
    parentA = None
    parentB = None
    validAncestor = True
    people = {}

    def Person(n):
        name = n

    def setParentA(self, parentA):
        self.parentA = parentA
        validAncestor = False

    def setParentB(self, parentB):
        self.parentB = parentB
        validAncestor = False

    # getParentA() method
    def getParentA(self):
        return self.parentA

    # getParentB() method
    def getParentB(self):
        return self.parentB

    # married() method
    def married(self, spouseName):
        if spouseName not in self.people:
            self.people[spouseName] = []

    def conceived(self, spouse, child):
        if spouse not in self.people.keys():
            self.people[spouse] = []  # people.put(spouse, new ArrayList<>());

        Lukas.addPersonToHashMap(child)
        self.people.get(spouse).add(child)

    def getPersonSpouse(self):
        return self.people.keys()

    def getChildren(self, spouse):
        return self.people.get(spouse)

    # getAllKids() method
    def getAllKids(self):
        allKids = []
        result = []
        set = set()

        for kids in self.people.values():
            allKids.extend(kids)

        for kid in allKids:
            if kid not in set:
                result.add(kid)
                set.add(kid)
        return result

        # getKids() method
    def getKids(self, parent):
        return self.people.get(parent)

    def getHalfSiblings(self):
        halfSiblings = []
        result = []

        if self.parentA == None:
            return halfSiblings

        if self.parentB == None:
            return halfSiblings

        halfSiblings.extend(Lukas.familyMember.get(self.parentA).getAllKids())
        halfSiblings.extend(Lukas.familyMember.get(self.parentB).getAllKids())
        halfSiblings.extend(Lukas.familyMember.get(self.parentA).getKids(self.parentB))

        return result

        # getCousins() method
    def getCousins(self):
        cousins = []
        cousinsNoDup = []
        ancestors = []
        allRelatives = []

        ancestors.extend(Lukas.familyMember.get(self.name).getAllAncestors())
        allRelatives.extend(Lukas.familyMember.get(self.name).getAllRelatives())

        cousins.extend(allRelatives)
        cousins = [x for x in cousins if x not in ancestors]

        cousins.remove(self.name)

#        cousinsNoDup = self.removeDuplicates(cousins)
        return cousins #cousinsNoDup

    def firstDescendants(self):
        desc = []

        if self.parentA == None:
            desc.add(self.name)
        else:
            desc.extend(Lukas.familyMember.get(self.parentA).firstDescendants())

        if self.parentB == None:
            desc.add(self.name)
        else:
            desc.extend(Lukas.familyMember.get(self.parentB).firstDescendants())

        return desc

    def getUnrelated(self):
        unrelated = []
        unrelated.extend(Lukas.familyMember.keySet())
        unrelated = [x for x in unrelated if x not in Lukas.familyMember.get(self.name).getAllRelatives()]

        return unrelated

    def getAllAncestors(self):
        ancestors = []
        result = []
        personSet = set()

        if self.parentA == None:
            return ancestors
        if self.parentB == None:
            return ancestors
        if self.validAncestor == True:
            if 'name' in ancestors == False:
                ancestors.add(self.name)

        ancestors.add(self.parentA)
        ancestors.add(self.parentB)

        parent1 = Lukas.familyMember.get(self.parentA)
        parent2 = Lukas.familyMember.get(self.parentB)
        ancestors.extend(parent1.getAllAncestors())
        ancestors.extend(parent2.getAllAncestors())

        for x in ancestors:
            if x in personSet == False:
                result.append(x)
                set.add(x)
        return ancestors

    def getAllDescendants(self):
        descendants = []
        allKids = []

        for kids in self.people.values():
            allKids.extend(kids)

            descendants = allKids

            firstDesc = []
            firstDesc.extend(descendants)

            for person in firstDesc:
                newKid = Lukas.familyMember.get(person)
                descendants.extend(newKid.getAllDescendants())

            return descendants

            # getAllRelatives() method

    def getAllRelatives(self):
        allAncestors = []

        allRelatives = []
        result = []
        set = set()

        allAncestors.extend(self.firstDescendants())
        allRelatives.extend(allAncestors)

        for ancestor in allAncestors:
            Person
            ancestor1 = Lukas.familyMember.get(ancestor)
            allRelatives.extend(ancestor1.getAllDescendants())

        for relative in allRelatives:
            if relative not in set:
                result.add(relative)
            set.add(relative)

        return result

        # removeDuplicates() methods
    def removeDuplicates(list):
        result = []

        set = set()

        for item in list:
            if item not in set:
                result.add(item)
                set.add(item)
        return result
