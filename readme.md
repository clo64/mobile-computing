Okay!
Here's how it works. You have to run this command to get the PIP tag data writing into a file
called data.txt:

NOTE: pip_to_database.py is you "main" application that you'll run. Remember that. 

sudo stdbuf -o0 ./pip_sense.v2 l l | stdbuf -o0 grep TX:0$1 | cat > data.txt

Then, you need to edit this line in pip_to_database.py:

9 file_Name = './PIPtagCode/ReceiverCode/data.txt'
The above line MUST point to the directory that you're storing your data.txt file in.

Start up your PIP tag and it'll start writing out to data.txt. Then, you can run pip_to_database.py
and it'll start reading the data and uploading it to the Mongo Database.

Have Fun. Fly Safe. 

