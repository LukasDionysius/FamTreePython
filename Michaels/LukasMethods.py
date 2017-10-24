def addPersonToHashMap(name):
	if name not in familyMember: 
            familyMember[name] = new Person(name)


def verifyRelation(name1, relation, name2)
	if name1 not in familyMember:
		return "No"
	elif name2 not in familyMember:
		return "No"
	elif relation == "sibling":
		if name1 in getAllSiblings(familyMember.get(name2)):
			return "Yes"
		else:
			return "No"
		elif relation == "ancestor":
			if name1 in familyMember.get(name2).getAllAncestors():
				return "Yes"
			else:
				return "No"   
		elif relation == "parent":
			if familyMember.get(name2).getParentA() == name1: 
				return "Yes"
			elif familyMember.get(name2).getParentB() == name1: 
				return "Yes"
			else:
                return "No"
		elif relation == "spouse":
			if name1 in familyMember.get(name2).getPersonSpouse(): 
				return "Yes"
			else:
				return "No"
		elif relation == "cousin":
			verifyCousin = verifyCousin(name1, name2)
			if verifyCousin == true:
				return "Yes"
			else:
				return "No"
		elif relation == "half-sibling":
			if name1 in familyMember.get(name2).getHalfSiblings():
				return "Yes"
			else:
				return "No"
		elif relation == "unrelated":
			if name1 in familyMember.get(name2).getUnrelated(): 
				return "Yes"
			else:
				return "No"
		else:
			return "No"
        
    
