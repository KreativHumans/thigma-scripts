try:
    #Delimiting Character limit
    delimiter=3

    #Confusing charcters list
    confusables="0O1IL"



    #---------------------libraries-----------------------
    import pyperclip
    import random
    import string
    import os

    # Get the current working directory
    cwd = os.getcwd()

    #--------------------character lists-------------------
    chars=string.digits+string.ascii_uppercase

    #removing confusables
    for letter in confusables:
        chars.replace(letter,"")

    #Enrolment Key Generator
    def id_generator(size=15,chars=string.digits+string.ascii_uppercase):
        "Enrolment Key Generator"
        return "-".join(''.join(random.SystemRandom().choice(chars) for _ in range(delimiter)) for k in range(length//delimiter))

    def savetoFile(filename,filedir,method,stringtoWrite):
        "Saves data to a file and closes the file"
        place=os.path.join(cwd,filedir)
        global filelocation
        filelocation=os.path.join(place,filename)
        filelocation.replace("\\\\","\\")
        try:
            os.mkdir(place)
            print("Directory didn't existed and has been created.")
        except FileExistsError:
            pass
        newEnrolmentKeys=open(filelocation,method)
        newEnrolmentKeys.write(stringtoWrite)
        newEnrolmentKeys.close()
        return
        


    #String which are printed to the user
    string1="Enter the length of a generated key (multiple of 3 is great/ 15 is recommended)    : "
    string2="Enter how many keys you need                                                       : "
    string3="Enter the name of the Course (at least 5 characters without comma)                 : "

    #Input character length of a key
    length=False
    while not(length):
        try:
            length=int(input(string1))
            if length%delimiter!=0 or length<10:
                print("Please enter a multiple of 3 greater than 10.")
                length=False
        except ValueError:
            print("Please enter a valid integer.")

    #Input the number of Keys
    howMany=False
    while not(howMany):
        try:
            howMany=int(input(string2))
        except ValueError:
            print("Please enter a valid integer.")


    #input the course name    
    courseName=""
    while len(courseName)<5:
        try:
            courseName=input(string3).strip().replace(",","")
        except ValueError:
            print("Please enter a valid Course Name.")
            



    # Generating Keys 
    generatedKeys=[id_generator(length,chars) for _ in range(howMany)]
#    generatedKeysString="\n".join(generatedKeys)
    
    generatedKeysString="\n".join([f"{courseName} Student {str(index+1).zfill(5)}\n"+generatedKey for index,generatedKey in enumerate(generatedKeys)])
    generatedCompleteString="\n".join([f"{courseName} Student {str(index+1).zfill(5)},"+generatedKey for index,generatedKey in enumerate(generatedKeys)])

    #Copying keys to clipboard, just in case
    pyperclip.copy(generatedKeysString)
    spam = pyperclip.paste()


    #Saving keys to respective files

    #File which should be imported to moodle
    savetoFile("newEnrolmentKeystoMoodle.csv","newKeys","w","groupname,enrolmentkey\n"+generatedCompleteString)


    #File which should be given to Thigma
    savetoFile("newEnrolmentKeystoThigma.csv","newKeys","w",generatedKeysString)



    #Backup File of keys imported to moodle
    savetoFile("backupnewEnrolmentKeystoMoodle.csv","backupKeys","a",generatedCompleteString)


    #Backup File of keys given to Thigma
    savetoFile("backupnewEnrolmentKeystoThigma.csv","backupKeys","w",generatedKeysString)



    print("\n"+"\n"+"\n"+generatedCompleteString)

    print(f"\nSaved {howMany} keys to following files\n"+cwd+"/newKeys/newEnrolmentKeystoMoodle.csv\n"+cwd+"/newKeys/newEnrolmentKeystoThigma.csv\n"+cwd+"/backupKeys/backupnewEnrolmentKeystoMoodle.csv\n"+cwd+"/backupKeys/backupnewEnrolmentKeystoThigma.csv")
    x=input("Press any key to exit the program...")
except Exception as e:
    print("There was an error while running the program.")
    print(e)
    try:
        print(filelocation)
    except:
        pass
    x=input("Press any key to exit the program...")