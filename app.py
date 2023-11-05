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
		iv = bleed(iv,item),
		item = item)

#孵化個体シミュレータ
def bleed(iv,item):
	bleed_iv = [None for _ in range(6)]
	a = 0
	count = 3
	if (item[0][0] == item[1][0]) and item[0][0] == "パ"  and item[1][0] == "パ": #両親ともにパワー系アイテムなら
		tmp = rm.randint(0,1)
		count -= 1
		if tmp == 1:
			a = 6
		bleed_iv[itemidx(item[tmp])] = iv[itemidx(item[tmp]) + a]
	elif item[0][0] == "パ":
		bleed_iv[itemidx(item[0])] = iv[itemidx(item[0])]
		count -= 1
	elif item[1][0] == "パ":
		bleed_iv[itemidx(item[1])] = iv[itemidx(item[1])+6]
		count -= 1
		
	if "あかいいと" in item:
		count += 2

	idx = getidx(bleed_iv)#修正できそう
	for i in range(count):
		tmp = rm.sample(idx,1)[0]
		bleed_iv[tmp] = iv[tmp + (6 * rm.randint(0,1))]


	return bleed_iv

def itemidx(item): #パワー系アイテムを添え字に変換
	if item == "パワーウエイト(H)":
		n = 0
	elif item == "パワーリスト(A)":
		n = 1
	elif item == "パワーベルト(B)":
		n = 2
	elif item == "パワーレンズ(C)":
		n = 3
	elif item == "パワーバンド(D)":
		n = 4
	elif item == "パワーアンクル(S)":
		n = 5
	else:
		n = -1
	if n >= 0:
		return n
	else:
		return None

def getidx(iv): #リスト内でNoneが格納されているidxをリストで返す
	idx = []
	for i in range(6):
		if iv[i] == None:
			idx.append(i)
	return idx	
	
def power_item(item):
	a = 0
	if item[0][0] == item[1][0]:
		tmp = rm.randint(0,1)
		if tmp == 1:
			a = 6
		return 

if __name__ == '__main__':
	app.run(debug=True)