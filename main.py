from flask import Flask,render_template,request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from werkzeug import secure_filename
import os
import json
import math
from datetime import datetime

#The below json function is use to store values that can be changed by user'"


with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)

app.config['UPLOAD_FOLDER']= params['upload_file']
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
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    '''pagination login if page is first prev=0 next=current+1
    if page is middle prev=current-1,next=current+1
    if page is last prev=current-1 ,next=0'''

    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif (page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    return render_template("index.html", params=params, posts = posts, prev=prev, next=next)


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

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "Uploaded Successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/login")

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/login")



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
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = req_title
                post.sub = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)

        post = Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html", params=params, post=post, sno=sno)





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



if __name__ == '__main__':
    app.run(debug=True)