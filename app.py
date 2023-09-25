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
    

@app.route("/register",methods = ['POST', 'GET'])
def Register_user():
    return render_template('Regsiter_user.html')






@app.route("/logout",methods = ['POST', 'GET'])
def Logout():
    session.pop('user_login')
    return redirect(url_for('Home'))




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
construction_data = [
    {"sq_ft": 28900, "cement_bags": 578, "bricks_count": 144500, "steel_tons": 57.8, "cost_inr": 4211860},
    {"sq_ft": 29400, "cement_bags": 588, "bricks_count": 147000, "steel_tons": 58.8, "cost_inr": 4283580},
    {"sq_ft": 30000, "cement_bags": 600, "bricks_count": 150000, "steel_tons": 60, "cost_inr": 4380000},
    {"sq_ft": 30500, "cement_bags": 610, "bricks_count": 152500, "steel_tons": 61, "cost_inr": 4451720},
    {"sq_ft": 31000, "cement_bags": 620, "bricks_count": 155000, "steel_tons": 62, "cost_inr": 4523440},
    {"sq_ft": 31600, "cement_bags": 632, "bricks_count": 158000, "steel_tons": 63.2, "cost_inr": 4612280},
    {"sq_ft": 32100, "cement_bags": 642, "bricks_count": 160500, "steel_tons": 64.2, "cost_inr": 4684000},
    {"sq_ft": 32700, "cement_bags": 654, "bricks_count": 163500, "steel_tons": 65.4, "cost_inr": 4772840},
    {"sq_ft": 33200, "cement_bags": 664, "bricks_count": 166000, "steel_tons": 66.4, "cost_inr": 4844560},
    {"sq_ft": 33700, "cement_bags": 674, "bricks_count": 168500, "steel_tons": 67.4, "cost_inr": 4916280},
    {"sq_ft": 34300, "cement_bags": 686, "bricks_count": 171500, "steel_tons": 68.6, "cost_inr": 5005120},
    {"sq_ft": 34800, "cement_bags": 696, "bricks_count": 174000, "steel_tons": 69.6, "cost_inr": 5076840},
    {"sq_ft": 35300, "cement_bags": 706, "bricks_count": 176500, "steel_tons": 70.6, "cost_inr": 5148560},
    {"sq_ft": 35900, "cement_bags": 718, "bricks_count": 179500, "steel_tons": 71.8, "cost_inr": 5237400},
    {"sq_ft": 36400, "cement_bags": 728, "bricks_count": 182000, "steel_tons": 72.8, "cost_inr": 5309120},
    {"sq_ft": 36900, "cement_bags": 738, "bricks_count": 184500, "steel_tons": 73.8, "cost_inr": 5380840},
    {"sq_ft": 37500, "cement_bags": 750, "bricks_count": 187500, "steel_tons": 75, "cost_inr": 5477250},
    {"sq_ft": 38000, "cement_bags": 760, "bricks_count": 190000, "steel_tons": 76, "cost_inr": 5549000},
    {"sq_ft": 38500, "cement_bags": 770, "bricks_count": 192500, "steel_tons": 77, "cost_inr": 5620750},
    {"sq_ft": 39100, "cement_bags": 782, "bricks_count": 195500, "steel_tons": 78.2, "cost_inr": 5709590},
    {"sq_ft": 39600, "cement_bags": 792, "bricks_count": 198000, "steel_tons": 79.2, "cost_inr": 5781310},
    {"sq_ft": 40100, "cement_bags": 802, "bricks_count": 200500, "steel_tons": 80.2, "cost_inr": 5853030},
    {"sq_ft": 40700, "cement_bags": 814, "bricks_count": 203500, "steel_tons": 81.4, "cost_inr": 5941870},
    {"sq_ft": 41200, "cement_bags": 824, "bricks_count": 206000, "steel_tons": 82.4, "cost_inr": 6013590},
    {"sq_ft": 41700, "cement_bags": 834, "bricks_count": 208500, "steel_tons": 83.4, "cost_inr": 6085310},
    {"sq_ft": 42300, "cement_bags": 846, "bricks_count": 211500, "steel_tons": 84.6, "cost_inr": 6174150},
    {"sq_ft": 42800, "cement_bags": 856, "bricks_count": 214000, "steel_tons": 85.6, "cost_inr": 6245870},
    {"sq_ft": 43300, "cement_bags": 866, "bricks_count": 216500, "steel_tons": 86.6, "cost_inr": 6317590},
    {"sq_ft": 43900, "cement_bags": 878, "bricks_count": 219500, "steel_tons": 87.8, "cost_inr": 6406430},
    {"sq_ft": 44400, "cement_bags": 888, "bricks_count": 222000, "steel_tons": 88.8, "cost_inr": 6478150},
    {"sq_ft": 44900, "cement_bags": 898, "bricks_count": 224500, "steel_tons": 89.8, "cost_inr": 6549870},
    {"sq_ft": 45500, "cement_bags": 910, "bricks_count": 227500, "steel_tons": 91, "cost_inr": 6646285},
    {"sq_ft": 46000, "cement_bags": 920, "bricks_count": 230000, "steel_tons": 92, "cost_inr": 6718000},
    {"sq_ft": 46500, "cement_bags": 930, "bricks_count": 232500, "steel_tons": 93, "cost_inr": 6789725},
    {"sq_ft": 47100, "cement_bags": 942, "bricks_count": 235500, "steel_tons": 94.2, "cost_inr": 6878565},
    {"sq_ft": 47600, "cement_bags": 952, "bricks_count": 238000, "steel_tons": 95.2, "cost_inr": 6950280},
    {"sq_ft": 48100, "cement_bags": 962, "bricks_count": 240500, "steel_tons": 96.2, "cost_inr": 7022005},
    {"sq_ft": 48700, "cement_bags": 974, "bricks_count": 243500, "steel_tons": 97.4, "cost_inr": 7110845},
    {"sq_ft": 49200, "cement_bags": 984, "bricks_count": 246000, "steel_tons": 98.4, "cost_inr": 7182560},
    {"sq_ft": 49700, "cement_bags": 994, "bricks_count": 248500, "steel_tons": 99.4, "cost_inr": 7254285},
    {"sq_ft": 50300, "cement_bags": 1006, "bricks_count": 251500, "steel_tons": 100.6, "cost_inr": 7343125},
    {"sq_ft": 50800, "cement_bags": 1016, "bricks_count": 254000, "steel_tons": 101.6, "cost_inr": 7414840},
    {"sq_ft": 51300, "cement_bags": 1026, "bricks_count": 256500, "steel_tons": 102.6, "cost_inr": 7486565},
      {
        "sq_ft": 1000,
        "cement_bags": 20,
        "bricks_count": 5000,
        "steel_tons": 2,
        "cost_inr": 138700
    },
    {
        "sq_ft": 1500,
        "cement_bags": 30,
        "bricks_count": 7500,
        "steel_tons": 3,
        "cost_inr": 208050
    },
    {
        "sq_ft": 2000,
        "cement_bags": 40,
        "bricks_count": 10000,
        "steel_tons": 4,
        "cost_inr": 277400
    },
    {
        "sq_ft": 2500,
        "cement_bags": 50,
        "bricks_count": 12500,
        "steel_tons": 5,
        "cost_inr": 346750
    },
    {
        "sq_ft": 3000,
        "cement_bags": 60,
        "bricks_count": 15000,
        "steel_tons": 6,
        "cost_inr": 416100
    },
    {
        "sq_ft": 1200,
        "cement_bags": 24,
        "bricks_count": 6000,
        "steel_tons": 2.4,
        "cost_inr": 166440
    },
    {
        "sq_ft": 1800,
        "cement_bags": 36,
        "bricks_count": 9000,
        "steel_tons": 3.6,
        "cost_inr": 249660
    },
    {
        "sq_ft": 2200,
        "cement_bags": 44,
        "bricks_count": 11000,
        "steel_tons": 4.4,
        "cost_inr": 323780
    },
    {
        "sq_ft": 2700,
        "cement_bags": 54,
        "bricks_count": 13500,
        "steel_tons": 5.4,
        "cost_inr": 416550
    },
    {
        "sq_ft": 3500,
        "cement_bags": 70,
        "bricks_count": 17500,
        "steel_tons": 7,
        "cost_inr": 508770
    },
    {
        "sq_ft": 1400,
        "cement_bags": 28,
        "bricks_count": 7000,
        "steel_tons": 2.8,
        "cost_inr": 193580
    },
    {
        "sq_ft": 1600,
        "cement_bags": 32,
        "bricks_count": 8000,
        "steel_tons": 3.2,
        "cost_inr": 221200
    },
    {
        "sq_ft": 2100,
        "cement_bags": 42,
        "bricks_count": 10500,
        "steel_tons": 4.2,
        "cost_inr": 290100
    },
    {
        "sq_ft": 2600,
        "cement_bags": 52,
        "bricks_count": 13000,
        "steel_tons": 5.2,
        "cost_inr": 358700
    },
    {
        "sq_ft": 3200,
        "cement_bags": 64,
        "bricks_count": 16000,
        "steel_tons": 6.4,
        "cost_inr": 443680
    },
    {
        "sq_ft": 1700,
        "cement_bags": 34,
        "bricks_count": 8500,
        "steel_tons": 3.4,
        "cost_inr": 234920
    },
    {
        "sq_ft": 1900,
        "cement_bags": 38,
        "bricks_count": 9500,
        "steel_tons": 3.8,
        "cost_inr": 262540
    },
    {
        "sq_ft": 2300,
        "cement_bags": 46,
        "bricks_count": 11500,
        "steel_tons": 4.6,
        "cost_inr": 318590
    },
    {
        "sq_ft": 2800,
        "cement_bags": 56,
        "bricks_count": 14000,
        "steel_tons": 5.6,
        "cost_inr": 386900
    },
    {
        "sq_ft": 3600,
        "cement_bags": 72,
        "bricks_count": 18000,
        "steel_tons": 7.2,
        "cost_inr": 498360
    },
    {
        "sq_ft": 1300,
        "cement_bags": 26,
        "bricks_count": 6500,
        "steel_tons": 2.6,
        "cost_inr": 179710
    },
    {
        "sq_ft": 2400,
        "cement_bags": 48,
        "bricks_count": 12000,
        "steel_tons": 4.8,
        "cost_inr": 332880
    },
    {
        "sq_ft": 2900,
        "cement_bags": 58,
        "bricks_count": 14500,
        "steel_tons": 5.8,
        "cost_inr": 400350
    },
    {
        "sq_ft": 3800,
        "cement_bags": 76,
        "bricks_count": 19000,
        "steel_tons": 7.6,
        "cost_inr": 523400
    },
    {
        "sq_ft": 3100,
        "cement_bags": 62,
        "bricks_count": 15500,
        "steel_tons": 6.2,
        "cost_inr": 426950
    },
    {
        "sq_ft": 3300,
        "cement_bags": 66,
        "bricks_count": 16500,
        "steel_tons": 6.6,
        "cost_inr": 455575
    },
    {
        "sq_ft": 3700,
        "cement_bags": 74,
        "bricks_count": 18500,
        "steel_tons": 7.4,
        "cost_inr": 509450
    },
    {
        "sq_ft": 4000,
        "cement_bags": 80,
        "bricks_count": 20000,
        "steel_tons": 8,
        "cost_inr": 554600
    },
    {
        "sq_ft": 1000,
        "cement_bags": 20,
        "bricks_count": 5000,
        "steel_tons": 2,
        "cost_inr": 138700
    },
    {
        "sq_ft": 1500,
        "cement_bags": 30,
        "bricks_count": 7500,
        "steel_tons": 3,
        "cost_inr": 208050
    },
    {
        "sq_ft": 2000,
        "cement_bags": 40,
        "bricks_count": 10000,
        "steel_tons": 4,
        "cost_inr": 277400
    },
    {
        "sq_ft": 2500,
        "cement_bags": 50,
        "bricks_count": 12500,
        "steel_tons": 5,
        "cost_inr": 346750
    },
    {
        "sq_ft": 3000,
        "cement_bags": 60,
        "bricks_count": 15000,
        "steel_tons": 6,
        "cost_inr": 416100
    },
    {
        "sq_ft": 1200,
        "cement_bags": 24,
        "bricks_count": 6000,
        "steel_tons": 2.4,
        "cost_inr": 166440
    },
    {
        "sq_ft": 1800,
        "cement_bags": 36,
        "bricks_count": 9000,
        "steel_tons": 3.6,
        "cost_inr": 249660
    },
    {
        "sq_ft": 2200,
        "cement_bags": 44,
        "bricks_count": 11000,
        "steel_tons": 4.4,
        "cost_inr": 323780
    },
    {
        "sq_ft": 2700,
        "cement_bags": 54,
        "bricks_count": 13500,
        "steel_tons": 5.4,
        "cost_inr": 416550
    },
    {
        "sq_ft": 3500,
        "cement_bags": 70,
        "bricks_count": 17500,
        "steel_tons": 7,
        "cost_inr": 508770
    },
    {
        "sq_ft": 1400,
        "cement_bags": 28,
        "bricks_count": 7000,
        "steel_tons": 2.8,
        "cost_inr": 193580
    },
    {
        "sq_ft": 1600,
        "cement_bags": 32,
        "bricks_count": 8000,
        "steel_tons": 3.2,
        "cost_inr": 221200
    },
    {
        "sq_ft": 2100,
        "cement_bags": 42,
        "bricks_count": 10500,
        "steel_tons": 4.2,
        "cost_inr": 290100
    },
    {
        "sq_ft": 2600,
        "cement_bags": 52,
        "bricks_count": 13000,
        "steel_tons": 5.2,
        "cost_inr": 358700
    },
    {
        "sq_ft": 3200,
        "cement_bags": 64,
        "bricks_count": 16000,
        "steel_tons": 6.4,
        "cost_inr": 443680
    },
    {
        "sq_ft": 1700,
        "cement_bags": 34,
        "bricks_count": 8500,
        "steel_tons": 3.4,
        "cost_inr": 234920
    },
    {
        "sq_ft": 1900,
        "cement_bags": 38,
        "bricks_count": 9500,
        "steel_tons": 3.8,
        "cost_inr": 262540
    },
    {
        "sq_ft": 2300,
        "cement_bags": 46,
        "bricks_count": 11500,
        "steel_tons": 4.6,
        "cost_inr": 318590
    },
    {
        "sq_ft": 2800,
        "cement_bags": 56,
        "bricks_count": 14000,
        "steel_tons": 5.6,
        "cost_inr": 386900
    },
    {
        "sq_ft": 3600,
        "cement_bags": 72,
        "bricks_count": 18000,
        "steel_tons": 7.2,
        "cost_inr": 498360
    },
    {
        "sq_ft": 1300,
        "cement_bags": 26,
        "bricks_count": 6500,
        "steel_tons": 2.6,
        "cost_inr": 179710
    },
    {
        "sq_ft": 2400,
        "cement_bags": 48,
        "bricks_count": 12000,
        "steel_tons": 4.8,
        "cost_inr": 332880
    },
    {
        "sq_ft": 2900,
        "cement_bags": 58,
        "bricks_count": 14500,
        "steel_tons": 5.8,
        "cost_inr": 400350
    },
    {
        "sq_ft": 3800,
        "cement_bags": 76,
        "bricks_count": 19000,
        "steel_tons": 7.6,
        "cost_inr": 523400
    },
    {
        "sq_ft": 3100,
        "cement_bags": 62,
        "bricks_count": 15500,
        "steel_tons": 6.2,
        "cost_inr": 426950
    },
    {
        "sq_ft": 3300,
        "cement_bags": 66,
        "bricks_count": 16500,
        "steel_tons": 6.6,
        "cost_inr": 455575
    },
    {
        "sq_ft": 3700,
        "cement_bags": 74,
        "bricks_count": 18500,
        "steel_tons": 7.4,
        "cost_inr": 509450
    },
    {
        "sq_ft": 4000,
        "cement_bags": 80,
        "bricks_count": 20000,
        "steel_tons": 8,
        "cost_inr": 554600
    }
]


@app.route('/construction_cost', methods=['GET'])
def calculate_construction_cost():
    try:
        sq_ft = float(request.args.get('sq_ft'))
        # Find the closest match based on square feet (you can customize this logic)
        closest_match = min(construction_data, key=lambda x: abs(x["sq_ft"] - sq_ft))
        
        # Extract cost details
        cement_bags = closest_match["cement_bags"]
        bricks_count = closest_match["bricks_count"]
        steel_tons = closest_match["steel_tons"]
        construction_cost_inr = closest_match["cost_inr"]
        
        return jsonify({
            "sq_ft": sq_ft,
            "cement_bags": cement_bags,
            "bricks_count": bricks_count,
            "steel_tons": steel_tons,
            "construction_cost_inr": construction_cost_inr
        })
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide a valid square feet value."})




