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
    with open('airport_booking_app\\Registers\\passenger_register.json', 'r') as file:
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
        passengerlist = passenger_dict.keys()
        return render_template('passenger/removepassenger.html', passengerlist=passengerlist)
    elif request.method == 'POST':
        passenger_id = request.form["passengerid"]
        pass_num = passenger_id[1:]
        del passenger_dict[passenger_id]
        with open("airport_booking_app\\Registers\\passenger_register.json", "r+") as file:
            content = json.load(file)
            register = content["passenger_register"]
            index = 0
            for user in register:
                if pass_num in user["passport_number"]:
                    del (register[index])
                    break
                index += 1            
            else:
                return f"{passenger_id} could not be found. <p><a href='/passenger'>Back</a></p>"
        with open("airport_booking_app\\Registers\\passenger_register.json", "w") as file:
            file.seek(0)
            json.dump(content, file, indent=2)
            return f"{passenger_id} has been removed.  <p><a href='/passenger'>Back</a></p>" 


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
    return f"Flight trip {destination} has been created. <p><a href='/flighttrip'>Back</a></p>"



@app.route('/flighttrip/addpassengertoflight', methods=['POST', 'GET'])
def addpassengertoflight():
    if request.method == 'GET':
        flightlist = flight_trip_dict.keys()
        passengerlist = passenger_dict.keys()
        return render_template('flighttrip/addpassengertoflight.html', flighttrip=flightlist, passengerlist=passengerlist)
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        passenger_id = request.form["passenger_id"]
        flight_trip_dict[flighttrip].add_Passenger(passenger_dict[passenger_id])
        return f"Added {passenger_id} to {flighttrip}. <p><a href='/flighttrip'>Back</a></p>"


@app.route('/flighttrip/assignplane', methods=['POST', 'GET'])
def assignplane():
    if request.method == 'GET':
        plane_list = planes_dict.keys()
        flightlist = flight_trip_dict.keys()
        return render_template('flighttrip/assignplane.html', plane_list=plane_list, flighttrip=flightlist)
    elif request.method == 'POST':
        planeid = request.form["planeid"]
        flighttrip = request.form["flighttrip"]
        flight_trip_dict[flighttrip].assign_plane(planes_dict[planeid])
        return f"Plane {planeid} has been added to flight {flighttrip}. <p><a href='/flighttrip'>Back</a></p>"



@app.route('/flighttrip/removeflighttrip', methods=['POST', 'GET'])
def removeflighttrip():
    return render_template('flighttrip/removeflighttrip.html')


@app.route('/flighttrip/removepassengerfromflight', methods=['POST', 'GET'])
def removepassengerfromflight():
    if request.method == 'GET':
        flightlist = flight_trip_dict.keys()
        passengerlist = passenger_dict.keys()
        return render_template('flighttrip/removepassengerfromflight.html', flighttrip=flightlist, passengerlist=passengerlist)
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        passenger_id = request.form["passenger_id"]
        pass_num = passenger_id[1:]
        with open("airport_booking_app\\Registers\\flight_trip_register.json", "r+") as file:
            content = json.load(file)
            register = content["flight_trip_register"][flighttrip]
            index = 0
            for user in register:
                if pass_num in user["passport_number"]:
                    del (register[index])
                    break
                index += 1            
            else:
                return f"{passenger_id} could not be found. <p><a href='/flighttrip'>Back</a></p>"
        with open("airport_booking_app\\Registers\\flight_trip_register.json", "w") as file:
            file.seek(0)
            json.dump(content, file, indent=2)
            return f"{passenger_id} has been removed from the flight: {flighttrip}.  <p><a href='/flighttrip'>Back</a></p>" 


@app.route('/flighttrip/generatelist', methods=['POST', 'GET'])
def generatelist():
    if request.method == 'GET':
        flightlist = flight_trip_dict.keys()
        return render_template('flighttrip/generateflightattendeeslist.html', flighttrip=flightlist)
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        with open("airport_booking_app\\Registers\\flight_trip_register.json") as file:
            content = json.load(file)
            passenger_list = content["flight_trip_register"][flighttrip]
        return f"{passenger_list}<p><a href='/flighttrip'>Back</a></p>"


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
    return f"Plane {name} has been created. <p><a href='/plane'>Back</a></p>"



@app.route('/plane/remove')
def removeplane():
    return render_template('plane/removeplane.html')


@app.route('/flighttrip/checkplane', methods=['POST', 'GET'])
def check_plane():
    if request.method == 'GET':
        flightlist = flight_trip_dict.keys()
        return render_template('flighttrip/checkplane.html', flighttrip=flightlist)
    elif request.method == 'POST':
        flighttrip = request.form["flighttrip"]
        destination = flight_trip_dict[flighttrip]
        if destination.check_plane():
            return f"Plane assigned to {flighttrip} is valid.  <p><a href='/flighttrip'>Back</a></p>"
        else:
            return f"Plane assigned to {flighttrip} is not valid.  <p><a href='/flighttrip'>Back</a></p>"
    


if __name__ == '__main__':
    app.debug = True
    app.run()
