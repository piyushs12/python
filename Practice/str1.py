str = "i am studying python from Apna College"

print(str.endswith("ege"))

print(str.capitalize()) #It only makes changes in a new string to print

"""To make changes in the str itself write the following command
   str = str.capitalize
   print(str)"""

print(str.replace("o","a"))
print(str.replace("python","javascript"))

#returns the index of the 1st occurence
print(str.find("a"))  
print(str.find("Apna"))
print(str.find("was")) #returns -1