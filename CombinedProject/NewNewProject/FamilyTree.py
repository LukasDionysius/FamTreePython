from Person import *
import sys

__author__ = 'Lukas'

familytree = {}


def main():
    for line in sys.stdin:
        readData(line)


def setName(name):
    # sets a person's name

    familytree[name] = Person(name)


def getParents(name):
    # gets both parents of a specific person
    if name not in familytree:
        return []

    person = familytree[name]
    parentlist = person.getparents()

    return parentlist


def checkParents(parent, person):
    # checks to see if parent is a parent of person

    p = familytree[person]
    parent_list = p.getparents()

    if p.isae() and parent == person:
        return True

    if parent in parent_list:
        return True
    else:
        return False


def getSpouses(name):
    # gets all the spouses of a person

    p = familytree[name]
    return p.getspouses()


def checkSpouse(spouse, person):
    # checks to see if spouse is a spouse of a person

    p = familytree[person]
    spouse_list = p.getspouses()
    if spouse in spouse_list:
        return True
    else:
        return False


def getChildren(name):
    # gets all the children of a person

    p = familytree[name]
    return p.getchildren()


def checkChildren(child, person):
    # checks to see if child is a child of person

    p = familytree[person]
    childrenlist = p.getchildren()
    if child in childrenlist:
        return True
    else:
        return False


def addSpouse(spouse1, spouse2):
    # adds spouse 1 to spouse2's spouse list, and vice versa

    s1 = familytree[spouse1]
    s2 = familytree[spouse2]

    s1.addspouse(spouse2)
    s2.addspouse(spouse1)


def addParents(person, parent1, parent2):
    # adds parents to a persons parent list

    p = familytree[person]

    p.setparents(parent1, parent2)


def checkSiblings(person1, person2):
    # checks to see if person 1 and person 2 are full siblings (share the same parents)
    if getParents(person1) != [] and getParents(person1) != []:
        if set getParents(person1)) == set getParents(person2)):
            return True
        else:
            return False
    else:
        return False


def getAllSiblings(person):
    # returns the full siblings of a person, only those who share the same parents
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
    # returns all the ancestors of a person recursively

    ancestor_list = []
    person = familytree[person]

    if person.isae():
        ancestor_list.append(person.name)

    if person.getparents() is None:
        return list(sorted(set(ancestor_list)))

    ancestor_list = ancestor_list + person.getparents()

    for x in person.getparents():
        ancestor_list = ancestor_list + getAncestors(x)

    return list(sorted(set(ancestor_list)))


def checkAncestors(person1, person2):
    # checks to see if person 2 is person1's ancestor

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
    # checks to see if to people have common ancestors

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


def checkAllCousins(person1, num_cousin, num_removal, person2):
    # checks to see if person 2 is person1's ancestor

    if person1 not in familytree:
        return False

    if person2 not in familytree:
        return False

    if person2 in getAllCousins(person1, num_cousin, num_removal):
        return True
    else:
        return False


def getAllUnrelated(person):
    # gets a list of unrelated people...brute force because I'm lazy and not above that..
    unrelated_list = []

    for x in familytree:
        if checkAllUnrelated(x, person):
            unrelated_list.append(x)

    return list(sorted(set(unrelated_list)))


def checkAllUnrelated(person1, person2):
    # check to see if person1 is unrelated to person2

    if person1 not in getAllRelatives(person2):
        return True
    else:
        return False


def readData(input_line):
    input_line = input_line.upper()
    print("\n" + input_line)
    tokens = input_line.split()

    if tokens[0].lower() == 'e':
        name1 = tokens[1]
        name2 = tokens[2]
        name3 = tokens[3]

        # make sure the parents are actually people, if not add them to the hash
        if name1 not in familytree:
            setName(name1)
        if name2 not in familytree:
            setName(name2)

        # if there is no child passed, add the spouses if they arent already
        if name3 is None and not (checkSpouse(name1, name2)):
            addSpouse(name1, name2)

        # if there is a child, and the parents are spouses already, just add the child
        elif checkSpouse(name1, name2):

            if name3 not in familytree:
                setName(name3)

            p1 = familytree[name1]
            p2 = familytree[name2]
            c = familytree[name3]

            p1.addchild(name3)
            p2.addchild(name3)

            c.setparents(name1, name2)

        # if the parents aren't married, and they don't have the child listed, create all connections
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

    elif tokens[0].lower() == 'x':
        if len(tokens) == 4:
            x(tokens[1], tokens[2], tokens[3])

    elif tokens[0].lower() == 'w':
        if len(tokens) == 3:
            w(tokens[1], tokens[2])


def x(person1, relation, person2):
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

    if relation.lower() == "sibling":
        print("Yes.") if checkSiblings(person1, person2) else print("No.")

    elif relation.lower() == "spouse":
        print("Yes.") if checkSpouse(person1, person2) else print("No.")

    elif relation.lower() == "parent":
        print("Yes.") if checkParents(person1, person2) else print("No.")

    elif relation.lower() == "ancestor":
        print("Yes.") if checkAncestors(person2, person1) else print("No.")

    elif relation.lower() == "relative":
        print("Yes.") if checkAllRelatives(person1, person2) else print("No.")

    elif relation.lower() == "unrelated":
        print("Yes.") if checkAllUnrelated(person1, person2) else print("No")

    elif relation.lower() == "cousin":
        print("Yes.") if checkAllCousins(person2, person1) else print("No")

    else:
        print("This is not a valid relationship, BRO")

    return None


def w(relationship, person):
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

    elif relationship.lower() == "parent":
        plist = list getParents(person))

        p = familytree[person]
        if p.isae():
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
