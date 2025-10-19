from flask import Flask, render_template, url_for

app = Flask(__name__)

def abc(p1, p2):
    return p1 + p2

def abc1(p1, p2):
    try:
        return int(p1) + int(p2)
    except ValueError:
        return None

@app.route("/")
def home():
    return render_template("index.html", title="หน้าแรก | Flask Starter")


@app.route("/Tech")
def Tech():
    return render_template("Tech.html", title="เกี่ยวกับเทคโนโลยี | Flask Starter")

@app.route("/MyID")
def MyID():
    return render_template("MyID.html", title="MyID | Flask Starter")

@app.route("/draw")
def draw():
    return render_template("draw.html", title="draw | Flask Starter")

@app.route('/concat/<para1>/<para2>')
def concat(para1, para2):
    result = abc(para1, para2)
    return f"The result of concatenate between '{para1}' and '{para2}' is '{result}'"

@app.route('/sum/<para3>/<para4>')
def sumt(para3, para4):
    sum_result = abc1(para3, para4)
    if sum_result is None:
        return "You are using miss data type for operation"
    else:
        return f"The result of sum between '{para3}' and '{para4}' is '{sum_result}'"

if __name__ == "__main__":
   
    app.run(host='0.0.0.0',debug=True)
