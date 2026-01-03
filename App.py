from datetime import datetime
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

# my App
App = Flask(__name__)
Scss(App)

App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskmanagerapp.db"
App.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(App)

# Data
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}"


    with App.app_context():
        db.create_all()

# Routes

# LandingPage
@App.route("/", methods=["POST","GET"])
def index():
# Add to list
    if request.method == "POST":
        current_task = request.form['content']
        new_task = Task(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    
    #Fetch all current tasks
    else: 
        tasks = Task.query.order_by(Task.created).all()
        return render_template("index.html", tasks=tasks)

# Delete a task
@App.route("/delete/<int:id>")
def delete(id:int):
    delete_task = Task.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"

# Edit a task
@App.route("/edit/<int:id>", methods=["POST","GET"])
def edit (id:int):
    task_to_edit = Task.query.get_or_404(id)
    if request.method == "POST":
        task_to_edit.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return render_template("edit.html", task=task_to_edit)


if __name__ == "__main__":
    App.run(debug=True)