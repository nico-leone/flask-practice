from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id' : 1,
  'title' : 'Imposter',
  'location' : 'Medbay',
  'salary' : '$ 35'
}, 
  {
  'id' : 2,
  'title' : 'Crewmate',
  'location' : 'Engine',
}, 
  {
  'id' : 3,
  'title' : 'Imposter',
  'location' : 'Comms',
  'salary' : '$ 35'
}

  
]

#Gives a route to the app, just a / indicates the default home page.
@app.route("/")
def hello_world():                    #here we pass the information stored in JOBS through the arg
  return render_template('home.html', jobs=JOBS)#imported seperatley at the top, render template is how we will display html files.

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS);

#simpler way to have the file run
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)

