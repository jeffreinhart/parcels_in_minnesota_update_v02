#-------------------------------------------------------------------------------
# Name:        edit_export_date_update.py
# Purpose:     Quick and dirty update for edit_date and export_date fields.
#
# Author:      Jeff Reinhart
#
# Created:     2016-12-14
# Updated:     2016-12-14
#-------------------------------------------------------------------------------

def main():
    import arcpy, os
    from parcels_base_classes import userObject

    wkspGdb = userObject().wkspGdb

    parcels = os.path.join(wkspGdb, "parcels_in_minnesota")

    print "Running for: {0}".format(parcels)

    counExpDateList = [
        ['aitk', '001', '2016-10-05'],
        ['anok', '003', '2015-12-31'],
        ['beck', '005', '2014-12-09'],
        ['belt', '007', '2014-12-09'],
        ['bent', '009', '2016-07-19'],
        ['bigs', '011', '2016-06-07'],
        ['blue', '013', '2016-08-09'],
        ['brow', '015', '2016-07-05'],
        ['carl', '017', '2015-01-16'],
        ['carv', '019', '2015-12-31'],
        ['cass', '021', '2014-12-09'],
        ['chip', '023', '2016-07-12'],
        ['chis', '025', '2014-10-24'],
        ['clay', '027', '2016-07-11'],
        ['clea', '029', '2016-07-18'],
        ['cook', '031', '2015-01-13'],
        ['cott', '033', '2016-09-01'],
        ['crow', '035', '2014-12-09'],
        ['dako', '037', '2015-12-31'],
        ['dodg', '039', '2016-06-14'],
        ['doug', '041', '2016-07-29'],
        ['fari', '043', '2016-08-08'],
        ['fill', '045', '2015-03-04'],
        ['free', '047', '2015-03-11'],
        ['good', '049', '2016-04-26'],
        ['gran', '051', '2016-08-19'],
        ['henn', '053', '2015-12-31'],
        ['hous', '055', '2015-05-12'],
        ['hubb', '057', '2016-07-12'],
        ['isan', '059', '2016-08-22'],
        ['itas', '061', '2014-12-09'],
        ['jack', '063', '2016-07-15'],
        ['kana', '065', '2016-02-23'],
        ['kand', '067', '2016-07-29'],
        ['kitt', '069', '2016-10-13'],
        ['kooc', '071', '2016-05-18'],
        ['lacq', '073', '2016-07-12'],
        ['lake', '075', '2015-01-07'],
        ['lesu', '079', '2016-09-13'],
        ['linc', '081', '2016-07-06'],
        ['lotw', '077', '2016-07-19'],
        ['lyon', '083', '2016-07-05'],
        ['mahn', '087', ''],
        ['mars', '089', '2016-07-21'],
        ['mart', '091', '2016-07-27'],
        ['mcle', '085', '2016-11-17'],
        ['meek', '093', '2016-07-29'],
        ['mill', '095', '2016-03-30'],
        ['morr', '097', '2016-07-19'],
        ['mowe', '099', '2015-01-16'],
        ['murr', '101', '2016-07-12'],
        ['nico', '103', '2016-07-11'],
        ['nobl', '105', '2016-07-27'],
        ['norm', '107', '2016-07-26'],
        ['olms', '109', '2015-04-08'],
        ['otte', '111', '2016-09-14'],
        ['penn', '113', '2016-07-25'],
        ['pine', '115', '2015-10-19'],
        ['pipe', '117', '2016-07-11'],
        ['polk', '119', '2016-07-11'],
        ['pope', '121', '2016-08-05'],
        ['rams', '123', '2015-12-31'],
        ['redl', '125', '2016-08-12'],
        ['redw', '127', '2016-08-08'],
        ['renv', '129', '2016-07-08'],
        ['rice', '131', '2014-11-21'],
        ['rock', '133', '2016-07-27'],
        ['rose', '135', '2016-09-23'],
        ['scot', '139', '2015-12-31'],
        ['sher', '141', '2016-07-29'],
        ['sibl', '143', '2016-07-08'],
        ['stea', '145', '2016-08-05'],
        ['stee', '147', '2007-09-17'],
        ['stev', '149', '2016-08-05'],
        ['stlo', '137', '2016-06-14'],
        ['swif', '151', '2016-08-19'],
        ['todd', '153', '2016-07-29'],
        ['trav', '155', '2016-09-22'],
        ['waba', '157', '2016-03-22'],
        ['wade', '159', '2016-08-05'],
        ['wase', '161', '2016-10-10'],
        ['wash', '163', '2015-12-31'],
        ['wato', '165', ''],
        ['wilk', '167', '2016-07-29'],
        ['wino', '169', '2015-09-10'],
        ['wrig', '171', '2016-08-05'],
        ['yell', '173', '2016-05-09']
    ]

    for coun in counExpDateList:
        if coun[2] != '':
            formattedDate = "{0}/{1}/{2}".format(coun[2][5:7], coun[2][8:10], coun[2][0:4])

            where = "COUNTY_ID = '{0}'".format(coun[1])

            print "Updating {0} with date {1}, selecting with {2}...".format(coun[0], coun[2], where)

            fieldList = ["EDIT_DATE", "EXPORT_DATE"]

            with arcpy.da.UpdateCursor(parcels, fieldList, where) as ucur:
                for urow in ucur:
                    urow[0] = formattedDate
                    urow[1] = formattedDate
                    ucur.updateRow(urow)

if __name__ == '__main__':
    main()
