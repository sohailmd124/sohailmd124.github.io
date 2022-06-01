from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/interests.html')
def interests():
    return render_template('interests.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

app.run(debug=True)