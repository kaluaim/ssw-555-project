import gedcom
import ga
import ga2


FILE_PATH = './Gedcom1.ged'
if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_familie()  
    ga.US02bbm()
    ga2.US03bbm()

