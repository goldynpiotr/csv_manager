import pandas as pd
import os

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

    def read_sheet(self):
        try:
            df = pd.read_csv(self.filename, delimiter=';', encoding= 'unicode_escape')
            return df
        except FileNotFoundError:
            print("File not found.")

    def sort_data(self,data):
        checker = True
        while checker:
            try:
                column = input("Specify column to sort by: ")
                if column in data.columns:
                    res1 = input("Ascending or descending (A/D)")
                    if res1 == "A":
                        sorted_data = data.sort_values(by=column)
                        checker = False
                    elif res1=="D":
                        sorted_data = data.sort_values(by=column, ascending= False)
                        checker = False
                    else:
                        print("Wrong value. Choose again")
                else:
                    print("There is no such column. Try again")
            except Exception as e:   
                print("Error, ", e)
        return sorted_data
    
    def remove_na(self,data):
        try:
            cleaned_data = data.dropna()
            print("Cleaning completed")
            return cleaned_data
        except Exception as e:
            print("Error", e)

    def remove_duplicates(self,data):
        try:
            cleaned_data = data.drop_duplicates()
            print("Removing duplicates completed")
            return cleaned_data
        except Exception as e:
            print("Error", e)
    
    def write_data(self, data):
        checker2 = True
        while checker2:
            try:
                where_to_write=input("Where to write new file (full path and name): ")
                data.to_csv(where_to_write, encoding='utf-8', sep=';', index=False)
                print("Data written succesfully") 
                checker2=False
            except Exception as e:
                print("Error", e)

def main():
    checker = True
    path = get_filepath()
    manago = CSVFileManager(path)
    new_data = manago.read_sheet()
    print(manago.read_sheet())
    while checker:
        
        print("****************")
        print("1. Sort file")
        print("2. Remove n/a values")
        print("3. Remove duplicates")
        print("4. Save&Quit")
        print("5. Quit")
        menu_response = input("Choose number 1-4: ")
        if menu_response=="1":
            new_data = manago.sort_data(new_data)
            print(new_data)
        elif menu_response=="2":
            new_data = manago.remove_na(new_data)
            print(new_data)
        elif menu_response =="3":
            new_data = manago.remove_duplicates(new_data)
            print(new_data)
        elif menu_response == "4":
            saved_file = manago.write_data(new_data)
            checker = False
        elif menu_response=="5":
            print("quitting")
            checker=False

if __name__ == "__main__":
    main()
