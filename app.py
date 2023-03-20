from flask import Flask,jsonify,request
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb+srv://ChiragRohada:s54icYoW4045LhAW@atlascluster.t7vxr4g.mongodb.net/test")

mydb = myclient["IOT"]

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# class create_dict(dict): 
  
#     # __init__ function 
#     def __init__(self): 
#         self = dict() 
          
#     # Function to add key:value 
#     def add(self, key, value): 
#         self[key] = value 
        


def Api(api):
    mycol = mydb['Api']
    
    api1=mycol.find({"api_key":api})
    print(api1)

    
    api3=0
    for i in api1:
        api3=i

    return api3


@app.route("/users/<api>",methods = ['POST', 'GET'])
def Users(api):

    

    if (Api(api)):

        mycol = mydb['Users']
    
       
        
        list=[]
        for y in mycol.find():
            list.append({"name":y['name'],"email":y['email']})

        mydict={"response":list}
            
    
        return jsonify(mydict)
    else:
        return "wrong api_key"

@app.route("/accident/<api>",methods = ['POST', 'GET'])
def Accident(api):

    if (Api(api)):
            mycol = mydb['accident']
    
            list=[]
            i = 1
            for y in mycol.find():
                list.append({"Device_id":y['iot_id'],"Location":y['location'],"Vehicle_no":y['vehicle_no'],"Email":y['email'],"Critical":y['critical'],"Postcode":y['postcode'],"Date":y['date'],"Staff_email":y['staff_email'],"Staff_name":y['staff_name'],"Rescued":y['user_rescued']})
                
            mydict={"response":list}
            return jsonify(mydict)
    else:
        return "wrong api_key"







@app.route("/hospital_connect/<api>",methods = ['POST', 'GET'])
def Hospital_connect(api):
    if (Api(api)):
        mycol = mydb['HospitalData']
    
        list=[]
        i = 1
        for y in mycol.find():
            list.append({"Name":y['name'],"City":y['city'],"Location":y['location'],"Zipcode":y['zipcode']})
            
        mydict={"response":list}
        return jsonify(mydict)
    else:
        return "wrong api_key"

    


@app.route("/Staff/<api>",methods = ['POST', 'GET'])
def Staff(api):
    if (Api(api)):
            mycol = mydb['Staff']
    
            list=[]
            i = 1
            for y in mycol.find():
                list.append({"Email":y['email'],"Name":y['name']})

            mydict={"response":list}  
    
            return jsonify(mydict)
    else:
        return "wrong api_key"
    




