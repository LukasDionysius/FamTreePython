from Person import *
import sys
__author__ = 'Lukas'

familytree = {}

def main():
    for line in sys.stdin:
       sort_case(line)

def set_person(name):
    # sets a person's name

    familytree[name] = Person(name)

def check_person(name):
    # checks to see if a person is in the list of people

    if name in familytree:
        return True
    else:
        return False

def get_parents(name):
    # gets both parents of a specific person
    if not check_person(name):
        return []

    p = familytree[name]
    parentlist = p.getparents()

    return parentlist

def check_parent(parent, person):
    # checks to see if parent is a parent of person

    p = familytree[person]
    parent_list = p.getparents()

    if p.isae() and parent == person:
        return True

    if parent in parent_list:
        return True
    else:
        return False

def get_spouses(name):
    # gets all the spouses of a person

    p = familytree[name]
    return p.getspouses()

def check_spouse(spouse, person):
    # checks to see if spouse is a spouse of a person

    p = familytree[person]
    spouse_list = p.getspouses()
    if spouse in spouse_list:
        return True
    else:
        return False

def get_children(name):
    # gets all the children of a person

    p = familytree[name]
    return p.getchildren()

def check_children(child, person):
    # checks to see if child is a child of person

    p = familytree[person]
    childrenlist = p.getchildren()
    if child in childrenlist:
        return True
    else:
        return False

def add_child(parent1, parent2, child):
    # adds a child to the childrenlists of parent1 and parent2
    # also sets the parents of the child to parent 1 and parent2
    # used if parent1 and parent2 are already spouses

    p1 = familytree[parent1]
    p2 = familytree[parent2]
    c = familytree[child]

    p1.addchild(child)
    p2.addchild(child)

    c.setparents(parent1, parent2)

def add_spouse(spouse1, spouse2):
    # adds spouse 1 to spouse2's spouse list, and vice versa

    s1 = familytree[spouse1]
    s2 = familytree[spouse2]

    s1.addspouse(spouse2)
    s2.addspouse(spouse1)

def add_parents(person, parent1, parent2):
    # adds parents to a persons parent list

    p = familytree[person]

    p.setparents(parent1, parent2)

def add_all_connections(parent1, parent2, child):
    # adds all the connections of a new family
    # add parents to the child
    # adds child to each parent
    # adds parents to each other's spouse lists

    add_parents(child, parent1, parent2)
    add_child(parent1, parent2, child)
    if not check_spouse(parent1, parent2):
        add_spouse(parent1, parent2)

def check_sibs(person1, person2):
    # checks to see if person 1 and person 2 are full siblings (share the same parents)
    if get_parents(person1) != [] and get_parents(person1) != []:
        if set(get_parents(person1)) == set(get_parents(person2)):
            return True
        else:
            return False
    else:
        return False

def get_full_sibs(person):
    # returns the full siblings of a person, only those who share the same parents
    p = familytree[person]
    parents = p.getparents()
    all_siblings = []

    for x in parents:
        par = familytree[x]
        all_siblings = all_siblings + par.getchildren()

    final_siblings = []

    for x in all_siblings:
        if check_sibs(x, person):
            final_siblings.append(x)

    return list(sorted(set(final_siblings)))

def get_ancestors(person):
    # returns all the ancestors of a person recursively

    ancestor_list = []
    person = familytree[person]

    if person.isae():
        ancestor_list.append(person.name)

    if person.getparents() is None:
        return list(sorted(set(ancestor_list)))

    ancestor_list = ancestor_list + person.getparents()

    for x in person.getparents():
        ancestor_list = ancestor_list + get_ancestors(x)

    return list(sorted(set(ancestor_list)))

def check_ancestors(person1, person2):
    # checks to see if person 2 is person1's ancestor

    if person2 in get_ancestors(person1):
        return True
    else:
        return False

def get_relatives(person):
    relative_list = []

    for x in familytree:
        if check_relatives(person, x):
            relative_list.append(x)

    return list(sorted(set(relative_list)))

def check_relatives(person1, person2):
    # checks to see if to people have common ancestors
    if not check_person(person1):
        return False

    p1_ancestors = get_ancestors(person1)
    p2_ancestors = get_ancestors(person2)
    common_ancestors = []

    for x in p1_ancestors:
        if x in p2_ancestors:
            common_ancestors.append(x)

    if common_ancestors:
        return True
    else:
        return False

