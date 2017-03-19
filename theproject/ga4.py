from datetime import datetime
import gedcom
deaddate=[]
divdate=[]
def US06bbm():
    print("")
    print("")
    print("user story 06 : death after divorce")
    print("")
    for k,i, in gedcom.INDIs.items():
        if i.death != 'N/A' :
            if i.spouse != 'N/A':
                for l,m in gedcom.FAMs.items():
                    if i.spouse == m.famid :
                        if m.divorced != 'N/A':
                            deaddate= datetime.strptime(i.death, '%d %b %Y')
                            divdate= datetime.strptime(m.divorced, '%d %b %Y')
                            if  deaddate > divdate:
                                print("everything is fine. death is after divorce")
                                print("Person name is " + i.name)
                                print("death " + i.death)
                                print("divorced on " + m.divorced)
                                print("")
                            else:
                                print("error. death of person is before divorce")
                                print("error for person " + i.name)
                                print("death " + i.death)
                                print("divorced on " + m.divorced)
                                print("")
