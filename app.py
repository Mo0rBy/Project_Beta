from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/passenger')
def passenger():
    return render_template('passenger/passenger.html')


@app.route('/passenger/add', methods=['POST', 'GET'])
def addpassenger():
    if request.method == 'GET':
        return render_template('passenger/addpassenger.html')
    elif request.method == 'POST':
        form_data = request.form


@app.route('/passenger/remove')
def removepassenger():
    return render_template('passenger/removepassenger.html')


@app.route('/flighttrip')
def flighttrip():
    return render_template('flighttrip/flighttrip.html')


@app.route('/plane')
def plane():
    return render_template('plane/plane.html')




if __name__ == '__main__':
    app.debug = True
    app.run()
