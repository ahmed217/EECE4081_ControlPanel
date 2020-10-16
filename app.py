from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import re

# install using,  pip3 install sqlalchemy flask-sqlalchemy 
from flask_sqlalchemy import SQLAlchemy



database = "sqlite:///controlpanel.db"


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

##################################################
# use python shell to create the database (from inside the project directory) 
# >>> from app import db
# >>> db.create_all()
# >>> exit()
###################################################

@app.route('/')
def index():
    #brokenlaptops = BrokenLaptop.query.all()
    room = Room()
    course = Course()
    instructor = Instructor()
    timeslot = TimeSlot()
    
    schedules = Schedule.query.all()
    
    return render_template("index.html", rooms = room.getRooms(), courses = course.getCourses(), 
                           instructors = instructor.getInstructors(), timeslots = timeslot.getTimeSlots(),
                           schedules = schedules, title='Control Panel')
    
# @app.route('/add/<item>/<id>')
# def additem(item, id):
#     
#     room_text = [-1,'']
#     instruct_text = [-1,'']
#     course_text = [-1,'']
#     timeslot_text = [-1,'']
#     
#     room = Room()
#     course = Course()
#     instructor = Instructor()
#     timeslot = TimeSlot()
#     
#     int_id = int(id)
#     
#     if re.match(r'rooms',item):
#         room_text = room.getRoomById(int_id)
#         
#     if re.match(r'instructors',item):
#         instruct_text = instructor.getInstructorById(int_id)
#         
#     if re.match(r'courses',item):
#         course_text = course.getCourseById(int_id)
#         
#     if re.match(r'timeslots',item):
#         timeslot_text = timeslot.getTimeSlotById(int_id)
#     
#     
#     return render_template("index.html", room_text=room_text[1], instruct_text=instruct_text[1],
#                            course_text=course_text[1],timeslot_text=timeslot_text[1],
#                            rooms = room.getRooms(), courses = course.getCourses(), 
#                            instructors = instructor.getInstructors(), timeslots = timeslot.getTimeSlots(),title='Control Panel')
#     

@app.route('/create', methods=['GET','POST'])
def create():
    if request.form:
        room_id = request.form.get("room_id")
        room_name = request.form.get("room_name")
        
        instruct_id = request.form.get("instruct_id")
        instruct_name = request.form.get("instruct_name")
         
        course_id = request.form.get("course_id")
        course_name = request.form.get("course_name")
         
        timeslot_id = request.form.get("timeslot_id")
        timeslot_name = request.form.get("timeslot_name")
        #return request.form
     
        schedule = Schedule(room_id = room_id, room_name = room_name, instruct_id = instruct_id, instruct_name = instruct_name,
                             course_id=course_id, course_name=course_name, timeslot_id = timeslot_id, timeslot_name = timeslot_name)
         
        db.session.add(schedule)
        db.session.commit()
        return redirect("/")   
    
@app.route('/init_db')
def init_db():
    db.create_all()

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
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    room_id = db.Column(db.Integer, nullable = True)
    room_name = db.Column(db.String(100), nullable = True)
    instruct_id = db.Column(db.Integer, nullable = True)
    instruct_name = db.Column(db.String(100), nullable = True)
    course_id = db.Column(db.Integer, nullable = True)
    course_name = db.Column(db.String(100), nullable = True)
    timeslot_id = db.Column(db.Integer, nullable = True)
    timeslot_name = db.Column(db.String(100), nullable = True)




class Room():
    def __init__(self):
        self.rooms = [[0,"ES 220"], [1,"ES 230"],[2,"ET 140"]]
    
    def getRoomById(self, index ):
        return self.rooms[index]
        
    def getRooms(self):
        return self.rooms

class Instructor():
    def __init__(self):
        self.instructors = [[0,"Dr. Zack Pendley"],[1,"Dr. Mamadou Ba"]]
    
    def getInstructorById(self, index ):
        return self.instructors[index]
     
    def getInstructors(self):
        return self.instructors

class TimeSlot():
    def __init__(self):
        self.timeslots = [[0,"MWF 9:00 - 10:00"],[1,"MWF 11:00 - 12:00"],[2,"TR 10:00 - 11:00"]]
    
    def getTimeSlotById(self, index):
        return self.timeslots[index]
    
    def getTimeSlots(self):
        return self.timeslots

class Course():
    def __init__(self):
        self.courses = [[0,"EECE 4081-001"],[1,"EECE 4278-001"],[2,"EECE 2201-002"],[3,"EECE 3213-002"]]
    
    def getCourseById(self, index):
        return self.courses[index]
    
    def getCourses(self):
        return self.courses
    

if __name__ == '__main__':
    app.run(debug=True)
