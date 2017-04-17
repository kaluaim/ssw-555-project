from datetime import datetime
import gedcom
deaddate=[]
def US29bbm():
    for k,i in gedcom.INDIs.items():
        if i.death != 'N/A':
            print('INFO: INDIVIDUAL: US29: ' + i.indiid + ': Is deceased.')
