# --------------
# Code starts here

#Create list 'class_1' & pass elements 'Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio'.
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

#Create list 'class_2' and pass the elements 'Hilary Mason','Carla Gentry','Corinna Cortes'
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

#Concatenate the 'class_1' and 'class_2'
new_class = class_1 + class_2
print(new_class)
print("="*20)

#Add new element 'Peter Warden' in the list 'new_class'
new_class.append('Peter Warden')
print(new_class)
print("="*20)

#Remove the element 'Carla Gentry' from list 'new_class'
new_class.remove('Carla Gentry')
print(new_class)
print("="*20)

# Code ends here


# --------------
# Code starts here

courses = {"Math" : 65, "English" : 70, "History" : 80, "French" : 70, "Science" : 60 }
print("Marks obtained in Math")
print(courses["Math"])
print('='*10)

print("Marks obtained in English")
print(courses["English"])
print('='*10)

print("Marks obtained in History")
print(courses["History"])
print('='*10)

print("Marks obtained in French")
print(courses["French"])
print('='*10)

print("Marks obtained in Science")
print(courses["Science"])
print('='*10)

total = courses["Math"] + courses["English"] + courses["History"] + courses["French"] + courses["Science"]
percentage = (total / 500 ) * 100
print("percentage scored by Geoffrey Hinton")
print(percentage)
print('='*10)
# Code ends here


# --------------
# Code starts here

mathematics = {"Geoffrey Hinton" : 78, "Andrew Ng" : 95, "Sebastian Raschka" : 65, "Yoshua Benjio" : 50, "Hilary Mason" : 70, "Corinna Cortes" : 66 , "Peter Warden" : 75}
topper = max(mathematics,key = mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here

first_name = topper.split()[0]
last_name = topper.split()[1]
print(first_name)
print(last_name)

full_name = last_name + " " + first_name
print(full_name)

certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


