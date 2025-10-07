from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#add-data 
@app.route('/add-data', methods=['GET'])
def add_data_get():
    return render_template("addData.html")

@app.route('/add-data', methods=['POST'])
def add_data_post():
    return render_template("addData.html")

#practice
@app.route('/practice', methods=['GET'])
def practice_get():
    return render_template("practice.html")

@app.route('/practice', methods=['POST'])
def practice_post():
    return render_template("practice.html")

if __name__ == '__main__':
    app.run(debug=True)
    