from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
#    return 'hello'
    return render_template('hello.html') 

if __name__ == "__main__":
    app.run()
