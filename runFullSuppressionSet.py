#!/usr/bin/env python
'''
This runs the program to build the full set of records to suppress once the binning and suppression based on
identification based on the classes for which a user enrolled.
'''
import buildFullSuppressionSet
from de_id_functions import dbOpen

bin_size = ['05', '10', '15', '20', '25']
k_values = [3, 4, 5, 6]

cr = dbOpen('year.db')
geo_suppress = 'countryDict'
for k_val in k_values:
    for s in bin_size:
        class_supp = 'classSuppressSet' + str(k_val) + 'P'
        yob_fname = 'yobbin' + s + 'k'
        forum_fname = 'postbin' + s + 'k'
        suppress_out = 'fullSuppress'+ s + s + str(k_val) + 'P'
        buildFullSuppressionSet.main(cr, class_supp, geo_suppress, yob_fname, forum_fname, suppress_out, k_val)