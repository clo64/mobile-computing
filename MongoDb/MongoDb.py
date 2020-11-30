from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient('mongodb+srv://cowen:compproject@cluster0.1qgln.mongodb.net/Cluster0?retryWrites=true&w=majority')
    db = client.rooms               #creates database connection

    #test entry object
    sensor_package = {
            'PIP':1,
            'Temperature':1,
            'Humidity'   :1,
            'Light'      :1
            }
    #new = {'$set': {'room_one': 'boom'}}

    result = db.PIPdata.insert_one(sensor_package)

    #{"_id":{"$oid":"5fc4270e52d7e473db15b9d8"},"room_one":"kitchen"}

    