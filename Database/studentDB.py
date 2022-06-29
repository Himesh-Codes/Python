#!/usr/bin/env python3
"""
Student Database API 
"""

from connectDB import ConnectDB

def main():
    tablename = 'students'
    studentDB = ConnectDB(filename=':memory:', table=tablename) #in memory usage using :memory:
    studentDB.sql_do('DROP TABLE IF EXISTS {}'.format(tablename))
    studentDB.sql_do(f""" 
                      CREATE TABLE {tablename} 
                      (id INTEGER PRIMARY KEY, studentID TEXT, name TEXT)
                      """)
    studentRecords = [dict(studentID='12S', name='Tony'), dict(studentID='14S', name='Riya')]
    for record in studentRecords:
        studentDB.sql_insert(record)
    
    allData = studentDB.sql_selectall()
    for data in allData:
        print(dict(data))
        
if __name__ == '__main__': main()