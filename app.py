from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]
    
@app.route("/")
def homepage():
  name = "Ryan Rodriguez"
  details = readDetails('static/details.txt')
  return render_template("homepage.html", name=name, aboutMe = details)

@app.route('/greet/<name>')
def greet(name):
  return f'<h1> Hello there, {name} </h1>'

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']

    return render_template('form.html', name=name)
  
if __name__ == "__main__":
  app.run(debug=True, port=2000)