from flask import Flask, render_template, url_for, request
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
@app.route('/login', methods=['GET', 'POST'])
def login()
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'Eddie' or request.form['username'] != 'Jasper' or request.form['password'] != 'admin':
			error = "Invalid User Credentials. Please try again."
		else:
			return redirect(url_for('welcome"))
	return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)