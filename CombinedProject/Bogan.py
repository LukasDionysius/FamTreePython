import io
import sys
class Person():
    def __init__ (self, n):
        self.name = n
        self.parentA = None
        self.parentB = None
        self.validAncestor = True
        self.children = []
        self.people = {}

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

        # Lukas.addPersonToHashMap(child) Can't call Lukas directly, must call instance. should be back in Lukas
        self.people.get(spouse).append(child)

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

class Lukas():

    familyMember = {}


    def readData(self, ln):
        name1 = ""
        name2 = ""
        name3 = ""
        relationship = ""
        result = ""

        queryData = ln.split(" ")
        queryChar = ln[0]

        if queryChar == 'E' or queryChar == 'e':
            name1 = queryData[1]
            name2 = queryData[2]
            name3 = queryData[3]
            print:name1
            print:name2
            print:name3

            self.addPersonToHashMap(name1)
            self.addPersonToHashMap(name2)
            self.addPersonToHashMap(name3)

            self.familyMember.get(name1).married(name2)
            self.familyMember.get(name2).married(name1)

            self.familyMember.get(name3).setParentA(name1)
            self.familyMember.get(name3).setParentB(name2)

            self.familyMember.get(name1).conceived(name2, name3)
            self.familyMember.get(name2).conceived(name1, name3)
            self.addPersonToHashMap(self.familyMember.get(name3))

        if queryData[2] != "":
            name1 = queryData[1]
            name2 = queryData[2]
            self.addPersonToHashMap(name1)
            self.addPersonToHashMap(name2)
            self.familyMember.get(name1).married(name2)
            self.familyMember.get(name2).married(name1)
        elif queryChar == 'X' or queryChar == 'x':
            name1 = queryData[1]
            relationship = queryData[2]
            name2 = queryData[3]
            result = "\n" + ln + "\n" + self.verifyRelation(name1, relationship, name2) + "\n"
            print: result
        elif queryChar == 'W' or queryChar == 'w':
            relationship = queryData[1]
            name1 = queryData[2]
            result = "\n" + ln + "\n" + self.relatedTo(relationship, name1)
            print: result
        else:
            result = "\n" + ln + "\nis not a valid query\n"

        return result



    print: "\n" + "Programming Languages Family Tree - Java 2017" + "\n\n"
    print: "Instructions" + "\n" + "Please input a valid query:"


 #   try:
#    bw = BufferedWriter(new OutputStreamWriter(System.out))
#    input = BufferedReader(new InputStreamReader(System.in))
    def main (self):
        line = ""

        input = sys.stdin
        output = sys.stdout


        for line in input:
            line = line.lower()
            output.write(line)
            print(line)
            print("hello")

            self.readData(line)
            output.write(self.readData(line))
        output.close()

#    except


    def addPersonToHashMap(self, name):
        if name not in Lukas.familyMember:
            Lukas.familyMember[name] = Person(name)


    def verifyRelation(self, name1, relation, name2):
        if name1 not in self.familyMember:
            return "No"
        elif name2 not in self.familyMember:
            return "No"
        elif relation == "sibling":
            if name1 in self.getAllSiblings(self.familyMember.get(name2)):
                return "Yes"
            else:
                return "No"
        elif relation == "ancestor":
            if name1 in self.familyMember.get(name2).getAllAncestors():
                return "Yes"
            else:
                return "No"
        elif relation == "parent":
            if self.familyMember.get(name2).getParentA() == name1:
                return "Yes"
            elif self.familyMember.get(name2).getParentB() == name1:
                return "Yes"
            else:
                return "No"
        elif relation == "spouse":
            if name1 in self.familyMember.get(name2).getPersonSpouse():
                return "Yes"
            else:
                return "No"
        elif relation == "cousin":
            verifyCousin = self.verifyCousin(name1, name2)
            if verifyCousin == True:
                return "Yes"
            else:
                return "No"
        elif relation == "half-sibling":
            if name1 in self.familyMember.get(name2).getHalfSiblings():
                return "Yes"
            else:
                return "No"
        elif relation == "unrelated":
            if name1 in self.familyMember.get(name2).getUnrelated():
                return "Yes"
            else:
                return "No"
        else:
            return "No"


    # relatedTo() method
    def relatedTo(self, relation, name1):
        relativeType = []
        relativeTypeNoDup = []
        if name1 not in self.familyMember:
            return ""
        elif relation == "spouse":
            relativeType.extend(self.familyMember.get(name1).getPersonSpouse())
        elif relation == "sibling":
            relativeType.extend(self.getAllSiblings(self.familyMember.get(name1)))
        elif relation == "parent":
            p1 = self.familyMember.get(name1).getParentA()
            p2 = self.familyMember.get(name1).getParentB()
            if p1 == "" or p2 == "":
                return ""
            relativeType.add(p1)
            relativeType.add(p2)

        elif relation == "ancestor":
            relativeType.extend(self.familyMember.get(name1).getAllAncestors())
        elif relation == "cousin":
            relativeType.extend(self.familyMember.get(name1).getCousins())
        elif relation == "unrelated":
            relativeType.extend(self.familyMember.keySet())
            relativeType = [x for x in relativeType if x not in self.familyMember.get(name1).getAllRelatives()]
        else:
            return "Invalid Relation"

        members = ""
        relativeType.sort()
        relativeTypeNoDup = self.removeDuplicates(relativeType)

        for relative in relativeTypeNoDup:
            if relative != name1:
                members += relative + "\n"

        return members

    def verifyCousin(self, name1, name2):
            isCousin = False
            person1 = Person(Lukas.familyMember.get(name1))
            person2 = Person(Lukas.familyMember.get(name2))
            ancestors1 = self.getAllAncestors(person1)
            ancestors2 = self.getAllAncestors(person2)

            for x in ancestors1:
                for y in ancestors2:
                    if x == y:
                        isCousin == True

            for x in ancestors1:
                if x == name2:
                    isCousin == False

            for y in ancestors2:
                if y == name1:
                    isCousin == False

            return isCousin

    def getAllSiblings(self, name):
            siblings_list = []
            if (name.ParentA == None):
                print(siblings_list)
            elif (name.ParentB == None):
                print(siblings_list)
            else:
                siblings_list = self.familyMember.get(name.getParentA()).getChildren(name.getParentB())

            return siblings_list

            # removeDuplicates() methods

    def removeDuplicates(self, list):
            result = []
            set = set()

            for item in list:
                if item not in set:
                    result.add(item)
                    set.add(item)

            return result



L = Lukas()
L.main()
