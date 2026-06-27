from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():

    username = request.form.get('username')
    phone = request.form.get('phone')

    return render_template("Success_register.html")

if __name__ == '__main__':
    app.run(debug=True)