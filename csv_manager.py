import pandas as pd
import os
from csv import Sniffer

def get_filepath():
    while True:
        res = input("Full path to file: ")
        if os.path.exists(res):
            return res
        else:
            print("File not found. Please provide a valid file path.")

class CSVFileManager:
    def __init__(self, filename):
        self.filename = filename
        self.df = None
        self.delimiter = None

    def read_sheet(self):
        try:
            with open(self.filename, 'r', newline='') as file:
                sample = file.read(4096)
                dialect = Sniffer().sniff(sample)
                self.delimiter = dialect.delimiter
    
            self.df = pd.read_csv(self.filename, delimiter=self.delimiter, encoding= 'unicode_escape')
            return self.df
        except FileNotFoundError:
            print("File not found.")
            
    def sort_data(self):
        checker = True
        while checker:
            try:
                column = input("Specify column to sort by: ")
                if column in self.df.columns:
                    res1 = input("Ascending or descending (A/D)")
                    if res1 == "A":
                        self.df = self.df.sort_values(by=column)
                        checker = False
                    elif res1=="D":
                        self.df = self.df.sort_values(by=column, ascending= False)
                        checker = False
                    else:
                        print("Wrong value. Choose again")
                else:
                    print("There is no such column. Try again")
            except Exception as e:   
                print("Error, ", e)
        return self.df
    
    def remove_na(self):
        try:
            self.df = self.df.dropna()
            print("Cleaning completed")
            return self.df
        except Exception as e:
            print("Error", e)

    def remove_duplicates(self):
        try:
            self.df = self.df.drop_duplicates()
            print("Removing duplicates completed")
            return self.df
        except Exception as e:
            print("Error", e)
    
    def write_data(self):
        checker2 = True
        while checker2:
            try:
                where_to_write=input("Where to write new file (full path and name): ")
                self.df.to_csv(where_to_write, encoding='utf-8', sep=self.delimiter, index=False)
                print("Data written succesfully") 
                checker2=False
            except Exception as e:
                print("Error", e)

def main():
    checker = True
    path = get_filepath()
    file1 = CSVFileManager(path)
    new_data = file1.read_sheet()
    print(file1.read_sheet())
    while checker:
        
        print("****************")
        print("1. Sort file")
        print("2. Remove n/a values")
        print("3. Remove duplicates")
        print("4. Save&Quit")
        print("5. Quit")
        menu_response = input("Choose number 1-5: ")
        if menu_response=="1":
            new_data = file1.sort_data()
            print(new_data)
        elif menu_response=="2":
            new_data = file1.remove_na()
            print(new_data)
        elif menu_response =="3":
            new_data = file1.remove_duplicates()
            print(new_data)
        elif menu_response == "4":
            saved_file = file1.write_data()
            checker = False
        elif menu_response=="5":
            print("quitting")
            checker=False

if __name__ == "__main__":
    main()
