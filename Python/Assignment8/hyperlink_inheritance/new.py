from flask import Flask, render_template
import os
app = Flask(__name__)
pic_folder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = pic_folder
@app.route('/')
def first():
    pic = os.path.join(app.config['UPLOAD_FOLDER'],'waterfall.jpg')
    return render_template('home.html',user_image=pic)

@app.route('/second')
def second():
    return render_template("second.html")


@app.route('/home_index')
def inh():
    return render_template("home_index.html")

if __name__ == '__main__':
    app.run()