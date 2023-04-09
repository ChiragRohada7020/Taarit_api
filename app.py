from flask import Flask,jsonify,request
from flask import Flask, redirect, url_for, render_template, request, flash,session
import pymongo
from flask_mail import Mail, Message
from Home.Ambulance.ambulance import ambulance
from flask_bcrypt import Bcrypt
import os
from werkzeug.security import check_password_hash, generate_password_hash






app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb+srv://ChiragRohada:s54icYoW4045LhAW@atlascluster.t7vxr4g.mongodb.net/test")

import string
import random



app.secret_key=os.urandom(24)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


bcrypt = Bcrypt(app)



app.register_blueprint(ambulance)


# class create_dict(dict): 
  
#     # __init__ function 
#     def __init__(self): 
#         self = dict() 
          
#     # Function to add key:value 
#     def add(self, key, value): 
#         self[key] = value 
mydb = myclient["IOT"]
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ' taarit364@gmail.com'
app.config['MAIL_PASSWORD'] = 'bnneszfcnfhvkibn'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



def Api(api):
    mycol = mydb['Api']
    
    api1=mycol.find({"api_key":api})
    print(api1)

    
    api3=0
    for i in api1:
        api3=i

    return api3


def mailing(email,res):
    msg = Message(
                "Taarit Api",
                sender ='taarit364@gmail.com',
                recipients = [email]
               )
    msg.html ="""
            <!DOCTYPE html>

<html
  lang="en"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns:v="urn:schemas-microsoft-com:vml"
>
  <head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
   
    <link
      href="https://fonts.googleapis.com/css?family=Noto+Sans"
      rel="stylesheet"
      type="text/css"
    />
   
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        padding: 0;
      }

      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: inherit !important;
      }

      #MessageViewBody a {
        color: inherit;
        text-decoration: none;
      }

      p {
        line-height: inherit;
      }

      .desktop_hide,
      .desktop_hide table {
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
      }

      .image_block img + div {
        display: none;
      }

      .menu_block.desktop_hide .menu-links span {
        mso-hide: all;
      }

      @media (max-width: 720px) {
        .desktop_hide table.icons-inner {
          display: inline-block !important;
        }

        .icons-inner {
          text-align: center;
        }

        .icons-inner td {
          margin: 0 auto;
        }

        .row-content {
          width: 100% !important;
        }

        .mobile_hide {
          display: none;
        }

        .stack .column {
          width: 100%;
          display: block;
        }

        .mobile_hide {
          min-height: 0;
          max-height: 0;
          max-width: 0;
          overflow: hidden;
          font-size: 0px;
        }

        .desktop_hide,
        .desktop_hide table {
          display: table !important;
          max-height: none !important;
        }

        .row-3 .column-1 .block-2.image_block td.pad {
          padding: 20px 20px 0 !important;
        }

        .row-2 .column-2 .block-1.menu_block td.pad {
          padding: 30px 10px 10px !important;
        }

        .row-2 .column-2 .block-1.menu_block .menu-links a,
        .row-2 .column-2 .block-1.menu_block .menu-links span {
          font-size: 16px !important;
        }

        .row-3 .column-1 .block-4.heading_block h1 {
          font-size: 35px !important;
        }
      }
    </style>
  </head>
  <body
    style="
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: none;
      text-size-adjust: none;
    "
  >
    <table
      border="0"
      cellpadding="0"
      cellspacing="0"
      class="nl-container"
      role="presentation"
      style="
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        background-color: #ffffff;
      "
      width="100%"
    >
      <tbody>
        <tr>
          <td>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              class="row row-1"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
              width="100%"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      class="row-content stack"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e5f1fd;
                        border-radius: 0;
                        color: #000000;
                        width: 700px;
                      "
                      width="700"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="100%"
                          >
                            <div
                              class="spacer_block block-1"
                              style="
                                height: 30px;
                                line-height: 30px;
                                font-size: 1px;
                              "
                            >
                               
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              class="row row-2"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
              width="100%"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      class="row-content stack"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e5f1fd;
                        color: #000000;
                        width: 700px;
                      "
                      width="700"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: middle;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="50%"
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              class="heading_block block-1"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="width: 100%; text-align: center"
                                >
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #555555;
                                      font-size: 23px;
                                      font-family: Noto Sans, Trebuchet MS,
                                        Helvetica, sans-serif;
                                      line-height: 120%;
                                      text-align: center;
                                      direction: ltr;
                                      font-weight: 700;
                                      letter-spacing: normal;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span class="tinyMce-placeholder"
                                      >TAARIT
                                    </span>
                                  </h1>
                                </td>
                              </tr>
                            </table>
                          </td>
                          <td
                            class="column column-2"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: middle;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="50%"
                          >
                            <table
                              border="0"
                              cellpadding="10"
                              cellspacing="0"
                              class="menu_block block-1"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td class="pad">
                                  <table
                                    border="0"
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                    style="
                                      mso-table-lspace: 0pt;
                                      mso-table-rspace: 0pt;
                                    "
                                    width="100%"
                                  >
                                    <tr>
                                      <td
                                        class="alignment"
                                        style="
                                          text-align: center;
                                          font-size: 0px;
                                        "
                                      >
                                        <div class="menu-links">
                                          <a
                                            href="https://taarit2.onrender.com"
                                            style="
                                              mso-hide: false;
                                              padding-top: 5px;
                                              padding-bottom: 5px;
                                              padding-left: 10px;
                                              padding-right: 10px;
                                              display: inline-block;
                                              color: #003770;
                                              font-family: 'Noto Sans',
                                                'Trebuchet MS', Helvetica,
                                                sans-serif;
                                              font-size: 16px;
                                              text-decoration: none;
                                              letter-spacing: normal;
                                            "
                                            target="_self"
                                            >HOME</a
                                          >><!--[if mso]></td><!
                                          [endif]-->[endif]--><!--[if mso]><td style="padding-top:5px;padding-right:10px;padding-bottom:5px;padding-left:10px"><!
                                          [endif]--><a
                                            href="https://taarit2.onrender.com/login"
                                            style="
                                              mso-hide: false;
                                              padding-top: 5px;
                                              padding-bottom: 5px;
                                              padding-left: 10px;
                                              padding-right: 10px;
                                              display: inline-block;
                                              color: #003770;
                                              font-family: 'Noto Sans',
                                                'Trebuchet MS', Helvetica,
                                                sans-serif;
                                              font-size: 16px;
                                              text-decoration: none;
                                              letter-spacing: normal;
                                            "
                                            target="_self"
                                            >LOG IN</a
                                          >><!--[if mso]></td><!
                                          [endif]-->[endif]--><!--[if mso]></tr></table><![endif]-->
                                        </div>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              class="row row-3"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
              width="100%"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      class="row-content stack"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #e5f1fd;
                        border-radius: 0;
                        color: #000000;
                        width: 700px;
                      "
                      width="700"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="100%"
                          >
                            <div
                              class="spacer_block block-1 mobile_hide"
                              style="
                                height: 40px;
                                line-height: 40px;
                                font-size: 1px;
                              "
                            >
                               
                            </div>
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              class="image_block block-2"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    width: 100%;
                                    padding-right: 0px;
                                    padding-left: 0px;
                                  "
                                >
                                  <div
                                    align="center"
                                    class="alignment"
                                    style="line-height: 10px"
                                  >
                                    <img
                                      alt="Hero Image"
                                      src="https://www.elemental.co.za/cms/resources/uploads/blog/86/926f6aaba773.png"
                                      style="
                                        display: block;
                                        height: auto;
                                        border: 0;
                                        width: 315px;
                                        max-width: 100%;
                                      "
                                      title="Hero Image"
                                      width="315"
                                    />
                                  </div>
                                </td>
                              </tr>
                            </table>
                            <div
                              class="spacer_block block-3 mobile_hide"
                              style="
                                height: 30px;
                                line-height: 30px;
                                font-size: 1px;
                              "
                            >
                               
                            </div>
                            <table
                              border="0"
                              cellpadding="10"
                              cellspacing="0"
                              class="heading_block block-4"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td class="pad">
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #0274ee;
                                      direction: ltr;
                                      font-family: 'Noto Sans', 'Trebuchet MS',
                                        Helvetica, sans-serif;
                                      font-size: 40px;
                                      font-weight: 400;
                                      letter-spacing: normal;
                                      line-height: 150%;
                                      text-align: center;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span class="tinyMce-placeholder"
                                      >Congratulations<br
                                    /></span>
                                  </h1>
                                </td>
                              </tr>
                            </table>
                            <div
                              class="spacer_block block-5"
                              style="
                                height: 30px;
                                line-height: 30px;
                                font-size: 1px;
                              "
                            >
                               
                            </div>
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              class="heading_block block-6"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="width: 100%; text-align: center"
                                >
                                  <h1
                                    style="
                                      margin: 0;
                                      color: #555555;
                                      font-size: 23px;
                                      font-family: Noto Sans, Trebuchet MS,
                                        Helvetica, sans-serif;
                                      line-height: 120%;
                                      text-align: center;
                                      direction: ltr;
                                      font-weight: 700;
                                      letter-spacing: normal;
                                      margin-top: 0;
                                      margin-bottom: 0;
                                    "
                                  >
                                    <span class="tinyMce-placeholder"
                                      >API KEY :-"""+res+"""
                                    </span>
                                  </h1>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              class="row row-4"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
              width="100%"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      class="row-content stack"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        background-color: #0274ee;
                        border-left: 16px solid #e5f1fd;
                        border-radius: 0;
                        border-right: 16px solid #e5f1fd;
                        border-top: 30px solid #e5f1fd;
                        color: #000000;
                        width: 700px;
                      "
                      width="700"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="100%"
                          >
                            <div
                              class="spacer_block block-1"
                              style="
                                height: 20px;
                                line-height: 20px;
                                font-size: 1px;
                              "
                            >
                               
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              class="row row-5"
              role="presentation"
              style="mso-table-lspace: 0pt; mso-table-rspace: 0pt"
              width="100%"
            >
              <tbody>
                <tr>
                  <td>
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      class="row-content stack"
                      role="presentation"
                      style="
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        color: #000000;
                        width: 700px;
                      "
                      width="700"
                    >
                      <tbody>
                        <tr>
                          <td
                            class="column column-1"
                            style="
                              mso-table-lspace: 0pt;
                              mso-table-rspace: 0pt;
                              font-weight: 400;
                              text-align: left;
                              padding-bottom: 5px;
                              padding-top: 5px;
                              vertical-align: top;
                              border-top: 0px;
                              border-right: 0px;
                              border-bottom: 0px;
                              border-left: 0px;
                            "
                            width="100%"
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              class="icons_block block-1"
                              role="presentation"
                              style="
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                              "
                              width="100%"
                            >
                              <tr>
                                <td
                                  class="pad"
                                  style="
                                    vertical-align: middle;
                                    color: #9d9d9d;
                                    font-family: inherit;
                                    font-size: 15px;
                                    padding-bottom: 5px;
                                    padding-top: 5px;
                                    text-align: center;
                                  "
                                >
                                  <table
                                    cellpadding="0"
                                    cellspacing="0"
                                    role="presentation"
                                    style="
                                      mso-table-lspace: 0pt;
                                      mso-table-rspace: 0pt;
                                    "
                                    width="100%"
                                  >
                                    <tr>
                                      <td
                                        class="alignment"
                                        style="
                                          vertical-align: middle;
                                          text-align: center;
                                        "
                                      >
                                        <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                        <!--[if !vml]><!-->
                                        <table
                                          cellpadding="0"
                                          cellspacing="0"
                                          class="icons-inner"
                                          role="presentation"
                                          style="
                                            mso-table-lspace: 0pt;
                                            mso-table-rspace: 0pt;
                                            display: inline-block;
                                            margin-right: -4px;
                                            padding-left: 0px;
                                            padding-right: 0px;
                                          "
                                        >
                                          <!--<![endif]-->
                                        </table>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- End -->
  </body>
</html>

        """
      
    mail.send(msg)




