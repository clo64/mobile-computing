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

    def extract_line(self):
        with open(self.file_Name, 'r') as f:
            self.content = f.readlines()[-1]
        return self.content

    def print_all_data_lines(self):
        if self.content:
            for line in self.content:
                print(line)

    def print_last_line(self):
        print(self.content)

    def extract_sensor_data(self):
        '''This is just a demonstration that we can
           extract the individual data points. We actually 
           need to DO something with them now.'''
        raw_data = self.extract_line()
        token_container = raw_data.split()
        #temperature
        print('Temperature: ', token_container[17])
        #humidity
        print('Humidity: ', token_container[19])
        #light
        print('Light: ', token_container[15])


#test code for scraper class
if __name__ == "__main__":
    
    file_Name = input("Please enter the file name: ")
    scraper = FileScraper(file_Name)
    while True:
        scraper.extract_line()
        scraper.print_last_line()
        scraper.extract_sensor_data()
        time.sleep(2)