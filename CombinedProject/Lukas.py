import Person.py
import io


class Lukas:

    familyMember = {}


    def readData(self, line):
        name1 = ""
        name2 = ""
        name3 = ""
        relationship = ""
        result = ""

        queryData = line.split(" ")
        queryChar = line.charAt(0)

        if queryChar == 'E' or queryChar == 'e':
            name1 = queryData[1]
            name2 = queryData[2]
            name3 = queryData[3]

            self.addPersonToHashMap(name1)
            self.addPersonToHashMap(name2)
            self.addPersonToHashMap(name3)

            self.familyMember.get(name1).married(name2)
            self.familyMember.get(name2).married(name1)

            self.familyMember.get(name3).setParentA(name1)
            self.familyMember.get(name3).setParentB(name2)

            self.familyMember.get(name1).conceived(name2, name3)
            self.familyMember.get(name2).conceived(name1, name3)

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
            result = "\n" + line + "\n" + self.verifyRelation(name1, relationship, name2) + "\n"
            print: result
        elif queryChar == 'W' or queryChar == 'w':
            relationship = queryData[1]
            name1 = queryData[2]
            result = "\n" + line + "\n" + self.relatedTo(relationship, name1)
            print: result
        else:
            result = "\n" + line + "\nis not a valid query\n"

        return result



    print: "\n" + "Programming Languages Family Tree - Java 2017" + "\n\n"
    print: "Instructions" + "\n" + "Please input a valid query:"


 #   try:
#    bw = BufferedWriter(new OutputStreamWriter(System.out))
#    input = BufferedReader(new InputStreamReader(System.in))
    line = ""

    input = open('input.txt', 'r')
    output = open('output.txt', 'w')

    while line != "":
        line = input.readline()
        line = line.lower()
        output.write(readData(line))
    output.close()

#    except


    def addPersonToHashMap(self, name):
        if name not in self.familyMember:
            self.familyMember[name] = Person(name)


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

        def removeDuplicates(list):
            result = []
            set = set()

            for item in list:
                if item not in set:
                    result.add(item)
                    set.add(item)

        return result
