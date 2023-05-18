#This program will read value from a SQLITE3 db and save it in CSV and PDF Files
import pandas as pd
import csv
import pdfkit
import sqlite3
from fpdf import FPDF


db = r"C:\Users\Sayani\Desktop\WorkSpace\2023-24\Python\ATPLC_Internship\May\atplc.db"

#function to fetch data from database

def collect_data(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print("Connected to DataBase")

    #Selecting all data from database
    query = """select * from Google_sheet"""
    cursor.execute(query)
    global records
    records = cursor.fetchall()

    return records

#fuction to write data into CSV file

def write_csv(records):
    print("CSV Process")
    file_name = input("Enter the desired CSV File Name = ")
    file_name = file_name+".csv"
    df = pd.DataFrame(records)
    df.to_csv(file_name)
    print("CSV File Generated!")


#function to write data into PDF file

def write_pdf(records):
    print("PDF Process")
    config = pdfkit.configuration(wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe") 
    file_name = input("Enter the desired PDF File Name = ")
    file_name = file_name+".pdf"
    df = pd.DataFrame(records)
    html_string = df.to_html()
    pdfkit.from_string(html_string, file_name, configuration = config)
    print("PDF file generated!")    


def main():
    collect_data(db)
    write_csv(records)
    write_pdf(records)


main()