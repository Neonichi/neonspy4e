#Read and parse the “From” lines and pull out the addresses from the line. 
#Count the number of messages from each person using a dictionary. 
# After all the data has been read, print the person with the most occurrences by 
# creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most occurrence.

userInput = input("Enter a file name: ")
try:
    fhand = open(userInput)
    
except:
    print('That is not a valid file.')
    quit()

counts = dict()

for line in fhand:
 if line.startswith('From:'):
    words = line.split()
    for item in words:
        counts[item] = counts.get(item,0) + 1

keys_to_remove=['From:'] #removes "From:" from the dict

for email in keys_to_remove:
   del counts[email] #deletes the keys specified above

myList = list()
for email,count in counts.items():
    myList.append((count,email)) 

myList = sorted(myList, reverse = True)

for count,email in myList[:1]: #only 1 gets printed out 
    print(email,count)
