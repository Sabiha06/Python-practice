# Assign a message to a variable and print that message
message = "Hello, Aaquib!"
print(message)

# change the value of the variable to a new message and print the new message
message = "Hi, Javed!"
print(message)

#`print a personal message to the person represented in the variable created
var = "Aaquib"
print(f"Hello {var}, would you like to learn some python today?")
print(var.upper())
print(var.lower())
print(var.title())

#Print statement with whitespace characters
famous_person = "John Heywoods"
message = "Out of sight, Out of mind"
print(f"{message}:\n\tby {famous_person}")
name = "\t\nSabiha\n\t"
print(name)

#Using stripping function on variable 'name'
name = ' Sabiha '
name.strip()
print(name)


#Print statement for printing out'Gomez-Acevedo'
instructore = [{'fname': 'Jonathan', 'lname': 'Bona', 'dept': 'Biomedical Informatics'},
               {'fname': 'Horacio', 'lname': 'Gomez-Acevedo', 'dept': 'Biomedical Informatics'}]
print(instructore[1]['lname'])

#What will the code produce as output'99'?
temp = 99
if temp < 60:
    print('Too cold')
elif temp < 90:
    print('okay')
else:
    print('Too hot')

#Add a print statement that outputs the message 'Sabiha Aman became affiliated with UAMS in 2021.
givenName= "Sabiha"
familyName = "Aman"
startYear = 2021
print(f"{givenName} {familyName} became affiliated with UAMS in {startYear}")

#
