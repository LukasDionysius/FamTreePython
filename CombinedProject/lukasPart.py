if queryData[2] != null:
    name1 = queryData[1]
    name2 = queryData[2]
    addPersonToHashMap(name1)
    addPersonToHashMap(name2)
    familyMember.get(name1).married(name2)
    familyMember.get(name2).married(name1)
elif queryChar == 'X' or queryChar == 'x':
    name1 = queryData[1]
    relationship = queryData[2]
    name2 = queryData[3]
    result = "\n" + line + "\n" + verifyRelation(name1, relationship, name2) + "\n"
    print: result
elif queryChar == 'W' or queryChar == 'w':
    relationship = queryData[1]
    name1 = queryData[2]
    result = "\n" + line + "\n" + relatedTo(relationship, name1)
    print: result
else:
    result = "\n" + line + "\nis not a valid query\n"

return result
