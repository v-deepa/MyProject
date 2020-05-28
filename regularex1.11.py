import re
#open the file mbox1.txt
fhandle=open("mbox1.txt")
count=0
numlist=list()
for line in fhandle:

    line=line.rstrip()

    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)

    if (len(stuff) !=1):
        continue
    num=float(stuff[0])
    numlist.append(num)

    #if re.search('^X-\S+:', line):
print("maximum",max(numlist))

fhandle.close()


# if re.search('^From.*:',line):
# if re.search('^X-.*:', line):
x="My favouite 2 number is 10 and 41"
y=re.findall('[0-9]+',x)
print(y)

x="FRom: using a s: asdfsda"
y=re.findall('^F.+:',x)
print(y)
y=re.findall('^F.+?:',x)
print(y)

Email="From cwen@iupui.edu Thu Jan  3 16:29:07 $2008"
y=re.findall('^From (\S+@\S+)',Email)
print(y)

y=re.findall('^From .*@([^ ]*)',Email)
print(y)

y=re.findall(' [a-z0-9]',Email)
print(y)

f="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y=re.findall('@(\S+)',f)
print(y)
