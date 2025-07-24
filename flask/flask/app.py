from flask import Flask

''' It creates an instance of the Flask class wbich will be your Wsgi (WEB SERVER GATEWAY INTERFACE)Application '''
## wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to this best flask course,This should be an amazing course" 
@app.route("/index")
def index():
    return "welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)
