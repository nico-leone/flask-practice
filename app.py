from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

#Gives a route to the app, just a / indicates the default home page.
@app.route("/")
def hello_world():#here we pass the information stored in JOBS through the arg
  
  jobs = load_jobs_from_db()#rather than the hardcoded list, we are now pulling the jobs from the database.
  return render_template('home.html', jobs=jobs)#imported seperatley at the top, render template is how we will display html files.

@app.route("/api/jobs")
def list_jobs():
  jobs = dict(load_jobs_from_db())
  return jsonify(jobs);

#putting id in <id> creates a dynamic route. URL passes the id through so we can call load_job_from_db to get the info we need to load the page.
@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)#because load_job_from_db returns none if there is no row for certain id
  if not job:              #we can say if not job, and if there was no row it will return an error.
    return "Not Found", 404
  return render_template('jobpage.html', job = job)


#simpler way to have the file run
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)

