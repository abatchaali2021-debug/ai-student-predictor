from flask import Flask, render_template, request
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Training data
students = [
    [95, 98, 92], [90, 95, 88], [88, 90, 85],
    [85, 88, 82], [80, 85, 78], [75, 80, 70],
    [65, 70, 60], [60, 65, 55], [55, 60, 50],
    [50, 55, 45], [45, 50, 40], [40, 45, 35],
    [35, 40, 30], [30, 35, 25],
]
results = [
    "Pass","Pass","Pass","Pass","Pass","Pass","Pass",
    "Fail","Fail","Fail","Fail","Fail","Fail","Fail"
]

# Train AI when app starts
model = KNeighborsClassifier()
model.fit(students, results)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    score = int(request.form["score"])
    attendance = int(request.form["attendance"])
    assignments = int(request.form["assignments"])
    
    prediction = model.predict([[score, attendance, assignments]])[0]
    
    return render_template("result.html",
        result=prediction,
        score=score,
        attendance=attendance,
        assignments=assignments
    )

if __name__ == "__main__":
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)