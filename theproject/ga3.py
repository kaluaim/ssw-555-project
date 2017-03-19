from datetime import datetime
import gedcom
deaddate=[]
mardate=[]
def US05bbm():
    print("")
    print("")
    print("user story 05: marriage before death")
    print("")
    for k,i, in gedcom.INDIs.items():
        if i.death != 'N/A' :
            if i.spouse != 'N/A':
                for l,m in gedcom.FAMs.items():
                    if i.spouse == m.famid :
                        deaddate= datetime.strptime(i.death, '%d %b %Y')
                        mardate= datetime.strptime(m.married, '%d %b %Y')
                        if  deaddate > mardate:
                            print("everything is fine. death is after marriage")
                            print("Person name is " + i.name)
                            print("death " + i.death)
                            print("Married on " + m.married)
                            print("")
                        else:
                            print("error. death of person is before marriage")
                            print("error for person " + i.name)
                            print("death " + i.death)
                            print("Married on " + m.married)
                            print("")
