import gedcom
import ga
import ga2
import ga3
import ga4


FILE_PATH = './Gedcom1.ged'
if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_familie()  
    ga.US02bbm()
    ga2.US03bbm()
    ga3.US05bbm()
    ga4.US06bbm()
    US22.US22UniqueIDs()
    US22.US22UniqueIDs1()
