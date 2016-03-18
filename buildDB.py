#!/usr/bin/env python

'''
Builds the basic database for de-identification. While building the database, this program
will replace the current student name and id with a randomly generated id (which is the same
for the student for all his or her records) and will also create the country/continent table.
The dates will also be altered to contain just the date (not the time), and a copy of the
table will be made as a separate table so that changes can be compared with the original.

The database will be saved, and can be copied and re-used for multiple runs of the rest of
the code.
'''
import random
import sqlite3
import sys

from utils.tsv2sqlite import convert_tsv_to_sqlite


def split_date(date):
    """ Remove the date from the time in the time signature while creating the main table. """
    if ' ' in date:
        point = date.index(' ')
        date = date[:point]
    return date


def idGen2(varName, prefix, lDict):
    if varName in lDict:
        return (lDict[varName])
    nId = prefix + str(random.randint(0, 10000000000))
    while nId in lDict:
        nId = prefix + str(random.randint(0, 10000000000))
    lDict[varName] = nId
    lDict[nId] = varName
    return nId


def filter_data(cursor, table_name):
    """
    Filters the data, removing unnecessary rows.

    Removes rows meeting the following criteria:
        - Person is course staff or instructor

    Arguments:
        cursor (sqlite3.Cursor) -- SQLite3 database cursor
        table_name (str) -- Name of the table where the data is stored

    Returns:
        None
    """
    # Remove staff and instructor users
    cursor.execute("DELETE FROM {table_name} WHERE roles IN ('instructor', 'staff')".format(table_name=table_name))
    print('Deleted [{count}] instructor/staff rows from table [{table_name}].'.format(
        count=cursor.rowcount,
        table_name=table_name)
    )

    # TODO Add support for filtering out students who did not explore the course content
    # TODO Add support for filtering out students who did not complete the course


def clean_dates(cursor, table_name):
    """
    Converts the date-time strings to date strings.

    Arguments:
        cursor (sqlite3.Cursor) -- SQLite3 database cursor
        table_name (str) -- Name of the table where the data is stored

    Returns:
        None
    """
    pass


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: python buildDB csvFileName databaseName countryTableFileName'
        sys.exit(1)

    input_file_name = sys.argv[1]
    db_file_name = sys.argv[2]
    table_name = 'source'

    with sqlite3.connect(db_file_name) as conn:
        cursor = conn.cursor()
        convert_tsv_to_sqlite(input_file_name, db_file_name, table_name)
        filter_data(cursor, table_name)
