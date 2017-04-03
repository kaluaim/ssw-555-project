from datetime import datetime
import gedcom
deaddate=[]
def US31bbm():
    for k,i in gedcom.INDIs.items():
        if i.spouse == 'N/A' :
            if i.death == 'N/A':
                print('INFO: INDIVIDUAL: US31: ' + i.indiid + ': Is alive and single.')
