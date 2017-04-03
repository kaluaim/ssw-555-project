from datetime import datetime
import gedcom
deaddate=[]
def US30bbm():
    for k,i in gedcom.INDIs.items():
        if i.spouse != 'N/A' :
            if i.death == 'N/A':
                print('INFO: INDIVIDUAL: US30: ' + i.indiid + ': Is alive and married.')
