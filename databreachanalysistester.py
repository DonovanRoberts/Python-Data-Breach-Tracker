with open("C:/Users/DFRob/data_breach.txt", "r") as breaches:
    #print(breaches.read(250))
    lineList = breaches.readlines()

print(lineList)

#create a counter to keep track of how many data breaches per organization type
#HealthCare, Financial, and Government records are found
HealthCare = 0
Financial = 0
Government = 0


#below we are determining which type of organiztion has had the most data breaches
#for line in lineList[1:]:
    #print(line)
    #cleanLine = line.strip()
    #breachesValues = cleanLine.split(',')
    #print(breachesValues)
    #if breachesValues[4] == "healthcare":
        #HealthCare += 1
    #elif breachesValues[4] == "financial":
        #Financial += 1
    #else:
        #breachesValues[4] == "government"
        #Government += 1
#print("Health Care Organizations had", HealthCare, "data leaks,"
      #"Financial Organizations had", Financial, "data leaks,"
      #"Governmental Orginzations had", Government, "data leaks.")

#Once we have ran the above code you will know which one has the most data breaches which should be Goverment Organizations
# From there we will determine the most comomn method of data breachs in Government Organizations
#create a counter to keep track of the occurence of methods per data breach
Hacked= 0
Poor_Security= 0
Lost_Stolen_Media= 0
Accidential_Publish= 0
Inside_Job= 0
 

#we will know set up code to ensure it is only analyzing government organizations by adding an and statement

for line in lineList[1:]:
    print(line)
    cleanLine = line.strip()
    breachesValues = cleanLine.split(',')
    print(breachesValues)
    if breachesValues[4] == "government":
        if breachesValues[5] == "hacked":
            Hacked += 1
        if breachesValues[5] == "poor security":
            Poor_Security += 1
        if breachesValues[5] == "lost / stolen media":
            Lost_Stolen_Media += 1
        if breachesValues[5] == "accidentally published":
            Accidential_Publish += 1
    else:
            if breachesValues[5] == "inside job":
                Inside_Job += 1

print("Goverment Organizations had", Hacked, "data leaks due to hacking", Poor_Security, "data leaks due to poor security",
       Lost_Stolen_Media, "data leaks due to lost and stolen media, ", Accidential_Publish, "data leaks due to accidential publishing and,",
       Inside_Job, "data leaks due to inside jobs.")

with open("C:/Users/DFRob/data_breach.txt", "w") as report:
    report.write(str(len(lineList)-1) + "total data breach cases reviewed")
    report.write("\n Government Organizations had the most data breaches with a total of"+str(Government) +
                 "\n Of all of methods of data breaching, inside jobs were the most common method with a total of"+str(Inside_Job))
    
