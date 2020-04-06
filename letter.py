from jdatetime import datetime
import sqlite3
import jdatetime

conn=sqlite3.connect('letters_database')
curser=conn.cursor()

    
curser.execute('''CREATE TABLE IF NOT EXISTS main (
    id integer PRIMARY KEY,
    name TEXT NOT NULL ,
    letter_date TEXT  ,
    moment TEXT  ,
    deadline TEXT,
    receiver TEXT,
    description TEXT  
    
 
)''')

def record_in_database(name,letter_date,deadline,receiver,description):

   
    moment=jdatetime.date.today()

    
    timeout=(moment+jdatetime.timedelta(days=deadline)).strftime('%Y/%m/%d')
    moment=moment.strftime('%Y/%m/%d')
    data_tupel=(name,letter_date,moment,timeout,receiver,description)
 
   
    curser.execute('INSERT INTO main (name,letter_date,moment,deadline,receiver,description)  VALUES (?,?,?,?,?,?)' ,data_tupel)
    conn.commit()
               


def read_from_datebase():
    letters_list=[]
    curser.execute('SELECT * FROM main')
    rows=curser.fetchall()
    for row in rows:
        #print (row)
        row=list(row)
        letters_list.append(row[1:])
 
    return letters_list

def delete_from_database(name):
    curser.execute('DELETE  FROM 'main' WHERE name = name; ')
    



def letter_trace(name):
    
    history_list=[]
    curser.execute('SELECT receiver,moment FROM main where name=\'%s\' order by id asc' %name)
    rows=curser.fetchall()
    for row in rows:
        print (row)
        s='-------->'.join(map(str,row))
        history_list.append(s)
    return history_list



def archived():
    archive_list=[]
        
    curser.execute('SELECT name FROM main where  receiver=\'بایگانی\' ' )
    rows=curser.fetchall()
    for row in rows:
        archive_list.append(row[0])  
    archive_list=list(dict.fromkeys(archive_list))  
    return archive_list

def un_archived():
    not_archive = []
    letters_list=letters()
    archive_list=archived()
    for x in letters_list:
        if x not in archive_list:
            not_archive.append(x)
    return not_archive


def print_Unarchive(UnArchiveList):
    notArchive_print_list=[]
    for name in UnArchiveList:

        curser.execute('SELECT name,receiver,moment FROM main where name=%s order by id desc limit 1' %name)
        row=curser.fetchone()
        print((row))
        s='-------->'.join(map(str,row))
        notArchive_print_list.append(s)

    return notArchive_print_list  
        
