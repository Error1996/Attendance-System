__author__ = 'ERROR'

import sqlite3

con = sqlite3.connect('Data\Database\Teachers.db', check_same_thread=False)
curs = con.cursor()

curs.execute(('CREATE TABLE IF NOT EXISTS teacher\n'
              '                        (\n'
              '                        t_name text,\n'
              '                        depart text,\n'
              '                        t_pass text\n'
              '                        )'
              ))

curs.execute(('CREATE TABLE IF NOT EXISTS lectures\n'
              '                        (\n'
              '                        t_name text,\n'
              '                        clas text\n'
              '                        )'
              ))


def log():
    curs.execute(('SELECT t_name, t_pass\n'
                  'FROM teacher'
                  ))
    return curs.fetchall()


def lec():
    curs.execute(('SELECT *\n'
                  'FROM lectures'
                  ))
    return curs.fetchall()


def account(name, dep, pas):
    curs.execute(('INSERT INTO teachers (t_name, depart, t_pass)\n'
                  'VALUES (?,?,?)'
                  ), [name, dep, pas])
    con.commit()


def allote_class(name, clas):
    curs.execute(('INSERT INTO lectures (t_name, clas)\n'
                  'VALUES (?,?)'
                  ), [name, clas])
    con.commit()