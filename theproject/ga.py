from datetime import datetime
import gedcom
birtdate=[]
mardate=[]
def US02bbm():
    print("user story 02: birth before marriage")
    for k,i, in gedcom.INDIs.items():
        if i.spouse != 'N/A' :
            for l,m in gedcom.FAMs.items():
                if i.spouse == m.famid :
                    birtdate= datetime.strptime(i.birthday, '%d %b %Y')
                    mardate= datetime.strptime(m.married, '%d %b %Y')
                    if  birtdate < mardate:
                        print("everything is fine. Birth is before marriage")
                        print("Person name is " + i.name)
                        print("Birthday " + i.birthday)
                        print("Married on " + m.married)
                        print("")
                    else:
                        print("error. birth of person after marriage")
                        print("error for person " + i.name)
                        print("Birthday " + i.birthday)
                        print("Married on " + m.married)
                        print("")