def get_cousins(person, num_cousin, num_removed):
    personlist1 = [person]
    personlist2 = []

    # gets the shared grandparents
    for x in range(0, num_cousin):

        personlist2.clear()
        for x in personlist1:
            personlist2 = personlist2 + get_parents(x)

        personlist1 = list(set(personlist2))


    # gets the siblings of grandparents
    personlist2.clear()
    for x in personlist1:
        personlist2 = personlist2 + get_full_sibs(x)


    personlist2 = set(personlist2) - set(personlist1)

    personlist1 = list(set(personlist2))

    # this gets the children on the proper cousin level
    for x in range(0, (num_cousin + num_removed)):

        personlist2.clear()
        for x in personlist1:
            personlist2 = list(personlist2) + get_children(x)

        personlist1 = list(set(personlist2))

    return list(sorted(set(personlist1)))

def check_cousins(person1,  num_cousin, num_removal, person2):
    # checks to see if person 2 is person1's ancestor
    if not check_person(person1) or not check_person(person2):
        return False

    if person2 in get_cousins(person1, num_cousin, num_removal):
        return True
    else:
        return False

def get_unrelated(person):
    # gets a list of unrelated people...brute force because I'm lazy and not above that..
    unrelated_list = []

    for x in familytree:
        if check_unrelated(x, person):
            unrelated_list.append(x)

    return list(sorted(set(unrelated_list)))

def check_unrelated(person1, person2):
    # check to see if person1 is unrelated to person2

    if person1 not in get_relatives(person2):
        return True
    else:
        return False

def sort_case(input_line):
    input_line = input_line.upper()
    print("\n" + input_line)
    tokens = input_line.split()

    if tokens[0].lower() == 'e':
        name1 = tokens[1]
        name2 = tokens[2]
        name3 = tokens[3]

        # make sure the parents are actually people, if not add them to the hash
        if not check_person(name1):
            set_person(name1)
        if not check_person(name2):
            set_person(name2)

        # if there is no child passed, add the spouses if they arent already
        if name3 is None and not (check_spouse(name1, name2)):
            add_spouse(name1, name2)

        # if there is a child, and the parents are spouses already, just add the child
        elif check_spouse(name1, name2):
            if not check_person(name3):
                set_person(name3)

            add_child(name1, name2, name3)

        # if the parents aren't married, and they don't have the child listed, create all connections
        else:
            if not check_person(name3):
                set_person(name3)

            add_all_connections(name1, name2, name3)

    elif tokens[0].lower() == 'x':
        if len(tokens) == 4:
            x(tokens[1], tokens[2], tokens[3])

    elif tokens[0].lower() == 'w':
        if len(tokens) == 3:
            w(tokens[1], tokens[2])

def x(person1, relation, person2):
        if not check_person(person1):
            if person1 == person2 or relation.lower() == "unrelated":
                print("Yes.")
            else:
                print("No.")
            return None

        if not check_person(person2):
            if person1 == person2 or relation.lower() == "unrelated":
                print("Yes.")
            else:
                print("No.")
            return None

        if relation.lower() == "sibling":
            print("Yes.") if check_sibs(person1, person2) else print("No.")

        elif relation.lower() == "spouse":
            print("Yes.") if check_spouse(person1, person2) else print("No.")

        elif relation.lower() == "parent":
            print("Yes.") if check_parent(person1, person2) else print("No.")

        elif relation.lower() == "ancestor":
            print("Yes.") if check_ancestors(person2, person1) else print("No.")

        elif relation.lower() == "relative":
            print("Yes.") if check_relatives(person1, person2) else print("No.")

        elif relation.lower() == "unrelated":
            print("Yes.") if check_unrelated(person1, person2) else print("No")

        elif relation.lower() == "cousin":
            print("Yes.") if check_cousins(person2, person1) else print("No")

        else:
            print("This is not a valid relationship, BRO")

        return None

def w(relationship, person):
    if not check_person(person):
        if relationship.lower() == "unrelated":
            print(list(sorted(set(familytree))))
        else:
            print([])
        return None

    if relationship.lower() == "sibling":
        print(list(sorted(set(get_full_sibs(person)))))

    elif relationship.lower() == "spouse":
        print(list(sorted(set(get_spouses(person)))))

    elif relationship.lower() == "parent":
        plist = list(get_parents(person))

        p = familytree[person]
        if p.isae():
            plist.append(person)
        print(list(sorted(set(plist))))

    elif relationship.lower() == "ancestor":
        print(list(sorted(set(get_ancestors(person)))))

    elif relationship.lower() == "relative":
        print(list(sorted(set(get_relatives(person)))))

    elif relationship.lower() == "unrelated":
        print(list(sorted(set(get_unrelated(person)))))

    elif relationship.lower() == "cousin":
        print(list(sorted(set(get_cousins(person)))))

    else:
        print("This is not a valid relationship.")

main()
