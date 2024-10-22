from flask import Flask, render_template

app = Flask(__name__)

FILES = [
    {'id': 1,
     'title': 'student1.py'},
    {'id': 2,
     'title': 'student2.py'},
    {'id': 3,
     'title': 'student3.py'}
]

@app.route("/")
def hello():
    return render_template("home.html", files=FILES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)