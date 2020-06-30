from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
#connect to the database
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:********@localhost/heightcollector'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://kiefwwctcaimxt:0c54e114d02157206002c6b9112494f0412b43c0eedeaa43a2ea16db61b5c3f9@ec2-50-19-26-235.compute-1.amazonaws.com:5432/do06tce60p2hh?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'heightdata'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String,unique=True)
    height = db.Column(db.Integer)
    
    def __init__(self, email,height):
        self.email = email
        self.height = height
        
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=["POST"])
def success():
    if request.method == 'POST':
        email = request.form['email']
        height = request.form['height']
        
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            newData = Data(email, height)
            db.session.add(newData)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height,1)
            count = db.session.query(Data.height).count()
            send_email(email, height,average_height,count)
            return render_template("success.html")
        return render_template("index.html",text="Email alreay exists!")
if __name__ == "__main__":
    app.run()

