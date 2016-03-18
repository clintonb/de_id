""" Converts a TSV to SQLite table.

Examples:
    $ python tsv2sqlite.py input.tsv output.db table_name
"""
from __future__ import unicode_literals

import csv
import sqlite3
import sys

import pandas


def convert_tsv_to_sqlite(tsv_file_path, db_path, table_name):
    data_frame = pandas.read_csv(
        tsv_file_path,
        header=0,
        quoting=csv.QUOTE_NONE,
        encoding='utf-8',
        delimiter='\t'
    )

    with sqlite3.connect(db_path) as conn:
        data_frame.to_sql(table_name, conn, if_exists='replace', index=False)

        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM {table_name}'.format(table_name=table_name))
        print('Loaded [{count}] rows into table [{table_name}].'.format(count=cursor.fetchone()[0], table_name=table_name))


if __name__ == '__main__':
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    table_name = sys.argv[3]

    convert_tsv_to_sqlite(input_file_name, output_file_name, table_name)
