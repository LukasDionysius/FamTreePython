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

#getKids() method
def getKids(parent):
    return people.get(parent)

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
