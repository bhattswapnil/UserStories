import requests
import sqlite3

def create_db():
    conn = sqlite3.connect('TestDB.db')  
    c = conn.cursor() 
    c.execute('''CREATE TABLE IF NOT EXISTS Stories ([StoryId] INTEGER PRIMARY KEY, [name] text,[description] text, [duration] INTEGER, [type] text, [latitude] text , [longitude] text , [timestamp] TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn;
    
def main():

    conn = create_db();  


if __name__ == '__main__':
    main()
