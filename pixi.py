from flask import Flask, render_template

app = Flask(__name__)


# routers
#@app.route('/')
#def index1():
#   return 'Hello World'

 #step 2  routers

#@app.route('/whereami')
#def whereami():
#    return 'Ghana'

#@app.route('/foo/<name>')
#def foo(name):
#    return render_template('index.html', to=name)

@app.route("/")
@app.route('/index.html')
def index():
    return render_template('index.html')


#3 Start server
if __name__=='__main__':
    app.run(debug=True, host='127.0.0.1')