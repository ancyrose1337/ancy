from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# --------------------
# USER TABLE
# --------------------
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    mobile = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))  # farmer / vendor


# --------------------
# PRODUCT TABLE
# --------------------
class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer)

    name = db.Column(db.String(100))
    quantity = db.Column(db.String(50))
    price = db.Column(db.String(50))
    location = db.Column(db.String(100))


# --------------------
# ORDER TABLE
# --------------------
class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer)

    quantity = db.Column(db.String(50))
    status = db.Column(db.String(50))


# --------------------
# TRANSPORT TABLE
# --------------------
class Transport(db.Model):

    __tablename__ = "transport"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer)

    vehicle = db.Column(db.String(100))
    driver = db.Column(db.String(100))
    contact = db.Column(db.String(20))

    status = db.Column(db.String(50))
