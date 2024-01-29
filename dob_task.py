#setting up storage and lists for names and dob
contents = ""
names = []
dobs = []

#reading in the file
with open('T14 - IO Operations - Input/10-018 IO Operations - Input/Task file/DOB.txt', 'r+', encoding='utf-8') as file:
    contents = file.readlines()

file.close()

#sorting the info into names and dob
for i in range(0,len(contents)):

    person_info = contents[i].split()#splitting each word in each line
    fullname = person_info[0] + ' ' +  person_info[1] #first 2 words are names
    names.append(fullname)
    person_dob = person_info[2] + ' ' + person_info[3] + ' ' + person_info[4] # last 3 are DOB
    dobs.append(person_dob)

#printing results
print('=' * 100)
print("Name")
print('=' * 100)

for name in names:
    print(name)

print('=' * 100)
print("Birthdate")
print('=' * 100)

for dob in dobs:
    print(dob)






