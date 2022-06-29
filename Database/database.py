#!/usr/bin/env python3
"""
Database API 
"""

import sqlite3


def main():
    # db hanlder object, create a db file specified in connection
    dbHandle = sqlite3.connect('sqldb.db')
    dbConnect = dbHandle.cursor()
    dbConnect.execute('DROP TABLE IF EXISTS MyDB')
    dbConnect.execute(""" 
                      CREATE TABLE MyDB 
                      (id INTEGER PRIMARY KEY, textDescription TEXT)
                      """)
    dbConnect.execute("""
                        INSERT INTO MyDB (textDescription) VALUES ('Initial Checkin Data')
                      """)
    dbHandle.commit()
    dbConnect.execute('SELECT COUNT(*) FROM MyDB')
    count = dbConnect.fetchone()[0]
    print(count)
    allData = dbConnect.execute('SELECT * FROM MyDB')
    for row in allData:
        print(row)
    dbConnect.close()
        
if __name__ == '__main__': main()