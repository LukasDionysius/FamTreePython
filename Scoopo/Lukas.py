#removeDuplicates() methods
def removeDuplicates(list):
    result = []
    set = set()

    for item in list:
        if item not in set:
            result.add(item)
            set.add(item)
    return result

#relatedTo() method
def relatedTo(relation, name1):
    relativeType = []
    relativeTypeNoDup = []
    if name1 not in familyMember:
        return ""
    elif relation == "spouse":
        relativeType.extend(familyMember.get(name1).getPersonSpouse())
    elif relation == "sibling":
        relativeType.extend(getAllSiblings(familyMember.get(name1)))
    elif relation == "parent":
        p1 = familyMember.get(name1).getParentA()
        p2 = familyMember.get(name1).getParentB()
        if p1 == "" || p2 == "":
            return ""
        relativeType.add(p1)
        relativeType.add(p2)

    elif relation == "ancestor":
        relativeType.extend(familyMember.get(name1).getAllAncestors())
    elif relation == "cousin":
        relativeType.extend(familyMember.get(name1).getCousins())
    elif relation == "unrelated":
        relativeType.extend(familyMember.keySet())
        relativeType = [x for x in relativeType if x not in familyMember.get(name1).getAllRelatives()]
    else:
        return "Invalid Relation"

    members = ""
    relativeType.sort()
    relativeTypeNoDup = removeDuplicates(relativeType)

    for (relative in relativeTypeNoDup):
        if relative != name1:
            members += relative + "\n"

    return members