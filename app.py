from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'name':'user1'
  },
  {
    'id':2,
    'name':'user2'
  },
  {
    'id':3,
    'name':'user3'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/users")
def list_users():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
