from datetime import datetime
import gedcom
deaddate=[]
def US29bbm():
    print("")
    print("")
    print("user story 29: List of living singles")
    print("")
    print("List of deceased is : ")
    for k,i in gedcom.INDIs.items():
        if i.death != 'N/A':
            print(i.name)
