from jdatetime import datetime
import sqlite3
import jdatetime

conn=sqlite3.connect('letters_database')
curser=conn.cursor()
curser.execute('''CREATE TABLE IF NOT EXISTS main (
    id integer PRIMARY KEY,
    name TEXT NOT NULL ,
    receiver TEXT NOT NULL,
    moment TEXT NOT NULL,
    archive BLOB DEFAULT False
 
)''')
def get_data(name,receiver):

    moment=datetime.now().strftime('%Y-%m-%d    %H:%M')
    if receiver == 'بایگانی':
        curser.execute('INSERT INTO main (name,receiver,moment,archive)  VALUES (?,?,?,?)'    ,(name,receiver,moment,True)    )
        conn.commit()
        
    else :
        curser.execute('INSERT INTO main (name,receiver,moment)  VALUES (?,?,?)'  ,(name,receiver,moment)   )
        conn.commit()    
        


def letters():
    letters_list=[]
    curser.execute('SELECT * FROM main')
    rows=curser.fetchall()
    for row in rows:
        #print (row)
        letters_list.append(row[1])
    
    letters_list=list(dict.fromkeys(letters_list))   
    return letters_list


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
    not_archive=[]
    for name in UnArchiveList:
        

        curser.execute('SELECT name,receiver,moment FROM main where name=%s order by id desc limit 1' %name)
        row=curser.fetchone()
        s='-------->'.join(map(str,row))
        not_archive.append(s)
        
      
        
    # print(not_archive) 
    return not_archive       
        
