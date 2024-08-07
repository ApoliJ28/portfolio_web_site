from flask import Flask, render_template, request, redirect, url_for
from src.controller_mail import send_mail

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/contact", methods=['POST'])
def contact():
    name = request.form.get('name')
    mail = request.form.get('email')
    msg = request.form.get('message')
    if name and mail and msg:
        send_mail(name=name, mail=mail, msg=msg)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=True)