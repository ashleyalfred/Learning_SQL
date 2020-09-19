import csv
import sqlite3

    

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('DROP TABLE titles')
    # cursor.execute('DROP TABLE genres')
    cursor.execute('''CREATE TABLE titles (
        idnum TEXT, 
        Type TEXT, 
        Title TEXT, 
        originalTitle TEXT, 
        isAdult INTEGER, 
        startYear INTEGER, 
        endYear INTEGER, 
        runtimeMinutes INTEGER,
        PRIMARY KEY (idnum)
        )''')
    cursor.execute(''' CREATE TABLE genres (
        title_id TEXT,
        genre TEXT,
        PRIMARY KEY (title_id, genre),
        FOREIGN KEY(title_id) REFERENCES titles(idnum)
        )''')
    conn.commit()

    with open('title.basics.tsv', 'r') as file:
        reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
        # iterate over the titles 
        for title in reader:
            # print(title)
            # create row and insert title data 
            cursor.execute('''INSERT INTO titles 
            (idnum, Type, Title, originalTitle, isAdult, startYear, endYear, runtimeMinutes) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
            (title['tconst'],
            title['titleType'],
            title['primaryTitle'],
            title['originalTitle'],
            int(title['isAdult']),
            int(title['startYear'] if title['startYear'] != '\\N' else 0),
            int(title['endYear'] if title['endYear'] != '\\N' else 0),
            int(title['runtimeMinutes'] if title['runtimeMinutes'] != '\\N' else 0)))
            # split genres then iterate over them
            for genre in title['genres'].split(','):
                # create row and insert genre data 
                cursor.execute('INSERT INTO genres (title_id, genre) VALUES (?, ?)', (title['tconst'], genre))
        conn.commit()
