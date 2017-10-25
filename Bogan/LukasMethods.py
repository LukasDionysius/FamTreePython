def getAllSiblings(name):
    siblings_list = []
    if (name.ParentA == None):
        print(siblings_list)
    elif (name.ParentB == None):
        print(siblings_list)
    else:
       # siblings_list = familyMember.get(name.getParentA()).getChildren(name.getParentB())

    return siblings_list;
 
 def VerifyCousin(name1, name2):
    isCousin = False
   # Person person1 = Lukas.familyMember.get(name1);
   # Person person2 = Lukas.familyMember.get(name2);
    ancestors1 = getAllAncestors(person1)
    ancestors2 = getAllAncestors(person2)

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

    return isCousin;
    
    
 ANY LINE WITH A # NEXT TO IT IS SOMETHING WE HAVE NOT FIGURED OUT YET
