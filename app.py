from flask import Flask, render_template, request
from airport_booking_app.app_classes import Passenger, FlightTrip, Plane

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/passenger')
def passenger():
    with open("passenger_register.txt", "r") as file:
        content = file.read()
    return render_template('passenger/passenger.html', content=content)


@app.route('/passenger/add', methods=['POST', 'GET'])
def addpassenger():
    if request.method == 'GET':
        return render_template('passenger/addpassenger.html')
    elif request.method == 'POST':
        name = request.form["name"]
        passport_num = request.form["passportnum"]
        new_user = Passenger(name, passport_num)
        # VERIFY
        if new_user.is_passport_valid():
            # If it passes, carry on
            string_pas_num = "p" + str(new_user.passport_num)
            globals()[string_pas_num] = Passenger(name, passport_num)
            with open("passenger_register.txt", "a+") as register:
                register.write(string_pas_num + ", " + name + ", " + passport_num + "\n")
            return f'Passenger {globals()[string_pas_num].name} has been created with user name {string_pas_num}'
        # else return error message
        else:
            return f"Invalid passport number {passport_num}. Please use 9 integers."


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
        globals()[flighttrip].add_Passenger(globals()[passengerid])
        return f'Passenger {passengerid} has been added to flight {flighttrip}'


@app.route('/flighttrip/assignplane', methods=['POST', 'GET'])
def assignplane():
    if request.method == 'GET':
        return render_template('flighttrip/assignplane.html')
    elif request.method == 'POST':
        planeid = request.form["planeid"]
        flighttrip = request.form["flighttrip"]

        globals()[flighttrip].assign_plane(globals()[planeid])
        return f'Plane {planeid} has been added to flight {flighttrip}'


@app.route('/flighttrip/removeflighttrip', methods=['POST', 'GET'])
def removeflighttrip():
    return render_template('flighttrip/removeflighttrip.html')


@app.route('/flighttrip/removepassenger', methods=['POST', 'GET'])
def removepassengerfromflight():
    return render_template('flighttrip/removepassengerfromflight.html')


@app.route('/flighttrip/generatelist', methods=['POST', 'GET'])
def generatelist():
    if request.method == 'GET':
        return render_template('flighttrip/generateflightattendeeslist.html')
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        with open("airport_booking_app\\flight_trips\\" + flighttrip + '.txt') as file:
            content = file.read()
        return f"{content}"


@app.route('/plane')
def plane():
    return render_template('plane/plane.html')


@app.route('/plane/add', methods=['POST', 'GET'])
def addplane():
    if request.method == 'GET':
        return render_template('plane/addplane.html')
    elif request.method == 'POST':
        name = request.form["name"]
        capacity = request.form["capacity"]

        globals()[name] = Plane(capacity)
        with open("plane_register.txt", "a+") as register:
            register.write(name + ', ' + capacity + "\n")
        return f'Plane {name} has been created'


@app.route('/plane/remove')
def removeplane():
    return render_template('plane/removeplane.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
