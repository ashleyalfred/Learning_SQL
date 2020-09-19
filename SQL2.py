import csv
import sqlite3
    

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE ratings (
        title_id TEXT, 
        avg_rating REAL, 
        votes INTEGER,
        FOREIGN KEY(title_id) REFERENCES titles(idnum)
        )''')
    conn.commit()
    with open('title.ratings.tsv', 'r') as file:
        reader = csv.DictReader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
        # iterate over the ratings
        for ratings in reader:
            # create row and insert title data 
            cursor.execute('''INSERT INTO ratings 
            (title_id, avg_rating, votes) 
            VALUES (?, ?, ?)''', 
            (ratings['tconst'],
            float(ratings['averageRating']),
            int(ratings['numVotes'])))
        conn.commit()