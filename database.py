from sqlalchemy import create_engine, text

#the parameters for this are a template to connect to a database through msql/mariadb that can be found
#here: https://docs.sqlalchemy.org/en/20/dialects/mysql.html, along with the rest of the information on
#how to set up a database using sqlalchemy. You can see from the mysql+pymysql that we need to 
#install the pymysql library to use as a connector.
db_connection_string = "mysql+pymysql://4l58fwwryik8xfzu5exu:pscale_pw_t7Dua0RMOBQz9u47UNb8RVXzHaDcvg1AnYje2lxOdA9@aws.connect.psdb.cloud/flask_test?charset=utf8mb4"

#information found in the ssl secion of https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mysqldb-ssl,
#you need to replace the ca section with the one found in planetscale.coms args.
engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl" : {
                            "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

with engine.connect() as conn:
  result = conn.execute(text('select * from jobs'))
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all())", type(result_all))
  print("result", result_all)