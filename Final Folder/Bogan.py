#!/usr/bin/python

from Person import *
import sys

familytree = {}

def main():
    for line in sys.stdin:
        readData(line)

def setName(name):
    familytree[name] = Person(name)

def getParents(name):
    if name not in familytree:
        return []
    person = familytree[name]
    parentlist = person.getparents()
    return parentlist

def checkParents(parent, person):
    p = familytree[person]
    parent_list = p.getparents()
    if p.isFD() and parent == person:
        return True
    if parent in parent_list:
        return True
    else:
        return False

def getSpouses(name):
    p = familytree[name]
    return p.getspouses()

def checkSpouse(spouse, person):
    p = familytree[person]
    spouse_list = p.getspouses()
    if spouse in spouse_list:
        return True
    else:
        return False

def getChildren(name):
    p = familytree[name]
    return p.getchildren()

def checkChildren(child, person):
    p = familytree[person]
    childrenlist = p.getchildren()
    if child in childrenlist:
        return True
    else:
        return False

def addSpouse(spouse1, spouse2):
    s1 = familytree[spouse1]
    s2 = familytree[spouse2]
    s1.addspouse(spouse2)
    s2.addspouse(spouse1)

def addParents(person, parent1, parent2):
    p = familytree[person]
    p.setparents(parent1, parent2)

def checkSiblings(person1, person2):
    if getParents(person1) != [] and getParents(person1) != []:
        if set(getParents(person1)) == set(getParents(person2)):
            return True
        else:
            return False
    else:
        return False

def getAllSiblings(person):
    p = familytree[person]
    parents = p.getparents()
    all_siblings = []

    for x in parents:
        par = familytree[x]
        all_siblings = all_siblings + par.getchildren()

    final_siblings = []

    for x in all_siblings:
        if checkSiblings(x, person):
            final_siblings.append(x)

    return list(sorted(set(final_siblings)))

def getAncestors(person):
    ancestor_list = []
    person = familytree[person]

    if person.isFD():
        ancestor_list.append(person.name)

    if person.getparents() is None:
        return list(sorted(set(ancestor_list)))

    ancestor_list = ancestor_list + person.getparents()

    for x in person.getparents():
        ancestor_list = ancestor_list + getAncestors(x)

    return list(sorted(set(ancestor_list)))

def checkAncestors(person1, person2):
    if person2 in getAncestors(person1):
        return True
    else:
        return False


def getAllRelatives(person):
    relative_list = []

    for x in familytree:
        if checkAllRelatives(person, x):
            relative_list.append(x)

    return list(sorted(set(relative_list)))


def checkAllRelatives(person1, person2):
    if person1 not in familytree:
        return False

    p1_ancestors = getAncestors(person1)
    p2_ancestors = getAncestors(person2)
    common_ancestors = []

    for x in p1_ancestors:
        if x in p2_ancestors:
            common_ancestors.append(x)

    if common_ancestors:
        return True
    else:
        return False

def getAllCousins(name):
    cousins = []
    ancestors = []
    allRelatives = []

    ancestors.extend(getAncestors(name))
    allRelatives.extend(getAllRelatives(name))

    cousins.extend(allRelatives)
    cousins = [x for x in cousins if x not in ancestors]

    cousins.remove(name)

    return cousins

def checkAllCousins(person1, person2):
    if person1 not in familytree:
        return False

    if person2 not in familytree:
        return False

    if person2 in getAllCousins(person1):
        return True
    else:
        return False

def getAllUnrelated(person):
    unrelated_list = []

    for x in familytree:
        if checkAllUnrelated(x, person):
            unrelated_list.append(x)

    return list(sorted(set(unrelated_list)))

def checkAllUnrelated(person1, person2):
    if person1 not in getAllRelatives(person2):
        return True
    else:
        return False

def checkHalfSiblings(person1, person2):
	parentsList1 = getParents(person1)
	parentsList2 = getParents(person2)

	counter = 0

	for parent1 in parentsList1:
		if parent1 in parentsList2:
			counter=counter+1

	if counter == 1:
		return True
	else:
		return False

