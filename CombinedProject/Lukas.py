import java.util.*;
import java.io.*;

public class Lukas {

    static HashMap<String, Person> familyMember = new HashMap<String, Person>();

    /***
     *
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {

        System.out.println("\n" + "Programming Languages Family Tree - Java 2017" + "\n\n");
        System.out.println("Instructions" + "\n" + "Please input a valid query:");

        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            String line = "";

            while (line != null) {
                line = in.readLine();
                line = line.toLowerCase();
                bw.write(readData(line));
            }
            bw.close();

        } catch (IOException ex) { }
        catch (NullPointerException ex2) { }
    }

    /***
     *
     * @param line single line fed to program
     * @return depending on first param (E, X, W) performs task
     * Handles the 'E' event
     */
    public static String readData(String line) {

        String name1, name2, name3, relationship, result = "";
        String[] queryData = line.split(" ");
        char queryChar = line.charAt(0);

        if (queryChar == 'E' || queryChar == 'e') {
            try {
                name1 = queryData[1];
                name2 = queryData[2];
                name3 = queryData[3];

                addPersonToHashMap(name1);
                addPersonToHashMap(name2);
                addPersonToHashMap(name3);

                familyMember.get(name1).married(name2);
                familyMember.get(name2).married(name1);

                familyMember.get(name3).setParentA(name1);
                familyMember.get(name3).setParentB(name2);

                familyMember.get(name1).conceived(name2, name3);
                familyMember.get(name2).conceived(name1, name3);
            } catch (ArrayIndexOutOfBoundsException e) { }

            if (queryData[2] != null) {
                name1 = queryData[1];
                name2 = queryData[2];

                addPersonToHashMap(name1);
                addPersonToHashMap(name2);
                familyMember.get(name1).married(name2);
                familyMember.get(name2).married(name1);
            }
        } else if (queryChar == 'X' || queryChar == 'x') {
            name1 = queryData[1];
            relationship = queryData[2];
            name2 = queryData[3];
            result = "\n" + line + "\n" + verifyRelation(name1, relationship, name2) + "\n";
            System.out.print(result);
        } else if (queryChar == 'W' || queryChar == 'w') {
            relationship = queryData[1];
            name1 = queryData[2];
            result = "\n" + line + "\n" + relatedTo(relationship, name1);
            System.out.print(result);
        } else {
            result = "\n" + line + "\nis not a valid query\n";
        }

        return result;
    }
    
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
    
    def getAllSiblings(name):
      siblings_list = []
      if (name.ParentA == None):
        print(siblings_list)
      elif (name.ParentB == None):
        print(siblings_list)
      else:
        # siblings_list = familyMember.get(name.getParentA()).getChildren(name.getParentB())

      return siblings_list;
      
     #removeDuplicates() methods
     def removeDuplicates(list):
      result = []
      set = set()

      for item in list:
        if item not in set:
            result.add(item)
            set.add(item)
     return result
