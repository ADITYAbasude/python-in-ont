from flask import Flask
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/")  
def aditya():
    return "hello world",'www.homepage.html'
    
app.run