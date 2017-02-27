from datetime import datetime
import gedcom
birtdate=[]
deaddate=[]
def US03bbm():
    for k,i in gedcom.INDIs.items():
        if i.death != 'N/A' and i.birthday != 'N/A':
            birtdate= datetime.strptime(i.birthday, '%d %b %Y')
            deaddate= datetime.strptime(i.death, '%d %b %Y')
            if  birtdate > deaddate:
                print('ERROR: INDIVIDUAL: US03: ' + i.indiid + ': Birthday ' +
                    i.birthday + ' afrer death: ' + i.death)
