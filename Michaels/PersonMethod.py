def conceived(spouse, child):
	if spouse in people.keys() != true:
		familyMember[spouse] = new ArrayList<>() #people.put(spouse, new ArrayList<>());

	Lukas.addPersonToHashMap(child)
	people.get(spouse).add(child)


def Set<String> getPersonSpouse():
	return people.keys()

def getChildren(spouse):
	return people.get(spouse)

def getHalfSiblings():

	halfSiblings = []
	result = []

	if parentA == None:
		return halfSiblings

	if parentB == None:
		return halfSiblings

	halfSiblings.extend(Lukas.familyMember.get(parentA).getAllKids())
	halfSiblings.extend(Lukas.familyMember.get(parentB).getAllKids())
	halfSiblings.extend(Lukas.familyMember.get(parentA).getKids(parentB))

	return result

def firstDescendants():

	desc = []

	if parentA == None:
		desc.add(name)
	else:
		desc.extend(Lukas.familyMember.get(parentA).firstDescendants())

	if parentB == None:
		desc.add(name)
	else:
		desc.extend(Lukas.familyMember.get(parentB).firstDescendants())
        
	return desc


def getAllDescendants():

	descendants = []
	allKids = []

	for kids in people.values():
		allKids.extend(kids)
        
	descendants = allKids
	
	firstDesc = []
	firstDesc.extend(descendants)

	for person in firstDesc
		newKid = Lukas.familyMember.get(person)
		descendants.extend(newKid.getAllDescendants())

	return descendants