@app.route("/",methods = ['POST', 'GET'])
def Home():
    try:
        if 'user_login' in session:
            return render_template('index.html',login=1)
        else:
            return render_template('index.html',login=0)
    except:
        return "error"
            
        
    

@app.route("/docs",methods = ['POST', 'GET'])
def Docs():
    try:
        if 'user_login' in session:
          mycol = mydb['Api']
          print(session["user_login"])
          data=mycol.find_one({"email":session['user_login']})
          
          return render_template('doc.html',login=1,data=data["api_key"])
        else:
            return render_template('doc.html')
    except:
        return 'error'
    
global chirag

@app.route("/register",methods = ['POST', 'GET'])
def Register_user():
    return render_template('Regsiter_user.html')






@app.route("/logout",methods = ['POST', 'GET'])
def Logout():
    session.pop('user_login')
    return redirect(url_for('Home'))


@app.route("/sahil/<code>",methods = ['POST', 'GET'])
def Sahil(code):
    print(code)
    chirag=code
    
    
    return code

@app.route("/login",methods = ['POST', 'GET'])
def Login():
    try:
        if 'user_login' in session:
            return  redirect(url_for('Home'))
            
        if request.method == 'POST':
          email=request.form["email"]
          password=request.form["password"]
          mycol = mydb['Api']
          user=mycol.find_one({"email":email})
          
          if(check_password_hash(user['password'], password)):
              session['user_login']=email
              return redirect(url_for('Home'))
          else:
              return "wrong credentials"
        else:
            return render_template('login.html')
            
          
          
    except:
        return "error"
              
          
        
    
    
    

@app.route("/register_api",methods = ['POST', 'GET'])
def Register():
    try:
        if request.method == 'POST':
            name=request.form['Name']
            email=request.form['email']
            password=request.form['password']
            password = generate_password_hash(password)
            res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10))
            mycol = mydb["Api"]
            x=mycol.find_one({"email":email})
            if x:
                flash("Aleardy Registered")
                return  redirect(url_for('Login'))


            mycol.insert_one({"name":name,"email":email,"password":password,"api_key":res})

            
            mailing(email,res)
            flash("Successfully Registered")
            
            
    except Exception as e:
        print(e)
        flash("Register Failed")
    
    return  redirect(url_for('Login'))


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
    




