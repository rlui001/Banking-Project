CREATE DATABASE IF NOT EXISTS LuiBank;
USE LuiBank;

DROP TABLE IF EXISTS Customer CASCADE;
DROP TABLE IF EXISTS Account CASCADE;
DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS Services CASCADE;

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
    service_type char(50) NOT NULL,
    service_status char(50) NOT NULL,
    ratee float NOT NULL,
    PRIMARY KEY(serviceid),
    FOREIGN KEY(cid) REFERENCES Customer(ssn));

