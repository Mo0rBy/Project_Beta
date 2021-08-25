## Project_Beta Airlines

 ## Contents
* [How to Run App](#How-to-Run-App)
* [Using the Booking App](#Using-the-Booking-App)
* [Removing Instances From Booking App](#Removing-Instances-From-Booking-App)

## How to Run App
```
Execute in Order:
cd into location you want the files to be stored.
git clone https://github.com/Mo0rBy/Project_Beta.git
cd Project_Beta
pip install -r requirements.txt
python app.py
```
## Using the Booking App

Follow Steps in Order:

1. Navigate to Passenger home page
    * Click Add Passenger
    * Input the name and passport number for the passenger - passport number should be 9 digits long
    * Click Submit
    
2. Navigate to Flight Trip homepage.
    * Click Add Flight Trip
    * Enter a Destination
    * Click Submit
    
3. Navigate to Plane homepage.
    * Click Add Plane
    * Enter a Plane Name e.g. Boeing747
    * Click Submit
    
4. Navigate to Passenger homepage to add passenger to flight.
    * Select Passenger from Dropdown
    * Select Destination from Dropdown
    * Click Submit
    
5. Navigate to Flight Trip homepage to add plane to flight trip.
    * Select Plane from Dropdown
    * Select Destination from Dropdown
    * Click Submit

6. Navigate to Flight Trip homepage to check flight trip has a suitable plane.
    * Select Destination from Dropdown
    * Click Submit

## Removing Instances From Booking App

1. Removing Passenger from Passenger List
    * Navigate to the Passenger homepage
    * Select the passenger id to be removed from the dropdown
    * Click Submit
    
2. Remove Flight Trip
    * Navigate to the Flight Trip homepage
    * Select from the dropdown the Destination to be removed
    * Click Submit
    
3. Remove Passenger from Flight
    * Navigate to the Flight Trip homepage
    * Select the destination from the dropdown
    * Select the passengers id from the second dropdown
    * Click Submit
    
4. Remove Plane
    * Navigate to Plane homepage
    * Select from the dropdown the plane to be removed
    * Click Submit
    
