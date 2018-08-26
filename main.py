from flask import Flask,render_template,request, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime

#The below json function is use to store values that can be changed by user'"


with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

#The Below function mail is used to send mail

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = '!Tj13is009'
)
mail=Mail(app)

#The below local server is used to acess Data baee using sqlalchemy

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sno Name email phone msg date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(12), nullable=True)

#the above contacts is used to store the values and send to data base

class Posts(db.Model):
    '''
    sno title , sub,slug content, img_file  date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    sub = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)
    date= db.Column(db.String(12),  nullable=True)

#the above post is used to store the values and send to data base

@app.route("/")
def Home():
    posts = Posts.query.filter_by().all()
    return render_template("index.html", params=params, posts = posts)


@app.route("/login", methods = ['GET', 'POST'])
def login():

    #if the user is in the session
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts=posts)


    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if (username == params['admin_user'] and password == params['admin_password']):
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html", params=params, posts=posts)
            #creating sessin variable


    return render_template("login.html", params=params)


@app.route("/post/<string:post_slug>", methods = ['GET'])
def post_route(post_slug):

    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template("post.html", params=params, post=post)

@app.route("/about")
def about():
    return render_template("about.html", params=params)

#to send the contact details to the database the GET and POST method is used.

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            req_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if sno =='0':
                post = Posts(title=req_title, sub=tline, slug=slug, content=content, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()

        return render_template("edit.html", params=params, sno=sno)





@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Adding Entry to the Data base'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry = Contacts(name = name, email = email, phone = phone, date=datetime.now(), msg = message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New messaage from blog sender is '+ name,
                          sender = email,
                          recipients = [params['gmail_user']],
                          body = message + '\n' + phone + '\n''\n''\n' + email)

    return render_template("contact.html", params=params)

# I have slug using string in the code to fetch from the database




app.run(debug=True)