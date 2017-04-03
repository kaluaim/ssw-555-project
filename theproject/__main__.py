import gedcom
import US0408sourabh, US10and22Sourabh#, US12and36Sourabh
import util_khalid
import ga, ga2, ga3, ga4
import US12andUS36

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
    US0408sourabh.US4MbD()
    # US05
    ga3.US05bbm()
    # US06
    ga4.US06bbm()
    # US07
    util_khalid.check_individual_age_less_than_150(gedcom.INDIs)
    # US08
    US0408sourabh.US08bbmp()
    # US10
    US10and22Sourabh.US10Ma14()
    # US12
    US12and36Sourabh.US12()
    # US16
    util_khalid.check_family_male_last_names(gedcom.FAMs, gedcom.INDIs)
    # US21
    util_khalid.check_gender_role(gedcom.FAMs, gedcom.INDIs)
    # US22
    US10and22Sourabh.US22UniqueIDs()
    # US26
    util_khalid.check_corresponding_entries(gedcom.FAMs, gedcom.INDIs)
    # US36
    US12and36Sourabh.US36()
