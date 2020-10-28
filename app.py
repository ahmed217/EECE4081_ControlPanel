from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask, render_template, redirect, url_for, request

# install using,  pip3 install sqlalchemy flask-sqlalchemy 
from flask_sqlalchemy import SQLAlchemy





database = "sqlite:///controlpanel.db"


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database

db = SQLAlchemy(app)

##################################################
# use python shell to create the database (from inside the project directory) 
# >>> from app import db
# >>> db.create_all()
# >>> exit()
###################################################
##############################################
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

##############################################


@app.route('/')
def index():
    #brokenlaptops = BrokenLaptop.query.all()
    room = Room()
    course = Course()
    instructor = Instructor()
    timeslot = TimeSlot()
    
    return render_template("index.html", rooms = room.getRooms(), courses = course.getCourses(), 
                           instructors = instructor.getInstructors(), timeslots = timeslot.getTimeSlots(),title='Control Panel')
    


# @app.route('/create', methods=['GET','POST'])
# def create():
#     if request.form:
#         brand = request.form.get("brand")
#         price = request.form.get("price")
#         brokenlaptop = BrokenLaptop(brand=brand,price=price)
#         db.session.add(brokenlaptop)
#         db.session.commit()
#         return redirect("/")   
#     
#     #brokenlaptops = BrokenLaptop.query.all()
#     #return render_template("create.html",brokenlaptops=brokenlaptops)
#     return render_template("create.html")


# @app.route('/delete/<laptop_id>') # add id
# def delete(laptop_id):
#     brokenlaptop = BrokenLaptop.query.get(laptop_id)
#     if brokenlaptop is None:
#         return "this many broken laptops are not there"
#     db.session.delete(brokenlaptop)
#     db.session.commit()
#     
#     return redirect("/")
# 
#     #brokenlaptops = BrokenLaptop.query.all()
#     #return render_template('delete.html', brokenlaptops=brokenlaptops )
# 
# @app.route('/update/<laptop_id>', methods=['GET','POST']) # add id 
# def update(laptop_id):
#     if request.form:
#         newbrand = request.form.get('brand')
#         newprice = request.form.get('price')
#         brokenlaptop = BrokenLaptop.query.filter_by(id=laptop_id).first()
#         brokenlaptop.brand = newbrand
#         brokenlaptop.price = newprice
#         db.session.commit()
#         
#         return redirect("/")
#     brokenlaptop = BrokenLaptop.query.filter_by(id=laptop_id).first()
#     return render_template('update.html', brokenlaptop = brokenlaptop)
# 
# class BrokenLaptop(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     brand = db.Column(db.String(40), nullable = False)
#     price = db.Column(db.Float, nullable = True)

class Room():
    def __init__(self):
        self.rooms = ['ES 220', 'ES 230','ET 140']
        
    def getRooms(self):
        return self.rooms

class Instructor():
    def __init__(self):
        self.instructors = ['Dr. Zack Pendley', 'Dr. Mamadou Ba']
        
    def getInstructors(self):
        return self.instructors

class TimeSlot():
    def __init__(self):
        self.timeslots = ['M,W,F 9:00 - 10:00', 'M,W,F 11:00 - 12:00','TR 10:00 - 11:00']
        
    def getTimeSlots(self):
        return self.timeslots

class Course():
    def __init__(self):
        self.courses = ['EECE 4081-001', 'EECE 4278-001','EECE 2201-002','EECE 3213-002']
        
    def getCourses(self):
        return self.courses
    

if __name__ == '__main__':
    app.run(debug=True)
