from flask import Flask, render_template, request, jsonify
from airport_booking_app.app_classes import Passenger, FlightTrip, Plane

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
        name = request.form["name"]
        passport_num = request.form["passportnum"]
        new_user = Passenger(name, passport_num)

        string_pas_num = "p" + str(new_user.passport_num)

        globals()[string_pas_num] = Passenger(name, passport_num)
        with open("passenger_register.txt", "a+") as register:
            register.write(string_pas_num + ", " + name + ", " + passport_num + "\n")
        return f'Passenger {globals()[string_pas_num].name} has been created with user name {string_pas_num}'


@app.route('/passenger/remove')
def removepassenger():
    return render_template('passenger/removepassenger.html')


@app.route('/flighttrip')
def flighttrip():
    return render_template('flighttrip/flighttrip.html')

@app.route('/flighttrip/add', methods=['POST', 'GET'])
def addflighttrip():
    if request.method == 'GET':
        return render_template('flighttrip/addflighttrip.html')
    elif request.method == 'POST':
        destination = request.form["destination"]

        globals()[destination] = FlightTrip(destination)
        with open("destinations_register.txt", "a+") as register:
            register.write(destination + "\n")
        return f'Flight trip {globals()[destination].destination} has been created'

@app.route('/flighttrip/addpassengertoflight', methods=['POST', 'GET'])
def addpassengertoflight():
    if request.method == 'GET':
        return render_template('flighttrip/addpassengertoflight.html')
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        passengerid = request.form["passengerid"]
        globals()[flighttrip].add_Passenger(passengerid)
        return f'Passenger {passengerid} has been added to flight {flighttrip} '

    #AttributeError: 'str' object has no  attribute 'name'

@app.route('/plane')
def plane():
    return render_template('plane/plane.html')




if __name__ == '__main__':
    app.debug = True
    app.run()

