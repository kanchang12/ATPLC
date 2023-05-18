#The Original path
#https://docs.google.com/spreadsheets/d/e/2PACX-1vQVUVI4ykXqPgA5l4mU94H6UhNxbA5nrhn-5KV5Cqn6eEL34dXKilGmeysI-r0T-YVQehWmZMID0Ewo/pub?output=csv


import sqlite3
import pandas as pd


sqliteConnection = sqlite3.connect('atplc.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")

# Publish the excel file via File-Share-Publish To Web-Embed as CSV
path_excel = input("Please enter the Link of Google Sheet: ")

excel = pd.read_csv(path_excel)

def table_present(table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    exists = cursor.fetchone() is not None
    return exists


table_name = 'google'

if table_present(table_name):
    # Table exists, perform your operations here
    print(f"The table '{table_name}' exists.")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    df =pd.DataFrame(excel)
    df.to_sql('google', sqliteConnection)
    sqliteConnection.close()
    print(f"The table '{table_name}' Updated.")
else:
    # Table doesn't exist, handle the case here
    print(f"The table '{table_name}' does not exist.")
    df =pd.DataFrame(excel)
        
    df.to_sql('google', sqliteConnection)
    sqliteConnection.close()
    print(f"The table '{table_name}' created.")