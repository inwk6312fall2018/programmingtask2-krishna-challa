def crime():        #list of crimes
 info = open("Crime.csv","r") #opening the csv file
 a = dict()
 list = []
 for line in info:
    line=line.strip()
    array = line.split(',')
    list.append(array[-1])  #appending info
 for i in list: #running for loop
    if(i not in a):  #checking in the dictionary
      a[i]=1         #if not, values remain 
    else:
      a[i]+=1           # if  present adding count value
 print ("{:<27} {:<15}".format('CrimeType','CrimeID'))# table formatt 
 for m, n in a.items():   # printing table format
    CrimeID = n
    print("{:<30} {:<200}".format(m, CrimeID))
crime() # function call
