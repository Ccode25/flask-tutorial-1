from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Manila, Philippines',
    'salary': 'PHP80,3000'
  },
  {
    'id': 2,
    'title': 'QA Tester',
    'location': 'CALABARZON, Philippines',
    'salary': 'PHP40,3000'
  },
  {
    'id': 1,
    'title': 'Software Develover',
    'location': 'Manila, Philippines',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs = JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0',debug=True)