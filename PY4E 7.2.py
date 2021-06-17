#What it should do:
#extract lines that starts with "X-DSPAM-Confidence:"
#extract the floating-point number on the line
#count the lines and compute the toal of the spam confidence values
#print the average spam confidence

fileName = input('Enter a filename: ')
try:
    fhand = open(fileName)
    ctr = 0
    total = 0
except:
    print("Cannot open the file or file does not exist")
    quit()


for line in fhand:
    #line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        colonLoc = line.find(":")
        num = line[colonLoc+1:]
        numFloat = float(num)
        total = total + numFloat
        ctr += 1

totalAve = total/ctr

print("Average Spam Confidence:", totalAve)    
print('Total number of lines:', ctr)