from datetime import datetime
import gedcom
deaddate=[]
divdate=[]
def US06bbm():
    for k,i, in gedcom.INDIs.items():
        if i.death != 'N/A' and i.spouse != 'N/A':
            for l,m in gedcom.FAMs.items():
                if i.spouse == m.famid and m.divorced != 'N/A':
                    deaddate= datetime.strptime(i.death, '%d %b %Y')
                    divdate= datetime.strptime(m.divorced, '%d %b %Y')
                    if  deaddate < divdate:
                        print("ERROR: FAMILY: US06: " + m.famid + ": Divorce "
                            + m.divorced + " after " + i.indiid + " Death " +
                            i.death)
