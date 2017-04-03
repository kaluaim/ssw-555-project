from datetime import datetime
import gedcom
deaddate=[]
def US31bbm():
    print("")
    print("")
    print("user story 31: List of living singles")
    print("")
    print("")
    for k,i in gedcom.INDIs.items():
        if i.spouse == 'N/A' :
            if i.death == 'N/A':
                print("Person name who is single and not dead is " + i.name)
                print("")
