#Publish the excel file via File-Share-Publish To Web-Embed as CSV
#import pandas module and read the entire data in excel variable


import pandas as pd
import sqlite3

path_excel = input("Please enter the Link of Google Sheet: ")
excel = pd.read_csv(path_excel)

def read_db(excel):
    try:
        sqliteConnection = sqlite3.connect('atplc.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        df =pd.DataFrame(excel)
        
        df.to_sql('Google_sheet', sqliteConnection)
        sqliteConnection.close()



    except sqlite3.error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")



read_db(excel)