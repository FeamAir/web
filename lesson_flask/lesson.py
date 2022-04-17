from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/avr_data")
def get_avr_data():
    with open("hw.csv", "r") as f:
        a = f.readlines()[1:][:-1]
        lst = []
        ht = lst.append(sum([float(i.split(",")[1]) for i in a])
                        * 2.54 / len(a))
        wt = lst.append(sum([float(i.split(",")[2]) for i in a])
                        * 0.4535 / len(a))
        return render_template("std/get_add.html", stds=lst)

@app.route("/requirements")
def get_requirements():
    with open("requirements.txt","r", encoding="utf-16") as file:
        my_txt = file.readlines()
        return render_template("std/requirements.html", docs=my_txt)

if __name__ == '__main__':
    app.run(debug=True)