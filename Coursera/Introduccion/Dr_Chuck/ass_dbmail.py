import sqlite3
import urllib
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Orgs''')

cur.execute('''
CREATE TABLE Orgs (org TEXT, count INTEGER)''')

url = 'http://www.pythonlearn.com/code/mbox.txt'
uh = urllib.urlopen(url)

# fname = raw_input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
# fh = open(fname)
for line in uh:
    if not line.startswith('From: ') : continue
    # pieces = line.split()
    # parts = pieces[1].split("@")
    # email = parts[1]
    emails = re.findall('@(\S*)', line)
    email = emails[0]
    cur.execute('SELECT count FROM Orgs WHERE org = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Orgs (org, count) 
                VALUES ( ?, 1 )''', ( email, ) )
    else : 
        cur.execute('UPDATE Orgs SET count=count+1 WHERE org = ?', 
            (email, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Orgs ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()