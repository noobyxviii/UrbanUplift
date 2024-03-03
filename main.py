from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/43211')
def fourthreetwooneone():
  return render_template("43211.html")

@app.route('/2576')
def twofifvesevensix():
  return render_template("2576.html")

app.run(host='0.0.0.0', port=8080)
