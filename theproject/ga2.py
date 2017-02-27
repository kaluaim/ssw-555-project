from datetime import datetime
import gedcom
birtdate=[]
deaddate=[]
def US03bbm():
    print("")
    print("user story 03 : birth before death")
    print("")
    for k,i in gedcom.INDIs.items():
        if i.death != 'N/A' :
            birtdate= datetime.strptime(i.birthday, '%d %b %Y')
            deaddate= datetime.strptime(i.death, '%d %b %Y')
            if  birtdate < deaddate:
                
                print("everything is fine. Birth is before death")
                print("Person name is " + i.name)
                print("Birthday " + i.birthday)
                print("death on " + i.death)
                print("")
            else:
                print("error. birth of person after death")
                print("error for person " + i.name)
                print("Birthday " + i.birthday)
                print("death on " + i.death)
                print("")

        

    
     
          
