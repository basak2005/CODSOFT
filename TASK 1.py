#==== A GREAT TO-DO APPLICATION MADE WITH PYTHON
#==== SPECIALITY IS THAT IT STORE note DOCUMENT ALONG WITH THE DATE AND TIME OF CREATION OF note
#==== FILE OPEARION OF PYTHOMN IS GREATLY USED HERE TO MAKE VARIOUS OPERATION ON FILES
#==== TIME MODULE IS USED TO TRACK CURRENT SYSTEM TIME WHEN THE note IS MADE
#==== OS MODULE IS ALSO USED TO REMOVE ANY SELECTED note FIE FROM THE DIRECTORY WHERE THIS PROGRAMME RUNS
#==== CREATING FILE
#==== SHOWING EXISTING TO-DO ALONG WITH DATE AND TIME OF CREATION
#==== DELETING EXISTING TO-DO WITH UPGRADATION OF NEW LIST OF EXISTING FILE AFTER DELETATION
#==== MODIFYING TO-DO FEATURING:1. ERASING THE TO-DO IN THE FILE AND WRITTING NEW IN FILE, 2. APPENDING NEW TO-DO WITH EXISTING TO-DO IN A FILE
#==== READING THE EXISTING TO-DO CONTENT






#MODULE INITIALIZED----------------
from time import ctime
import os

#LOOP TAKEN WITH VALUE (TRUE) FOR CONTINIOUS INPUT TAKING FACILLITY---------------
while(True):
    name_li=[] #FOR STORING FILE NAMES FOR TEMPORARY AND MAKING OPERTION WITH IT AS NEEDED
    time_li=[] #FOR STORING TIMES FOR TEMPORARY AND MAKING OPERTION WITH IT AS NEEDED
    print("------------------To-Do List---------------")
    print("PRESS THE FOLLOWING TO AVAIL FACILLITIES")

    #INSTRUCTION GIVEN TO USER------------------
    print("1. CREATE NEW LIST\n2. SHOW AVAILABLE LIST\n3. DELETE EXISTING LIST\n4. MODIFY EXISTING LIST\n5. READ FILE\n6. EXIT")
    
    #INPUT TAKEN FOR WHICH OPERATION TO PERFORM-----------------------
    option=int(input("ENTER THE OPTION: "))
    
    if(option==1):

        #FETCHING THE CURRENT SYSTEM TIME WHEN USER WRITTING NOTES----------
        time_store=ctime()

        #FILE NAME CHOOSED BY THE USER--------
        name=str(input("ENTER FILE NAME(WRITE WITHOUT EXTENTION): "))

        #USERS CONTENT IN THE FILE
        note=input("ENTER THE NOTE: ")

        #FILE OPERATION FOR OPENING NEW FILE AND INSERT THE CONTENT ALONG WITH TIME(WHEN THE CONTENT IS WRITTEN)----------------
        with open(f"{name}.txt","w") as f:
            f.write(f"WRITTEN ON:::{time_store}\n{note}")
            f.close()

            #APPENDING NEW FILE NAME AND TIME IN A LIST FOR TEMPORARY BASIS-----------
            name_li.append(f"{name}.txt\n")
            time_li.append(time_store+"\n")

        #PERMENENTLY STORE THE FILE NAME FROM THE LIST TO A TEXT FILE FOR FUTURE USE---------------    
        with open("output_file.txt","a") as g:
            g.writelines(name_li)
            g.close()
                
        #PERMENENTLY STORE THE TIME FROM THE LIST TO A TEXT FILE FOR FUTURE USE---------------        
        with open("output_time.txt","a") as h:
            h.writelines(time_li)
            h.close()

    elif(option==2):

        print()
        print("FILE NAME     TIME")
        print()

        #TAKING OUT ALL PREVOUSLY CREATED FILE IN A TEMPORARY LIST TO SHOW USER-------------------
        f=open("output_file.txt", "r")
        name_li=f.readlines()
        f.close()

        #TAKING OUT TIME AND DATE OF CREATION OF THE FILE------------------------
        f=open("output_time.txt", "r")
        time_li=f.readlines()
        f.close()

        #SHOWING THE USER ABOUT HIS PREVIUSLY CREATED FILE AND TIME, DATE OF CREATION--------------
        for i,j in zip(name_li,time_li):
            print(f"{i}                {j}")


    elif(option==3):

        #TAKING FILE NAME FROM USER WHICH HAVE TO BE DELETED----------------------
        user=input("ENTER FILE NAME(WRITE WITH EXTENTION): ")

        ##########REMOVING#######
        os.remove(user)

        #TAKING OUT THE PREVIOUS FILE NAME FROM THE PERMENENT FILE TO A TEMPORARRY LIST---------
        f=open("output_file.txt", "r")
        name_li=f.readlines()
        f.close()

        #TAKING OUT THE TIME AND DATE OF CREATION---------------------
        f=open("output_time.txt", "r")
        time_li=f.readlines()
        f.close()

        #UPDATE THE TEMPORARY FILE NAME LIST AND TIME LIST WITH POP AND REMOVING DELETED ITEMS(FILES)  
        x=0
        x=name_li.index(f"{user}\n")
        name_li.remove(f"{user}\n")

        #NOW UPDATE THE PERMENENT TXT FILE CONTAINING AVAILABLE note FILE WITH THE TEMPORARRY LIST (DATE AND TIME FILE ALSO) 
        with open("output_file.txt","w") as g:
            g.writelines(name_li)
            g.close()
        time_li.pop(x)
        with open("output_time.txt","w") as g:
            g.writelines(time_li)
            g.close()

    elif(option==4):

        #TAKING TEXT FILE NAME FROM USER TO UPDATE OR ERASE THE EXISTING DATA IN IT
        user=input("ENTER FILE NAME(WITHOUT EXTENTION): ")
        mode=input("ENTER r+ FOR DELETE PREVIOUS ALL AND WRITE NEW ENTER a+ TO WRITE AFTER THE PREVIOUS ONE: \n")

        #CONTENT TAKING FROM USER
        new=input("ENTER NEW CONTENT: ")

        #THIS MODE FOR ERASING ALL DATA FROM SELECTED FILE AND WRITE IN IT FROM THE BEGINING
        if(mode=="r+"):
            with open(f"{user}.txt", "r+") as file:
                content = file.read()
                print("ORIGINAL CONTENT:", content)
                file.seek(38)  # Move file pointer to the beginning
                file.write(new)
                file.seek(0)  # Move file pointer to the beginning
                content = file.read()
                print("MODIFIED CONTENT:", content)


        #THIS MODE IS FOR APPENDING NEW DATA IN THE SELECTED FILE WITOUT ERASING PREVOUS DATA
        elif(mode=="a+"):
            with open(f"{user}.txt", "a+") as file:
                file.write(f" {new}")
                file.seek(0)  # Move file pointer to the beginning
                content = file.read()
                print("CONTENT AFTER APPENDING:", content)

    elif(option==5):

        #ONLY READNG ANY CONTENT FROM ANY SELECTED FILE------------
        name=str(input("ENTER FILE NAME(WRITE WITHOUT EXTENTION): "))
        print("Your file content:")
        with open(f"{name}.txt", "r") as file:
            print(file.read())

    elif(option==6):

        #BREAKING OUT FROM THE LOOP
        break   
