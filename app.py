
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import joblib
import os

app = Flask(__name__)
app.secret_key = "multidisease_secret_key"

DATABASE = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

create_table()

def load_optional(path):
    try:
        return joblib.load(path)
    except Exception:
        return None

diabetes_model = load_optional("models/diabetes.pkl")
diabetes_scaler = load_optional("models/diabetes_scaler.pkl")
heart_model = load_optional("models/heart.pkl")
heart_scaler = load_optional("models/heart_scaler.pkl")
cancer_model = load_optional("models/cancer.pkl")
cancer_scaler = load_optional("models/cancer_scaler.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        conn=get_db(); cur=conn.cursor()
        cur.execute("SELECT id FROM users WHERE email=?",(email,))
        if cur.fetchone():
            flash("Email already exists")
            conn.close()
            return redirect(url_for("register"))
        cur.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)",(name,email,password))
        conn.commit(); conn.close()
        flash("Registration successful")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"]; password=request.form["password"]
        conn=get_db(); cur=conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?",(email,password))
        user=cur.fetchone(); conn.close()
        if user:
            session["user"]=user["name"]
            session["email"]=user["email"]
            return redirect(url_for("dashboard"))
        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", name=session["user"])

def predict_page(template, model, scaler, disease, positive, negative):

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        try:
            if model is None:
                flash(f"{disease} model not found.")
                return render_template(template)

            features = [float(v) for v in request.form.values()]

            if scaler is not None:
                features = scaler.transform([features])
            else:
                features = [features]

            pred = model.predict(features)[0]

            if int(pred) == 1:
                prediction = positive
            else:
                prediction = negative

            return render_template(
                "result.html",
                disease=disease,
                prediction=prediction
            )

        except Exception as e:
            flash(f"Prediction Error: {e}")
            return render_template(template)

    return render_template(template)
    

@app.route("/diabetes", methods=["GET","POST"])
def diabetes():
    return predict_page("diabetes.html", diabetes_model, diabetes_scaler, "Diabetes", "Diabetic", "Not Diabetic")

@app.route("/heart", methods=["GET","POST"])
def heart():
    return predict_page("heart.html", heart_model, heart_scaler, "Heart Disease", "Heart Disease Detected", "Healthy")

@app.route("/cancer", methods=["GET","POST"])
def cancer():
    return predict_page("cancer.html", cancer_model, cancer_scaler, "Breast Cancer", "Malignant", "Benign")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out")
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
