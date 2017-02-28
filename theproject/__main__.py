import gedcom
import US0408sourabh as US0408
import util_khalid
import ga, ga2
import US22sourabh

FILE_PATH = 'GEDCOM.ged'

if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_families()

    # Demonstration of user stories
    # US01
    fam_check = util_khalid.check_family_dates_before_current(gedcom.FAMs)
    indi_check = util_khalid.check_individual_dates_before_current(gedcom.INDIs)
    # US02
    ga.US02bbm()
    # US03
    ga2.US03bbm()
    # US04
    US0408.US4MbD()
    # US05

    # US06

    # US07
    util_khalid.check_individual_age_less_than_150(gedcom.INDIs)
    # US08
    US0408.US08bbmp()
    
    US22.US22UniqueIDs()  #sprint 2 user story
