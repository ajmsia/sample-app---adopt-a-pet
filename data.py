import sqlite3

db_path = 'ar.db'

def connect_db(path):
    conn = sqlite3.connect(path)
    # Convert tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# Read attendance by subject
def readatbysub(Subject):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM attendance WHERE Subject=?'
    results = cur.execute(query, (Subject,)).fetchall()
    conn.close()
    return results

def readatbydate(Date):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM attendance WHERE Date=?'
    results = cur.execute(query, (Date,)).fetchall()
    conn.close()
    return results