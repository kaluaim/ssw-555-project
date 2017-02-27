from datetime import datetime, timedelta
import gedcom
divdate=[]
mardate=[]
def US4MbD():
    for k,i in gedcom.FAMs.items():
        if i.divorced != 'N/A' and i.married != 'N/A':
            divdate = datetime.strptime(i.divorced, '%d %b %Y')
            mardate = datetime.strptime(i.married, '%d %b %Y')
            if divdate < mardate:
                print('ERROR: FAMILY: US04: ' + i.famid + ': Divorce ' +
                    i.divorced + ' after marriage ' + i.married)

mardate=[]
def US08bbmp():
    for l,m in gedcom.FAMs.items():
        if m.married != 'N/A':
            #If the person is married check for bday and id
            for k,i, in gedcom.INDIs.items():
                id1=i.indiid
                #Identify the child using
                if id1 in m.children:
                    bday = datetime.strptime(i.birthday, '%d %b %Y')
                    p_married = datetime.strptime(m.married, '%d %b %Y')
                    if bday<p_married:
                        print('ERROR: INDIVIDUAL: US08: ' + i.indiid +
                            ': Birthday ' + i.birthday + ' after ' + m.famid +
                            ' marriage ' + m.married)
                    if m.divorced != 'N/A':
                        p_divorced = datetime.strptime(m.divorced, '%d %b %Y')
                        p_divorced = p_divorced + timedelta(9*365/12)
                        if bday > p_divorced:
                            print('ERROR: INDIVIDUAL: US08: ' + i.indiid +
                                ': Birthday ' + i.birthday +
                                ' after 9 months of ' + m.famid + ' divorce ' +
                                m.divorced)
