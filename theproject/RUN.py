import gedcom
import US04
import US02
FILE_PATH = './gedcom123.ged'
if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_families()
    
    US04.US4MbB()
