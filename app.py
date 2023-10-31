from flask import Flask, render_template, request
import random as rm

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
	item = form.getlist("item")
	return render_template('hello.html', 
		title = 'Form Sample(post)',
		iv = bleed(iv),
		item = item)

#孵化個体シミュレータ
def bleed(iv,):
	bleed_iv = [None for _ in range(6)]
	if True:
		bleed_iv[rm.randint(0,5)] = rm.randint(0,31)
		for i in range(6):
			if bleed_iv[i] == None:
				bleed_iv[i] = iv[i + 6 * rm.randint(0,1)]
	return bleed_iv


if __name__ == '__main__':
	app.run(debug=True)