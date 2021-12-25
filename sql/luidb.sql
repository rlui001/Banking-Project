CREATE DATABASE IF NOT EXISTS LuiBank;
USE LuiBank;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Services;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE Customer (
    ssn int UNIQUE NOT NULL,
    first_name char(50) NOT NULL,
    last_name char(50) NOT NULL,
    home_address char(150) NOT NULL,
    PRIMARY KEY(ssn));

CREATE TABLE Account (
    accountid serial UNIQUE NOT NULL,
    cid int NOT NULL,
    balance int NOT NULL,
    rate float NOT NULL,
    account_type char(50) NOT NULL,
    terminate boolean NOT NULL,
    PRIMARY KEY(accountid),
    FOREIGN KEY(cid) REFERENCES Customer(ssn));

CREATE TABLE Services (
    serviceid serial UNIQUE NOT NULL,
    cid int NOT NULL,
    balance int NOT NULL,
    service_type char(50) NOT NULL,
    service_status char(50) NOT NULL,
    rate float NOT NULL,
    PRIMARY KEY(serviceid),
    FOREIGN KEY(cid) REFERENCES Customer(ssn));

