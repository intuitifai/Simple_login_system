create database IF NOT EXISTS mydb;
use mydb;
DROP TABLE IF EXISTS login_system;
create table login_system (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    password NVARCHAR(100),
    PRIMARY KEY (id)
);