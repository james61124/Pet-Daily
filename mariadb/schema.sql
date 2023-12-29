CREATE DATABASE IF NOT EXISTS djangoDB;
USE djangoDB;

-- CREATE DATABASE `djangoDB`;
-- CREATE USER 'user' IDENTIFIED BY 'password';
-- GRANT ALL privileges ON `djangoDB`.* TO 'user'@'localhost';
-- FLUSH PRIVILEGES;

-- CREATE USER 'user'@'*' IDENTIFIED BY 'password';
-- GRANT ALL PRIVILEGES ON djangoDB.* TO 'user'@'*';
-- FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS User (
	Username varchar(36) PRIMARY KEY, 
	Password varchar(60) NOT NULL
);



CREATE TABLE IF NOT EXISTS IotWeight (
    id SERIAL PRIMARY KEY,
    date DATETIME NOT NULL,
    weight DECIMAL(6, 3) NOT NULL
);

CREATE TABLE IF NOT EXISTS IotWaterIntake (
    id SERIAL PRIMARY KEY,
    date DATETIME NOT NULL,
    water_intake DECIMAL(4, 0) NOT NULL
);

CREATE TABLE IF NOT EXISTS IotFoodIntake (
    id SERIAL PRIMARY KEY,
    date DATETIME NOT NULL,
    food_intake DECIMAL(5, 0) NOT NULL
);
