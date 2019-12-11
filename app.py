from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

# Set up the database based on which environment we are running the application 
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/group4'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://prvhdzhzdaadhk:e75581f4cbaf8b6f3a27bf4520cbfbdeee87c2c67417f08f6fdb46545528677f@ec2-174-129-255-46.compute-1.amazonaws.com:5432/d7bu0hmdgsbgpf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# object we will use to query the db
db = SQLAlchemy(app)

# db model for user
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.column = db.Column(db.String(250), unique=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    password = db.Column(db.String(200))

    # constructor for user model 
    def __init__(self, email, firstName, lastName, password):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password


# db model for product
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.column = db.Column(db.String(250), unique=True)
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)    

    # constructor for product model 
    def __init__(self, name, description, category, price):
        self.name = name
        self.description = description
        self.category = category
        self.price = price

# db model for Cart
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    userID = db.column = db.Column(db.Integer, unique=True)
    price = db.Column(db.Float)

    # constructor for cart model 
    def __init__(self, userID, price):
        self.userID = userID
        self.price = price

# db model for a Cart Item
class CartItem(db.Model):
    __tablename__ = 'cartItem'
    id = db.Column(db.Integer, primary_key=True)
    productID = db.Column(db.Integer)
    cartID = db.Column(db.Integer)
    date = db.Column(db.DateTime)   

    # constructor for cartItem model 
    def __init__(self, productID, description, cartID, date):
        self.productID = productID
        self.cartID = cartID
        self.date = date


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields.')

        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()

            # send confirmation email 
            send_mail(customer, dealer, rating, comments)

            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback.')


if __name__ == '__main__':
    app.run()