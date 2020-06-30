from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#connect to the database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Qwert12345~!@localhost/heightcollector'
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
            return render_template("success.html")
        return render_template("index.html",text="Email alreay exists!")
if __name__ == "__main__":
    app.run()

