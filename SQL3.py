import csv
import sqlite3
    

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('DROP TABLE origins')
    cursor.execute('''CREATE TABLE origins (
        title_id TEXT, 
        region TEXT,
        language TEXT,
        FOREIGN KEY(title_id) REFERENCES titles(idnum)
        )''')
    conn.commit()
    with open('title.akas.tsv', 'r') as file:
        reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
        for origins in reader:
            cursor.execute('''INSERT INTO origins
            (title_id, region, language) 
            VALUES (?, ?, ?)''', 
            (origins['titleId'],
            (origins['region']),
            (origins['language'])))
        conn.commit()