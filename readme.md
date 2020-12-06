Okay!

NOTE: pip_to_database.py is your "main" application that you'll run. Remember that. 

Here's how it works. You have to run this command to get the PIP tag data writing into a file
called data.txt:

sudo stdbuf -o0 ./pip_sense.v2 l l | stdbuf -o0 grep TX:0$1 | cat > data.txt

Then, you need to edit this line in pip_to_database.py:

9 file_Name = './PIPtagCode/ReceiverCode/data.txt'
The above line MUST point to the directory that you're storing your data.txt file in.

Start up your PIP tag and it'll start writing out to data.txt. Then, you can run pip_to_database.py
and it'll start reading the data and uploading it to the Mongo Database.

Have Fun. Fly Safe. 

***How to run the webpage***

After you install express and get a node_modules folder, add the node_modules files from this
repository to the node_modules folder.

Install charts.js into the node_modules folder also. Google installation syntax.

run: node server.js

Now go to: http://localhost:8080/PIPdata in your browser , you should see the graph and it 
should be updating.

Now go run the piptag and scrape in your linux environment. 

Witness the magic.
