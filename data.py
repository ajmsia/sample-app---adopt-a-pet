import sqlite3

db_path = 'ar.db'

def connect_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# Read attendance by course
def readatbycourse(course):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM attendance WHERE course=?'
    results = cur.execute(query, (course,)).fetchall()
    conn.close()
    return results

# Read course by date
def readatbydate(course, date):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM attendance WHERE date=?'
    results = cur.execute(query, (date,)).fetchall()
    conn.close()
    return results
