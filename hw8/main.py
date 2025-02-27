from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/countries/')
def countries():
    return render_template("countries.html")

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("thank_you.html", name=name)
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
