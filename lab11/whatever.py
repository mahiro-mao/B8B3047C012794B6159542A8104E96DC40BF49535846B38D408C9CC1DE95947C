import sqlite3

# SQL setup
con = sqlite3.connect('scores.db') 
cursor = con.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    pID INTEGER PRIMARY KEY AUTOINCREMENT,
    fName TEXT,
    sName TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    task_num INTEGER,
    points INTEGER,
    pID INTEGER,
    FOREIGN KEY(pID) REFERENCES people(pID)
)''')

# Dictionary för att lagra unika kombinationer
person_dict = {}

try:
    with open('score2.txt', 'r') as file:
        for line in file:
            parts = line.strip().split()
            task_number = int(parts[1])
            fName = parts[2]
            sName = parts[3]
            points = int(parts[4])

            # Checka om hen finns
            if (fName, sName) not in person_dict:
                cursor.execute('''
                INSERT INTO people (fName, sName) VALUES (?, ?)
                ''', (fName, sName))
                pID = cursor.lastrowid
                person_dict[(fName, sName)] = pID
            else:
                pID = person_dict[(fName, sName)]

            # Insert score record
            cursor.execute('''
            INSERT INTO scores (task_num, points, pID) VALUES (?, ?, ?)
            ''', (task_number, points, pID))

    con.commit()

    # Top 10 people here at watchMojo
    cursor.execute('''
    SELECT p.fName, p.sName, SUM(s.points) AS total_points
    FROM scores s
    JOIN people p ON s.pID = p.pID
    GROUP BY s.pID
    ORDER BY total_points DESC
    LIMIT 10
    ''')

    print("Top 10:")
    for row in cursor.fetchall():
        print(f"{row[0]} {row[1]}: {row[2]} points")

    # Top 10 hardest tasks here at watchMojo
    cursor.execute('''
    SELECT s.task_num, SUM(s.points) AS total_task_points
    FROM scores s
    GROUP BY s.task_num
    ORDER BY total_task_points ASC
    LIMIT 10
    ''')

    print("\nTop 10 hardest upg.:")
    for row in cursor.fetchall():
        print(f"Task {row[0]}: {row[1]} points")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Delete data and close connection
    cursor.execute('DELETE FROM scores')
    cursor.execute('DELETE FROM people')
    con.commit()  # Commit the deletions
    con.close()
