from flask import Flask, render_template

app = Flask(__name__)

#Gives a route to the app, just a / indicates the default home page.
@app.route("/")
def hello_world():
  return render_template('home.html')#imported seperatley at the top, render template is how we will display html files.

#simpler way to have the file run
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)

