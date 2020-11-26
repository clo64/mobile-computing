##
#  Charles Owen
#  Python script for scraping PIP sensor data that has been
#  saved usig the cat command.
#  To direct the PIP data into a .txt file, from the 
#  linux CLI use the command:
#
#  sudo stdbuf -o0 ./pip_sense.v2 l l | stdbuf -o0 grep TX:0$1 | cat > sensor_data.txt
# #

import time

class FileScraper():

    def __init__(self, file_Name):
        self.file_Name = file_Name

    def extract_lines(self):
        with open(self.file_Name, 'r') as f:
            self.content = f.readlines()[-1]
        return self.content

    def print_all_data_lines(self):
        if self.content:
            for line in self.content:
                print(line)

    def print_last_line(self):
        print(self.content)

#test code for scraper class
if __name__ == "__main__":
    
    file_Name = input("Please enter the file name: ")
    scraper = FileScraper(file_Name)
    while True:
        scraper.extract_lines()
        scraper.print_last_line()
        time.sleep(2)