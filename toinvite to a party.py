# #hi! My name is: Mohamed Abdulsalam..
#practice cource..
# #challeange (2.3)
"""Ask the user to enter the names of three people they want toinvite to a party and store them in a list.
 After they have enteredall three names, ask them if they want to add another.
If they do,allow them to add more names until they answer “no”.
Whenthey answer “no”, display how many people they have invited tothe party.
and upload file to GitHub and past the link down
"""
#for GitHub

persons=[]
print("Enter the names of three people they want toinvite to a party :\n")
for i in range(3):
    persons.append(input())

print("People invited to the party")

for pe in range(len(persons)):
    print(str(pe + 1) + "." + persons[pe], end='\n')

add = input("\n Do you want add another ?\n\t\ty or n \n")

while add != 'n' and add != 'y':
    print("Pleace chose yes ( y ) or no ( n )")
    add = input("\n Do you want add another ? \n\t\ty or n\n")
else:
    while add == 'y':
        persons.append(input("Enter the names : "))
        add = input("Do you want add another ?\n\ty or no")
    else:
        print("the count of people that toinvite to party: " + str(len(persons)))
        for pe in range(len(persons)):
            print(str(pe + 1) + "." + persons[pe], end='\t')
