##
#  Python script for scraping PIP sensor data that has been
#  saved usig the cat command.
#  To direct the PIP data into a .txt file, from the 
#  linux CLI use the command:
#
#  sudo stdbuf -o0 ./pip_sense.v2 l l | stdbuf -o0 grep TX:0$1 | cat > sensor_data.txt
# #

class FileScraper():

    def __init__(self, file_Name):
        self.file_Name = file_Name

    def extract_all_data(self):
        with open(self.file_Name, 'r') as f:
            content = f.readlines()
        return content

if __name__ == "__main__":
    
    file_Name = input("Please enter the file name: ")
    scraper = FileScraper(file_Name)
    


    