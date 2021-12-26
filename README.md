# Python Banking System
A simple banking system powered by Python3, SQLAlchemy, and mySQL.

## Features

* Register as a new customer, checking account automatically created together
* Create a savings account
* Deposit, withdraw, request termination of account
* Request a service (loan, credit card, etc.) that can be adjusted by an employee before the customer accepts the terms
* Employee can adjust rates and permanently delete accounts from the database

## Banking Project UML Diagram
![umlpng](https://github.com/rlui001/Banking-Project/blob/main/diagram/Banking%20Project%20UML%20Diagram%20v1.1.png?raw=true)

## Requirements
+ sqlalchemy==1.4.22
+ mysql==8.0.22
+ python==3.9.7
+ pymysql==1.0.2

## Known Issues
* Because I have opted to use raw SQL queries, there is a potential risk of SQL injections. This may be addressed at some point when the project is complete.
