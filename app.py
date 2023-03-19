from flask import Flask,jsonify,request
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb+srv://ChiragRohada:s54icYoW4045LhAW@atlascluster.t7vxr4g.mongodb.net/test")

mydb = myclient["IOT"]

if __name__ == '__main__':
    app.run(host='0.0.0.0')

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
        

@app.route("/",methods = ['POST', 'GET'])
def Home():
    mycol = mydb['Users']
    
    mydict = create_dict()
    i = 1
    for y in mycol.find():
        mydict.add(i, ({"name":y['name'],"email":y['email']}))
        i = i+1
    
    return jsonify(mydict)