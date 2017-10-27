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

#getParentA() method
def getParentA():
    return parentA

#getParentB() method
def getParentB():
    return parentB

#married() method
def married(spouseName):
    if spouseName not in people:
        people[spouseName, list()]

        def conceived(spouse, child):
            if spouse in people.keys() != true:
        familyMember[spouse] = new ArrayList<>() #people.put(spouse, new ArrayList<>());

        Lukas.addPersonToHashMap(child)
        people.get(spouse).add(child)

        def getPersonSpouse():
            return people.keys()

            def getChildren(spouse):
                return people.get(spouse)

#getAllKids() method
def getAllKids():
    allKids = []
    result = []
    set = set()

    for kids in people.values():
        allKids.extend(kids)

        for kid in allKids:
            if kid not in set:
                result.add(kid)
                set.add(kid)
                return result

#getKids() method
def getKids(parent):
    return people.get(parent)

    def getHalfSiblings():
        halfSiblings = []
        result = []

        if parentA == None:
            return halfSiblings

            if parentB == None:
                return halfSiblings

                halfSiblings.extend(Lukas.familyMember.get(parentA).getAllKids())
                halfSiblings.extend(Lukas.familyMember.get(parentB).getAllKids())
                halfSiblings.extend(Lukas.familyMember.get(parentA).getKids(parentB))

                return result

#getCousins() method
def getCousins():
    cousins = []
    cousinsNoDup = []
    ancestors = []
    allRelatives = []

    ancestors.extend(Lukas.familyMember.get(name).getAllAncestors())
    allRelatives.extend(Lukas.familyMember.get(name).getAllRelatives())

    cousins.extend(allRelatives)
    cousins = [x for x in cousins if x not in ancestors]

    cousins.remove(name)

    cousinsNoDup = removeDuplicates(cousins)
    return cousinsNoDup

    def firstDescendants():
        desc = []

        if parentA == None:
            desc.add(name)
        else:
            desc.extend(Lukas.familyMember.get(parentA).firstDescendants())

            if parentB == None:
                desc.add(name)
            else:
                desc.extend(Lukas.familyMember.get(parentB).firstDescendants())

                return desc

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

# parent1 = Lukas.familyMember.get(parentA)
#parent2 = Lukas.familyMember.get(parentB)
#ancestors.addAll(parent1.getAllAncestors());
#ancestors.addAll(parent2.getAllAncestors());

for x in ancestors:
    if x in personSet == False:
        result.append(x)
        set.add(x)
        return ancestors;

        def getAllDescendants():
            descendants = []
            allKids = []

            for kids in people.values():
                allKids.extend(kids)

                descendants = allKids

                firstDesc = []
                firstDesc.extend(descendants)

                for person in firstDesc:
                    newKid = Lukas.familyMember.get(person)
                    descendants.extend(newKid.getAllDescendants())

                    return descendants

#getAllRelatives() method
def getAllRelatives():
    allAncestors = []
    allRelatives = []
    result = []
    set = set()

    allAncestors.extend(firstDescendants())
    allRelatives.extend(allAncestors)

    for ancestor in allAncestors:
        Person ancestor1 = Lukas.familyMember.get(ancestor)
        allRelatives.extend(ancestor1.getAllDescendants())

        for relative in allRelatives:
            if relative not in set:
                result.add(relative)
                set.add(relative)

                return result

#removeDuplicates() methods
def removeDuplicates(list):
    result = []
    set = set()

    for item in list:
        if item not in set:
            result.add(item)
            set.add(item)
            return result
