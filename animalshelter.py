#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # use MongoClient to access to the Mongodb database
        self.client = MongoClient('mongodb://%s:%s@localhost:42007/test?authSource=AAC' % ("aacuser1", "test"))
        self.database = self.client['AAC']

   # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("++++++++++++++++++ animal created +++++++++++++++")
        else:
            raise Exception("There's othing to save")
            
   # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False})  # data should be dictionary   
            return data
        else:
            raise Exception("There's nothing to read")
            
            
    # this is delete method 
    def delete(self, _data):
        if _data is not None:
            data = self.read(_data) # checj if animal exists
            if data is None:
                print("Animal not found")
                return
            #if found delete the animal or animals
            self.database.animals.delete_many(_data)  # data should be dictionary 
            data = self.read(_data) #confirm if animal was deleted
            return data
        else:
            raise Exception("There's nothing to delete")
            
    # for updating the animal database    def update(self, _keys,_data):
        if _data is not None and _keys is not None:
            self.database.animals.update_many(_keys,{'$set':_data})  # _keys will check for the doc to update 
            data = self.read(_data)
            return data
        else:
            raise Exception("please enter both key and data to edit")