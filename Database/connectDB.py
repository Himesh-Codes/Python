#!/usr/bin/env python3
"""
DB connect API
"""

import sqlite3


class ConnectDB():
    def __init__(self, **kwargs):
        # @property decorators
        self._filename = kwargs.get('filename')       
        self._table = kwargs.get('table', '') 
    
    # set table name
    def set_table(self, tablename):
        self._table = tablename;
        
    def sql_do(self, sql, params=()):
        self.sql_donot_commit(sql, params)
        self.__dbConnection.commit()
        
    def sql_donot_commit(self, sql, params=()):
        self.__dbConnection.execute(sql, params)
        
    def sql_query(self, sql, params=()):
        data = self.__dbConnection.execute(sql, params)
        for row in data:
            yield row
    
    def sql_query_row(self, sql, params=()):
        data = self.__dbConnection.execute(sql, params)
        return data.fetchone()[0]
    
    def sql_insert(self, record: dict):
        lastRowId = self.sql_insert_nocommit(record)
        self.__dbConnection.commit()
        return lastRowId
    
    def sql_insert_nocommit(self, record: dict):
        keysList = sorted(record.keys())
        values = [record[key] for key in keysList]
        query = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table, ', '.join(keysList), ', '.join('?' * len(values)))
        dbpoint = self.__dbConnection.execute(query, values)
        return dbpoint.lastrowid;
    
    def sql_update_nocommit(self, recid, record: dict):
        keyslist = sorted(record.keys())
        values = [record[key]  for key in keyslist]
        for index, key in enumerate(keyslist):
            if key == 'id':
               del keyslist[index] 
               del values[index]
        
        # lambda function is an anonymous function produces computed value
        query = 'UPDATE {} SET {} WHERE id = ?'.format(self._table, ', '.join(map(lambda key: '{} = ?'.format(key), keyslist)))
        self.__dbConnection.execute(query, values.append(recid))

    def sql_selectall(self):
        query = f'SELECT * FROM {self._table}'
        data = self.__dbConnection.execute(query)
        return data     
        
    # filename getter
    @property
    def _filename(self):
        return self._dbfilename
    
    # filename setter
    @_filename.setter
    def _filename(self, name):
        self._dbfilename = name
        self.__dbConnection = sqlite3.connect(name) 
        self.__dbConnection.row_factory = sqlite3.Row
    
    # filename deleter
    @_filename.deleter
    def _filename(self):
        self.closeDB()
    
    def closeDB(self):
        self.__dbConnection.close()
        del self._dbfilename
        
    def getDBConnection(self):
        return self.__dbConnection
        
    def commitDB(self):
       self.__dbConnection.commit()
        