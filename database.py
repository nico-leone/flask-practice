#this file pretty much just acts as a connector to the database.
from sqlalchemy import create_engine, text
import os#for use in secrets

#the parameters for this are a template to connect to a database through msql/mariadb that can be found
#here: https://docs.sqlalchemy.org/en/20/dialects/mysql.html, along with the rest of the information on
#how to set up a database using sqlalchemy. You can see from the mysql+pymysql that we need to 
#install the pymysql library to use as a connector.
db_connection_string = os.environ['DC_CONNECTION_STRING']#method for secret password

#information found in the ssl secion of https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mysqldb-ssl,
#you need to replace the ca section with the one found in planetscale.coms args.
engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl" : {
                            "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })


#function to load the jobs from the database, comments throughout explain.
def load_jobs_from_db():
  #here we connect with the engine
  with engine.connect() as conn:
  #this function makes an sql call and stores the return in the "result"
    result = conn.execute(text('select * from jobs'))

  #iterate through the rows returned by the above statement, converting them to dicts and storing them in the array.
    jobs = []#list of dictionaries.
    for row in result.all():
      #here we convert the sql row into a python dict, a type of data structure that stores value name and value.
      jobs.append(row._mapping)
    return jobs#returns the list of dictionaries.

#new funciton to get a specific job
def load_job_from_db(id):
  with engine.connect() as conn:
    #new sql statement that gets a specific jobs info based off of the id inputted
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
    
    row = result.fetchone()
    if row is None:
      return None
    else:
      return row._mapping
  