from datetime import datetime
import gedcom
deaddate=[]
def US30bbm():
    print("")
    print("")
    print("user story 30: List of living married")
    print("")
    print("")
    for k,i in gedcom.INDIs.items():
        if i.spouse != 'N/A' :
            if i.death == 'N/A':
                print("Person name who is married and not dead is " + i.name)
                print("")

        

    
     
          
