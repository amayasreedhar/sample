from flask import Flask,render_template,request,url_for,redirect,abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/rad')
def rad():
    return render_template('radiopy.html')


@app.route('/radioval' ,methods=['POST'])
def radioval():
    a=request.form['gender']
    print(a)
    if(a=="male"):
        return  render_template('radiopy.html',m="male")
    else:
        return render_template('radiopy.html', m="female")



@app.route('/check')
def check():
    return render_template('checkboxpy.html')

@app.route('/checkbox', methods=['POST'])
def checkbox():
    a=request.form.getlist('vehicle')
    j=",".join(a)

    print(j)

    return render_template('checkboxpy.html',m=j)


@app.route('/drop')
def drop():
    return render_template('dropdownpy.html')

@app.route('/dropdown', methods=['POST'])
def dropdown():
    a=request.form['country']
    return render_template('dropdownpy.html',m=a)

@app.route('/text')
def text():
    return render_template('textboxpy.html')
@app.route('/textbox',methods=['POST'])
def textbox():
    a=request.form['t2']
    return render_template('textboxpy.html',m=a)

@app.route('/register')
def register():
    return render_template('registrationformpy.html')
@app.route('/registration',methods=['POST'])
def registration():

 @app.route('/image')
 def image():
    return render_template('imagepy.html')
@app.route('/img',methods=['POST'])
def img():
    a = request.form['uname']
    b = request.form['adr']
    c = request.form['age']
    d = request.form['gen']
    e = request. form['num']
    f = request.form['email']
    g = request.form['dist']
    h = request.form['qual']
    aq = request.form.getlist('python')
    i = ",".join(aq)
    j = request.form['user']
    k = request.form['pwrd']
    l = request.form['cpd']
    m = request.form['sub']
    return render_template('profilepy.html',m1=a,m2=b,m3=c,m4=d,m5=e,m6=f,m7=g,m8=h,m9=i,m10=j,m11=k,m12=l,m13=m)
    a=request.files['t2']
    a.save("C:\\Users\\Amaya\\PycharmProjects\\sample\\static\\img\\"+a.filename)
    path="/static/img/"+a.filename

    return render_template("imagepy.html",m=path)




@app.route('/image1')
def imgag1():
    return render_template('imageregistpy.html')
@app.route('/image2',methods=['POST'])
def image2():
    a1=request.files['f1']
    a1.save("C:\\Users\\Amaya\\PycharmProjects\\sample\\static\\imageregform\\"+a1.filename)
    path="/static/imageregform/"+a1.filename
    a = request.form['uname']
    b = request.form['adr']
    c = request.form['age']
    d = request.form['gen']
    e = request.form['num']
    f = request.form['email']
    g = request.form['dist']
    h = request.form['qual']
    aq = request.form.getlist('python')
    i = ",".join(aq)
    j = request.form['user']
    k = request.form['pwrd']
    l = request.form['cpd']
    m = request.form['sub']


    return render_template('imageprofile.py.html', m1=a, m2=b, m3=c, m4=d, m5=e, m6=f, m7=g, m8=h, m9=i, m10=j, m11=k, m12=l,m13=m,m14=path)

@app.route("/a/<v>/<m>")
def url1(v,m):
    i=int(v)
    j=int(m)
    c=i+j
    w=str(c)
    return ("add"+w)

@app.route('/multtable')
def multtable():
    return render_template('multiplicationtablepy.html')

@app.route('/multtablebutton')
def multtablebutton():
    return render_template('buttonmultablepy.html',p=0)

@app.route('/buttonmul',methods=['POST'])
def buttonmul():
    return render_template('buttonmultablepy.html',p=5)




@app.route('/txtbuttonmul')
def txtbuttonmul():
    return render_template('multxtbuttonpy.html',c=0)
@app.route('/multxt',methods=['post'])
def multxt():
    a = request.form['t1']
    d=int(a)
    return render_template('multxtbuttonpy.html',c=d)



@app.route("/redirct1")
def d1():
    return "hallo"

@app.route('/d1')
def ad1():
    return "kitty"
@app.route("/redirect")
def ab():
    return render_template("textareapy.html")
@app.route("/ab",methods=['POST'])
def c():
    w = request.form['t2']
    print(w)

    if w =="a":

        return redirect(url_for('d1'))
    elif w == "b" :
        return abort(401)








if __name__ == '__main__':
    app.run(debug=True,port=5500)
