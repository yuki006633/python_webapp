from flask import Flask, render_template, request

app = Flask(__name__)

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	return render_template('hello.html', \
		title = 'Form Sample(get)', \
		message = '名前を入力して下さい。')

# postのときの処理
@app.route('/', methods=['POST'])
def post():
	form = request.form
	iv = form.getlist("iv")
	return render_template('hello.html', \
		title = 'Form Sample(post)', \
		iv = iv)




if __name__ == '__main__':
	app.run(debug=True)