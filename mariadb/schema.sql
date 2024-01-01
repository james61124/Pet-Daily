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
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid VARCHAR(36) NOT NULL,
    username VARCHAR(36) NOT NULL,
    password VARCHAR(60) NOT NULL,
    money DECIMAL(5, 0) DEFAULT 1000 NOT NULL
);

CREATE TABLE IF NOT EXISTS Pet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid VARCHAR(60) NOT NULL,
    petid VARCHAR(60) NOT NULL,
    name VARCHAR(36),
    breed VARCHAR(10),
    gender VARCHAR(10),
    age DECIMAL(3, 0),
    weight DECIMAL(5, 1),
    image VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS UserProduct (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid VARCHAR(60) NOT NULL,
    productid VARCHAR(60) NOT NULL,
    description VARCHAR(10),
    posX DECIMAL(4, 0),
    posY DECIMAL(4, 0),
    width DECIMAL(4, 0),
    height DECIMAL(4, 0),
    zIndex DECIMAL(4, 0),
    equipped BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    productid VARCHAR(60) NOT NULL,
    name VARCHAR(36),
    price DECIMAL(5, 0),
    image VARCHAR(100),
    product_type VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Diary (
    id SERIAL PRIMARY KEY,
    petid VARCHAR(60) NOT NULL,
    date DATE NOT NULL,
    image VARCHAR(100),
    content TEXT,
    place VARCHAR(120),
    mood VARCHAR(10),
    weight DECIMAL(6, 3),
    water_intake DECIMAL(4, 0),
    food_intake DECIMAL(5, 3),
    defecation VARCHAR(20),
    abnormality TEXT,
    medical_record TEXT
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
