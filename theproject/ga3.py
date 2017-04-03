from datetime import datetime
import gedcom
deaddate=[]
mardate=[]
def US05bbm():
    for k,i, in gedcom.INDIs.items():
        if i.death != 'N/A' and i.spouse != 'N/A':
            for l,m in gedcom.FAMs.items():
                if i.spouse == m.famid and m.married != 'N/A':
                    deaddate = datetime.strptime(i.death, '%d %b %Y')
                    mardate = datetime.strptime(m.married, '%d %b %Y')
                    if  deaddate < mardate:
                        print("ERROR: FAMILY: US05: " + m.famid + ": Marriage "
                            + m.married + " after " + i.indiid + " Death " +
                            i.death)
