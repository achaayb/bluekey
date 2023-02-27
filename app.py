import string
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime
from sqlalchemy import Integer, Enum
import enum
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Crypters(db.Model):
    __tablename__ = 'crypters'
    id = db.Column(db.String, primary_key=True, default=get_random_string(6))
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

class Remotes(db.Model):
    __tablename__ = 'remotes'
    id = db.Column(db.String, primary_key=True, default=get_random_string(6))
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

class Exploits(db.Model):
    __tablename__ = 'exploits'
    id = db.Column(db.String, primary_key=True, default=get_random_string(6))
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

#################### CRYPTERS

@app.route('/crypters/', methods=["POST", "GET"])
def viewCrypter():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        new_product = Crypters(product_name=product_name, product_image=product_image, product_description=product_description)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/crypters/")

        except:
            crypters = Crypters.query.order_by(Crypters.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        crypters = Crypters.query.order_by(Crypters.date_created).all()
        return render_template("crypters.html", crypters=crypters)

@app.route("/delete-crypter/<name>")
def deleteProduct(name):
    product_to_delete = Crypters.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/crypters/")
    except:
        return "There was an issue while deleteing the Product"

#################### CRYPTERS

#################### EXPLOITS

@app.route('/exploits/', methods=["POST", "GET"])
def viewExploit():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        new_product = Exploits(product_name=product_name, product_image=product_image, product_description=product_description)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/exploits/")

        except:
            exploits = Exploits.query.order_by(Exploits.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        exploits = Exploits.query.order_by(Exploits.date_created).all()
        return render_template("exploits.html", exploits=exploits)

@app.route("/delete-exploit/<name>")
def deleteExploit(name):
    product_to_delete = Exploits.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/exploits/")
    except:
        return "There was an issue while deleteing the Product"

#################### EXPLOITS

#################### REMOTES

@app.route('/remotes/', methods=["POST", "GET"])
def viewRemote():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        new_product = Remotes(product_name=product_name, product_image=product_image, product_description=product_description)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/remotes/")

        except:
            remotes = Remotes.query.order_by(Remotes.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        remotes = Remotes.query.order_by(Remotes.date_created).all()
        return render_template("remotes.html", remotes=remotes)

@app.route("/delete-remote/<name>")
def deleteRemote(name):
    product_to_delete = Remotes.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/remotes/")
    except:
        return "There was an issue while deleteing the Product"

#################### CRYPTERS


if (__name__ == "__main__"):
    app.run(debug=True)
