from flask import Flask,jsonify,request
from flask import Flask, redirect, url_for, render_template, request, flash,session
import pymongo
from flask_mail import Mail, Message
from flask import Blueprint
import haversine as hs
from flask_bcrypt import Bcrypt
import os
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app
from flask_session import Session






ambulance =Blueprint('ambulance',__name__)


myclient = pymongo.MongoClient("mongodb+srv://ChiragRohada:s54icYoW4045LhAW@atlascluster.t7vxr4g.mongodb.net/test")
mydb = myclient["IOT"]
import string
import random


def Api(api):
    mycol = mydb['Api']
    
    api1=mycol.find({"api_key":api})
    print(api1)

    
    api3=0
    for i in api1:
        api3=i

    return api3



@ambulance.route("/ambulance_register/<api>",methods = ['POST', 'GET'])
def ambulance_register(api):
    try:
        if (Api(api)):
        
            name=request.json["name"]
            mobile=request.json["mobile"]
            address=request.json["address"]
            email=request.json["email"]
            user_password=request.json["password"]
            password = generate_password_hash(user_password)
            mycol = mydb["Staff"]
            mycol.insert_one({"name":name,"email":email,"mobile":mobile,"address":address,"password":password})
            return "Success", 201
        else:
            return "Error",400
    except:
        return "error",400
    
@ambulance.route("/ambulance_login/<api>",methods = ['POST', 'GET'])
def ambulance_login(api):
    try:
        if (Api(api)):
        

        
       
            email=request.json["email"]
            password=request.json["password"]
        
            mycol = mydb["Staff"]
            user=mycol.find_one({"email":email})

            if (check_password_hash(user['password'], password)):
                session['ambulance_login']=email
            else:
                return "Wrong Credentials",400

            return "Success", 201
    except:
        return "error",400


@ambulance.route("/ambulance_accident/<lat>/<log>/<api>",methods = ['POST', 'GET'])
def ambulance_accident(lat,log,api):
    try:
        if (Api(api)):



            mycol = mydb["accident"]
            x=mycol.find({'critical':1})
            list=[]
            for i in x:
                loc1=(float(i['location'][0]),float(i['location'][1]))
                loc2=(float(lat),float(log))
                distance=hs.haversine(loc1,loc2)
            
            
        

            
                if(distance<5):
                    list.append({"vehicle_no":i['vehicle_no'],"location":loc1,"email":i["email"],"date":i['date'],"vehicle_id":i['iot_id']})

        

            mydict={"response":list}
            
    
            return jsonify(mydict)
        else:
            return "wrong api",400
    except:
        return "error",400

    

@ambulance.route("/ambulance_accept/<api>",methods = ['POST', 'GET'])
def ambulance_acept(api):
    try:
        if (Api(api)):

            iot_id=request.json["vehicle_id"]
            driver_email=request.json["email"]
            driver_name=request.json["name"]
            mycol = mydb["accident"]
            mycol.update_one({'iot_id':iot_id},{"$set":{'staff_email':driver_email,'staff_name':driver_name}})
            return "ok"
        else:
            return "wrong api",400
    except:
        return "error",400



