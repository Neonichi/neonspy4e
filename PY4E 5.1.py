num_sum = 0
ctr = 0

print('Hello human, today we will ask you to input numbers.')
print('You can input as many numbers as you want.')
print('\nIf you think that you have enough numbers, just type "done".')
print('The code will then show you the sum of the numbers, the')
print('amount of numbers you have inputted, and the corresponding')
print('average of the numbers. ☺')

print('Sum total:', num_sum)
print('Beginning Counter:', ctr)
#first two lines declares the value of the variables
#we then print out their values and label them accordingly.

while True: #we place the try except inside the while loop so that when the error occurs, the loop still continues.
    try:
        num = input("\nGive number: ")
        num_sum = num_sum + int(num) #adds the value to the "num_sum" variable.
        ctr += 1 #Since we added a number, we have to increase a number. The same with "ctr = ctr + 1"
    except:
        if num == "done":
            break  # breaks us out of the loop.
        else:   #ignores the input as it is not an integer; we can't use the input given.
            print("That is not an integer.") 

print("\nYou're all set! Here are the results. ☺")


print('\nSum:', num_sum) #prints out the sum
print('Count:', ctr) #prints out the counter
print('Average:', num_sum / ctr) #prints out the average
print('\nThank you and have a great day!\n')