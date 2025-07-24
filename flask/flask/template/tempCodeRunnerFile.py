### building url dynamically 
### jinja 2 Template Engine
## jinja 2 template engine 
from flask import Flask,render_template,request

''' It creates an instance of the Flask class wbich will be your Wsgi (WEB SERVER GATEWAY INTERFACE)Application '''
## wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1> Welcome to the flask course </H1></html>" 
@app.route("/index",methods=['GET'])
def index():
    return render_template('index1.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
## variable rule
@app.route('/sucess/<int:score>')
def sucess(score):
    res =""
    if score>=50:
        res="PASS"
    else:
        res="Fail"
    
    return render_template('result.html',results=res)    

if __name__=="__main__":
    app.run(debug=True)