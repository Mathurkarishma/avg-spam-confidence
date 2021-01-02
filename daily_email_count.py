#This program will ask the user for a file and count how many times emails are sent on each particular day of the week

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    #If the user inputted an invalid file name, program will exit
list = []
#Stores the days of the week as many times as it's listed in the file
counts = dict()
#Stores the frequency each word occurs
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    #Only selecting words from the email line
    words = line.split()
    list.append(words[2])
    #Only adding days of the week to the list
for line in list:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
            #First time loop, it will add the unique word to the list
        else:
            counts[word] += 1
            #Second time loop, it will add another count to the word already in the list
print(counts)
#Prints frequency

#End of script
