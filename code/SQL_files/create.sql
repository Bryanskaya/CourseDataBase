DROP TABLE hunting_grounds CASCADE;
DROP TABLE sectors CASCADE;
DROP TABLE accounts CASCADE;
DROP TABLE huntsmen CASCADE;
DROP TABLE hunters CASCADE;
DROP TABLE price_list CASCADE;
DROP TABLE vouchers CASCADE;


CREATE TABLE IF NOT EXISTS hunting_grounds(
	id SERIAL PRIMARY KEY,
	ground_name TEXT UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS sectors(
	id SERIAL PRIMARY KEY,
	id_husbandry INTEGER REFERENCES hunting_grounds
);


CREATE TABLE IF NOT EXISTS accounts(
	login VARCHAR(20) PRIMARY KEY,
	salt TEXT,
	hashed_password TEXT,
	surname VARCHAR(30) NOT NULL,
	firstname VARCHAR(30) NOT NULL,
	patronymic VARCHAR(30),
	date_of_birth DATE NOT NULL,
	sex CHAR NOT NULL,
	mobile_phone VARCHAR(30) NOT NULL,
	email VARCHAR(50) NOT NULL,
	type_role VARCHAR(10) NOT NULL
);


CREATE TABLE IF NOT EXISTS huntsmen(
	id INTEGER REFERENCES sectors,
	PRIMARY KEY (id),
	login VARCHAR(20) REFERENCES accounts
);


CREATE TABLE IF NOT EXISTS hunters(
	ticket_num TEXT PRIMARY KEY,
	residence VARCHAR(100) NOT NULL,
	login VARCHAR(20) REFERENCES accounts
);


CREATE TABLE IF NOT EXISTS price_list(
	id SERIAL PRIMARY KEY,
	animal TEXT NOT NULL,
	price NUMERIC CONSTRAINT valid_price CHECK (price > 0),
	is_relevant BOOLEAN NOT NULL,
	id_sector INTEGER REFERENCES sectors
);


CREATE TABLE IF NOT EXISTS vouchers(
	id SERIAL PRIMARY KEY,
	amount_animals INTEGER CONSTRAINT valid_animals CHECK (amount_animals > 0),
	price NUMERIC,
	id_hunter TEXT REFERENCES hunters,
	id_pricelist INTEGER REFERENCES price_list,
	status BOOLEAN NOT NULL
);


COPY hunting_grounds(ground_name)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\hunting_grounds_real.cvg'	 DELIMITER '|';

COPY sectors(id_husbandry)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\sectors.csv'	 DELIMITER '|';

COPY accounts
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\accounts.cvg'	 DELIMITER '|';
	
COPY huntsmen
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\huntsmen.cvg'	 DELIMITER '|';

COPY hunters
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\hunters.cvg'	 DELIMITER '|';

COPY price_list(animal, price, is_relevant, id_sector)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\price_list.cvg'	 DELIMITER '|';

COPY vouchers(duration_days, amount_animals, price, id_hunter, id_pricelist)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\SQL_files\generator\vouchers.cvg'	 DELIMITER '|';


SELECT * FROM hunting_grounds;
SELECT * FROM vouchers;
SELECT * FROM hunters;
SELECT * FROM price_list;
SELECT * FROM huntsmen;
SELECT * FROM accounts;
SELECT * FROM sectors;

UPDATE vouchers
SET price = price_list.price * amount_animals
FROM price_list
WHERE vouchers.id_pricelist = price_list.id
