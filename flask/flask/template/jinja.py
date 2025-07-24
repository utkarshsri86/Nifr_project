### building url dynamically 
### jinja 2 Template Engine
## jinja 2 template engine 
## jinja2 template template engine 
'''
{{}} expression to print output to html
{%...%}  condition , for loop , if
{#...#} this is for comment 

'''
from flask import Flask,render_template,request
from flask import render_template

''' It creates an instance of the Flask class wbich will be your Wsgi (WEB SERVER GATEWAY INTERFACE)Application '''
## wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1> Welcome to the best flask course </H1></html>" 
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
## variable rule
@app.route('/sucessres/<int:score>')
def sucessres(score):
    res =""
    if score>=50:
        res="PASSed"
    else:
        res="Failed"

    exp ={'score':score,'res':res}    
    return render_template('result1.html',results=exp)  
@app.route('/sucessif/<int:score>')
def sucessif(score):
 return render_template('result.html',results=score)  

if __name__=="__main__":
    app.run(debug=True)