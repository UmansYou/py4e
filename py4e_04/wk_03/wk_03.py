
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Artist;

    CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER
    );

    CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

    CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER
    );

    CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    )
    ''')

fh = open ('Library.xml')
file = ET.parse(fh)
file = file.findall("dict/dict/dict")

# define a lookup funtion that look for the value using the key and return the value
def lookup(d, key): # ‘d’用来放dictionary,key用来放tag
    found = False
    for child in d:
    # 'child' iterate through each key-value pair
    #if the tag is 'key'，if the value is the child，change 'found' to true
    #because the value in the next key-value pair is what we are looking for
    #now the 'found' is true, line50 will return the value in the pair and break out of the loop
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

for item in file:
    #use lookup function defined previously to return the 'value' of the keys
    track = lookup(item, 'Name')
    genre = lookup(item, 'Genre')
    album = lookup(item, 'Album')
    artist = lookup(item, 'Artist')

    #if any of these is missing, skip it
    if track is None or genre is None or album is None or artist is None:
        continue

    cur.execute('''INSERT OR IGNORE INTO Genre(name)
    VALUES(?)''',(genre,)) #insert the genre name to the genre table, skip if it already exist
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre,))
    genre_id = cur.fetchone()[0] #get the genre_id for that genre

    cur.execute('''INSERT OR IGNORE INTO Artist(name)
    VALUES(?)''',(artist,)) #insert the artist name into artist table, skip if it already exist
    cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist,))
    artist_id = cur.fetchone()[0] #get the artist_id

    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id)
    VALUES (?,?)''', (album,artist_id))#insert the album name and the artist_od into artist table, skip if it already exist
    cur.execute('''SELECT id FROM Album WHERE title = ?''', (album,))
    album_id = cur.fetchone()[0] #get the album_id

    cur.execute('''INSERT OR IGNORE INTO Track(title, album_id, genre_id)
    VALUES (?,?,?)''',(track,album_id,genre_id)) #insert into track table

conn.commit()
