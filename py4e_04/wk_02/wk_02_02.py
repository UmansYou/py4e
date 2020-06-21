import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

#Create a table in sql for email and counts (this is just like a dictionary)
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From '):
        continue
    email = line.split()[1]
    org = email[int(email.find('@'))+1:] #find() get the location of @, +1 make sure that @ is not included

    #get the row ready and retrieve the count from the row for that org
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))

    # get the count of the org
    number = cur.fetchone()

    #if the count of the org does not exist, use INSERT INTO to create the row
    if number is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)', (org,))

    #if the count of the org already exists, update the count with (count = count + 1)
    else:
        cur.execute('''UPDATE Counts SET count = count + 1
                    WHERE org = ?''', (org,))

conn.commit()

# get the table and print row by row
for row in cur.execute('SELECT * FROM Counts ORDER BY count DESC'):
    print(str(row[0]),row[1])
