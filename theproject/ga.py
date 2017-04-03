from datetime import datetime
import gedcom
birtdate=[]
mardate=[]
def US02bbm():
    for k,i, in gedcom.INDIs.items():
        if i.spouse != 'N/A' :
            for l,m in gedcom.FAMs.items():
                if i.spouse == m.famid and i.birthday != 'N/A' and m.married != 'N/A':
                    birtdate= datetime.strptime(i.birthday, '%d %b %Y')
                    mardate= datetime.strptime(m.married, '%d %b %Y')
                    if  birtdate > mardate:
                        print("ERROR: FAMILY: US02: " + m.famid + ": Marriage "
                            + m.married + " after " + i.indiid + " Birth " +
                            i.birthday)
