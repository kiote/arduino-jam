from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import serial

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def hello():
  if request.method == 'POST':
    ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
    print request.form["hours"]
    ser.write(str(request.form["hours"]))
  
  return render_template('hello.html') 

if __name__ == "__main__":
  app.run()
