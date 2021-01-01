fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
sumTot = 0
totSum = 0
for str in fhand:
    if str.startswith('X-DSPAM-Confidence:'):
        lenStr = len(str)
        colonIndex = str.find(":")
        strNum = str[colonIndex + 1:lenStr]
        floatNum = float(strNum.strip())
        count = count + 1
        totSum = totSum + floatNum
        spamConf = totSum/count
print('Average spam confidence: ',spamConf)
