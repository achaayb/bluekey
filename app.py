import string
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
from datetime import datetime
from sqlalchemy import Integer, Enum
from flask_migrate import Migrate
import enum
import random

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Crypters(db.Model):
    __tablename__ = 'crypters'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

class Remotes(db.Model):
    __tablename__ = 'remotes'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id

class Exploits(db.Model):
    __tablename__ = 'exploits'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    product_image = db.Column(db.String(50000))
    product_description = db.Column(db.String(10000)) 
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.id


@app.route('/backoffice/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

#################### CRYPTERS

@app.route('/backoffice/crypters/', methods=["POST", "GET"])
def viewCrypter():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        price = request.form["price"]
        price = int(price)
        new_product = Crypters(product_name=product_name, product_image=product_image, product_description=product_description,price=price)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/backoffice/crypters/")

        except:
          
            crypters = Crypters.query.order_by(Crypters.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        crypters = Crypters.query.order_by(Crypters.date_created).all()
        return render_template("crypters.html", crypters=crypters)

@app.route("/backoffice/delete-crypter/<name>")
def deleteProduct(name):
    product_to_delete = Crypters.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/backoffice/crypters/")
    except:
        return "There was an issue while deleteing the Product"

#################### CRYPTERS

#################### EXPLOITS

@app.route('/backoffice/exploits/', methods=["POST", "GET"])
def viewExploit():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        price = request.form["price"]
        new_product = Exploits(product_name=product_name, product_image=product_image, product_description=product_description,price=price)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/backoffice/exploits/")

        except:
            exploits = Exploits.query.order_by(Exploits.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        exploits = Exploits.query.order_by(Exploits.date_created).all()
        return render_template("exploits.html", exploits=exploits)

@app.route("/backoffice/delete-exploit/<name>")
def deleteExploit(name):
    product_to_delete = Exploits.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/backoffice/exploits/")
    except:
        return "There was an issue while deleteing the Product"

#################### EXPLOITS

#################### REMOTES

@app.route('/backoffice/remotes/', methods=["POST", "GET"])
def viewRemote():
    if (request.method == "POST") and ('product_name' in request.form):
        product_name = request.form["product_name"]
        product_image = request.form["product_image"]
        product_description = request.form["product_description"]
        price = request.form["price"]
        new_product = Remotes(product_name=product_name, product_image=product_image, product_description=product_description,price=price)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect("/backoffice/remotes/")

        except:
            remotes = Remotes.query.order_by(Remotes.date_created).all()
            return "There Was an issue while add a new Product"
    else:
        remotes = Remotes.query.order_by(Remotes.date_created).all()
        return render_template("remotes.html", remotes=remotes)

@app.route("/backoffice/delete-remote/<name>")
def deleteRemote(name):
    product_to_delete = Remotes.query.get_or_404(name)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/backoffice/remotes/")
    except:
        return "There was an issue while deleteing the Product"

#################### Order

@app.route('/order/')
@app.route('/order/home')
def home():
    return render_template('Order/index.html')

@app.route('/order/crypters')
def crypters():
    crypters = Crypters.query.order_by(Crypters.date_created).all()
    return render_template('Order/index.php?rp=%2Fstore%2Fcrypters.html',crypters=crypters)

@app.route('/order/silent office')
def silent():
    exploits = Exploits.query.order_by(Exploits.date_created).all()
    return render_template('Order/cart.php?a=confproduct&i=15&language=ukranian.html',exploits=exploits)


@app.route('/order/remote administrator')
def remote():
    
    remotes = Remotes.query.order_by(Remotes.date_created).all()
    return render_template('Order/index.php?rp=%2Fstore%2Fremote-administrator-tool.html',remotes=remotes)



if (__name__ == "__main__"):
    app.run(debug=True)
