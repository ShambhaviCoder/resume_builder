from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"
db = SQLAlchemy(app)

class PersonalInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(20), nullable=False)
    gpa = db.Column(db.Float, nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), nullable=False)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    return render_template("personal_info.html")

@app.route("/submit_personal_info", methods=["POST"])
def submit_personal_info():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    personal_info = PersonalInfo(first_name=first_name, last_name=last_name, email=email, phone=phone)
    db.session.add(personal_info)
    db.session.commit()
    return redirect(url_for("education"))

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/submit_education", methods=["POST"])
def submit_education():
    degree = request.form["degree"]
    institution = request.form["institution"]
    duration = request.form["duration"]
    gpa = request.form["gpa"]
    education = Education(degree=degree, institution=institution, duration=duration, gpa=gpa)
    db.session.add(education)
    db.session.commit()
    return redirect(url_for("skill"))

@app.route("/skill")
def skill():
    return render_template("skill.html")

@app.route("/submit_skill", methods=["POST"])
def submit_skill():
    skill_name = request.form["skill_name"]
    level = request.form["level"]
    skill = Skill(skill_name=skill_name, level=level)
    db.session.add(skill)
    db.session.commit()
    return redirect(url_for("experience"))

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/submit_experience", methods=["POST"])
def submit_experience():
    company = request.form["company"]
    position = request.form["position"]
    duration = request.form["duration"]
    description = request.form["description"]
    experience = Experience(company=company, position=position, duration=duration, description=description)
    db.session.add(experience)
    db.session.commit()
    return redirect(url_for("project"))

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/submit_project", methods=["POST"])
def submit_project():
    project_name = request.form["project_name"]
    description = request.form["description"]
    link = request.form["link"]
    project = Project(project_name=project_name, description=description, link=link)
    db.session.add(project)
    db.session.commit()
    return redirect(url_for("summary"))

@app.route("/summary")
def summary():
    personal_info = PersonalInfo.query.all()
    education = Education.query.all()
    skills = Skill.query.all()
    experiences = Experience.query.all()
    projects = Project.query.all()
    return render_template("summary.html", personal_info=personal_info, education=education, skills=skills, experiences=experiences, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)