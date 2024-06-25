# Parking Management System

#### Description
The main design and development of a parking management system, including vehicle management and billing management two parts.
1. Entry time of vehicles shall be recorded while exit time of vehicles shall be calculated.
2. Long-term card vehicles pay an annual or monthly fee. Calculate and pay the parking fee when the temporary vehicle comes out.
3. Parking management, real-time display of the total number and status of parking Spaces, the number of idle parking Spaces.
4. Parking fee inquiry and statistics.
5. Incoming vehicles and time will be generated randomly.
#### Software Architecture
The backend architecture description
- code
  - controller   <!--Basic Method of Database-->
    - __init__.py
    - carsController.py
    - parkingController.py
  - models      <!--Database Object-->
    - __init__.py
    - cars.py
    - parking.py
  - service     <!--Database Operation Method-->
    - __init__.py
    - service
  - __init__.py
- config        <!--Configuration File-->
  - config.py
  - __init__.py
- utils         <!--Common Methods-->

The frontend architecture description


#### Instructions

1. Enter the URL: xxxx, but for the time being, it can only be started by typing python start.py runserver in the terminal.
2. In each page there are text prompts to operate, the home page can be a vehicle into the garage; the current parking space can be viewed to see the current occupancy of the parking space and out of the garage; the use of the record can be viewed in all the history of the record.

#### Contribution
Menglin Zou