def getHalfSiblings(person1):
	siblingsList = getAllSiblings(person1)
	allChildrenList = []
	parentList = getParents(person1)

	for parent in parentList:
		allChildrenList.extend(getChildren(parent))

	allChildrenList = [x for x in allChildrenList if x not in siblingsList]

	return allChildrenList

def readData(input_line):
    input_line = input_line.upper()
    print("\n" + input_line)
    queryData = input_line.split()

    if queryData[0].lower() == 'e':
        name1 = queryData[1]
        name2 = queryData[2]
        name3 = queryData[3]

        if name1 not in familytree:
            setName(name1)
        if name2 not in familytree:
            setName(name2)

        if name3 is None and not (checkSpouse(name1, name2)):
            addSpouse(name1, name2)

        elif checkSpouse(name1, name2):

            if name3 not in familytree:
                setName(name3)

            p1 = familytree[name1]
            p2 = familytree[name2]
            c = familytree[name3]

            p1.addchild(name3)
            p2.addchild(name3)

            c.setparents(name1, name2)

        else:
            if name3 not in familytree:
                setName(name3)

            addParents(name3, name1, name2)

            p1 = familytree[name1]
            p2 = familytree[name2]
            c = familytree[name3]

            p1.addchild(name3)
            p2.addchild(name3)

            c.setparents(name1, name2)

            if not checkSpouse(name1, name2):
                addSpouse(name1, name2)

    elif queryData[0].lower() == 'x':
        person1 = queryData[1]
        relation = queryData[2]
        person2 = queryData[3]

        if len(queryData) == 4:
            if person1 not in familytree:
                if person1 == person2 or relation.lower() == "unrelated":
                    print("Yes.")
                else:
                    print("No.")
                return None

            if person2 not in familytree:
                if person1 == person2 or relation.lower() == "unrelated":
                    print("Yes.")
                else:
                    print("No.")
                return None

            if relation.lower() == "half-sibling":
				if checkHalfSiblings(person1, person2):
					print("Yes.")
				else:
					print("No.")

            if relation.lower() == "sibling":
                if checkSiblings(person1, person2):
                	print("Yes.")
                else:
                	print("No.")

            elif relation.lower() == "spouse":
                if checkSpouse(person1, person2):
                	print("Yes.")
                else:
                	print("No.")

            elif relation.lower() == "parent":
                if checkParents(person1, person2):
                	print("Yes.") 
                else:
                	print("No.")

            elif relation.lower() == "ancestor":
                if checkAncestors(person2, person1):
                	print("Yes.")
                else:
                 	print("No.")

            elif relation.lower() == "relative":
                if checkAllRelatives(person1, person2):
                	print("Yes.")
                else:
                	print("No.")

            elif relation.lower() == "unrelated":
                if checkAllUnrelated(person1, person2):
                	print("Yes.")
                else:
                 	print("No")

            elif relation.lower() == "cousin":
                if checkAllCousins(person2, person1):
                	print("Yes.")
                else:
                	print("No") 

            return None

    elif queryData[0].lower() == 'w':
        relationship = queryData[1]
        person = queryData[2]

        if len(queryData) == 3:
            if person not in familytree:
                if relationship.lower() == "unrelated":
                    print(list(sorted(set(familytree))))
                else:
                    print([])
                return None

            if relationship.lower() == "sibling":
                print(list(sorted(set(getAllSiblings(person)))))

            elif relationship.lower() == "spouse":
                print(list(sorted(set(getSpouses(person)))))

            elif relationship.lower() == "half-sibling":
                print(list(sorted(set(getHalfSiblings(person)))))

            elif relationship.lower() == "parent":
                plist = list(getParents(person))

                p = familytree[person]
                if p.isFD():
                    plist.append(person)
                print(list(sorted(set(plist))))

            elif relationship.lower() == "ancestor":
                print(list(sorted(set(getAncestors(person)))))

            elif relationship.lower() == "relative":
                print(list(sorted(set(getAllRelatives(person)))))

            elif relationship.lower() == "unrelated":
                print(list(sorted(set(getAllUnrelated(person)))))

            elif relationship.lower() == "cousin":
                print(list(sorted(set(getAllCousins(person)))))

            else:
                print("This is not a valid relationship.")

main()
