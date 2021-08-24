from flask import Flask, render_template, request
from airport_booking_app.app_classes import Passenger, FlightTrip, Plane
import json

passenger_dict = {}
flight_trip_dict = {}
planes_dict = {}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/passenger')
def passenger():
    with open("airport_booking_app\\Registers\\passenger_register.json", "r") as file:
        content = json.load(file)
        register = content["passenger_register"]
    return render_template('passenger/passenger.html', content=register)


@app.route('/passenger/add', methods=['POST', 'GET'])
def addpassenger():
    if request.method == 'GET':
        return render_template('passenger/addpassenger.html')
    elif request.method == 'POST':
        name = request.form["name"]
        passport_num = request.form["passportnum"]
        passenger_id = "p" + passport_num
        passenger_dict[passenger_id] = Passenger(name, passport_num)
        # VERIFY
        if passenger_dict[passenger_id].is_passport_valid():
            passenger_dict[passenger_id].write_to_register()
            return f"Passenger {passenger_dict[passenger_id].user_info['name']} has been created with passport number {passenger_dict[passenger_id].user_info['passport_number']}. <p><a href='/passenger/add'>Back</a></p>"
        # else return error message
        else:
            return f"Invalid passport number {passport_num}. Please use 9 integers. <p><a href='/passenger/add'>Back</a></p>"


@app.route('/passenger/remove', methods=['POST', 'GET'])
def removepassenger():
    if request.method == 'GET':
        return render_template('passenger/removepassenger.html')
    elif request.method == 'POST':
        pass


@app.route('/flighttrip')
def flighttrip():
    return render_template('flighttrip/flighttrip.html')


@app.route('/flighttrip/add', methods=['POST', 'GET'])
def addflighttrip():
    if request.method == 'GET':
        return render_template('flighttrip/addflighttrip.html')
    elif request.method == 'POST':
        destination = request.form["destination"]

    flight_trip_dict[destination] = FlightTrip(destination)
    flight_trip_dict[destination].write_to_register()
    return f"Flight trip {destination} has been created. <p><a href='/flighttrip/add'>Back</a></p>"



@app.route('/flighttrip/addpassengertoflight', methods=['POST', 'GET'])
def addpassengertoflight():
    if request.method == 'GET':
        return render_template('flighttrip/addpassengertoflight.html')
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        passenger_id = request.form["passenger_id"] # change HTML
        flight_trip_dict[flighttrip].add_Passenger(passenger_dict[passenger_id])
        return f"Added {passenger_id} to {flighttrip}. <p><a href='/flighttrip'>Back</a></p>"


@app.route('/flighttrip/assignplane', methods=['POST', 'GET'])
def assignplane():
    if request.method == 'GET':
        return render_template('flighttrip/assignplane.html')
    elif request.method == 'POST':
        planeid = request.form["planeid"]
        flighttrip = request.form["flighttrip"]
        flight_trip_dict[flighttrip].assign_plane(planes_dict[planeid])
        return f"Plane {planeid} has been added to flight {flighttrip}. <p><a href='/flighttrip/assignplane'>Back</a></p>"



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
        with open("airport_booking_app\\Registers\\flight_trip_register.json") as file:
            content = json.load(file)
            passenger_list = content["flight_trip_register"][flighttrip]
        return f"{passenger_list}<p><a href='/flighttrip/generatelist'>Back</a></p>"


@app.route('/plane')
def plane():
    return render_template('plane/plane.html')


@app.route('/plane/add', methods=['POST', 'GET'])
def addplane():
    if request.method == 'GET':
        return render_template('plane/addplane.html')
    elif request.method == 'POST':
        name = request.form["planeid"]
        capacity = request.form["capacity"]
        planes_dict[name] = Plane(name, capacity)
        planes_dict[name].write_to_register()
    return f"Plane {name} has been created. <p><a href='/plane/add'>Back</a></p>"



@app.route('/plane/remove')
def removeplane():
    return render_template('plane/removeplane.html')


@app.route('/flighttrip/checkplane', methods=['POST', 'GET'])
def check_plane():
    if request.method == 'GET':
        return render_template('flighttrip/checkplane.html')
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        destination = flight_trip_dict[flighttrip]
        if destination.check_plane():
            return f"Plane assigned to {flighttrip} is valid"
        else:
            return f"Plane assigned to {flighttrip} is not valid"
    


if __name__ == '__main__':
    app.debug = True
    app.run()
