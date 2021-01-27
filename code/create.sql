DROP TABLE hunting_grounds CASCADE;
DROP TABLE sectors CASCADE;
DROP TABLE accounts CASCADE;
DROP TABLE huntsmen CASCADE;
DROP TABLE hunters CASCADE;
DROP TABLE price_list CASCADE;
DROP TABLE vouchers CASCADE;

-- done
CREATE TABLE IF NOT EXISTS hunting_grounds(
	id SERIAL PRIMARY KEY,
	ground_name VARCHAR(30) UNIQUE NOT NULL,
	square NUMERIC CONSTRAINT valid_square CHECK (square > 0),
	max_num_sectors INTEGER CONSTRAINT valid_max_num CHECK (max_num_sectors > 0)
);

--done
CREATE TABLE IF NOT EXISTS sectors(
	id SERIAL PRIMARY KEY,
	square NUMERIC CONSTRAINT valid_square CHECK (square > 0),
	id_husbandry INTEGER REFERENCES hunting_grounds
);

--done
CREATE TABLE IF NOT EXISTS accounts(
	login VARCHAR(20) PRIMARY KEY,
	pswd TEXT CONSTRAINT valid_password CHECK (length(pswd) >= 6)
);

--done
CREATE TABLE IF NOT EXISTS huntsmen(
	id INTEGER REFERENCES sectors,
	PRIMARY KEY (id),
	
	surname VARCHAR(30) NOT NULL,
	firstname VARCHAR(30) NOT NULL,
	patronymic VARCHAR(30),
	date_of_birth date NOT NULL,
	sex CHAR NOT NULL,
	experience INTEGER CONSTRAINT valid_experience CHECK (experience >= 0),
	mobile_phone VARCHAR(30) NOT NULL,
	email VARCHAR(40) NOT NULL,
	salary NUMERIC CONSTRAINT valid_salary CHECK (salary > 0),
	login VARCHAR(20) REFERENCES accounts
);

--done
CREATE TABLE IF NOT EXISTS hunters(
	ticket_num INTEGER PRIMARY KEY,
	surname VARCHAR(30) NOT NULL,
	firstname VARCHAR(30) NOT NULL,
	patronymic VARCHAR(30),
	date_of_birth date NOT NULL,
	sex CHAR NOT NULL,
	residence VARCHAR(100) NOT NULL,
	mobile_phone VARCHAR(30) NOT NULL,
	email VARCHAR(40) NOT NULL,
	login VARCHAR(20) REFERENCES accounts
);

--done
CREATE TABLE IF NOT EXISTS price_list(
	id SERIAL PRIMARY KEY,
	animal TEXT NOT NULL,
	price NUMERIC CONSTRAINT valid_price CHECK (price > 0),
	is_relevant BOOLEAN NOT NULL,
	id_sector INTEGER REFERENCES sectors
);

--done
CREATE TABLE IF NOT EXISTS vouchers(
	id SERIAL PRIMARY KEY,
	duration_days INTEGER CONSTRAINT valid_days CHECK (duration_days > 0),
	amount_animals INTEGER CONSTRAINT valid_animals CHECK (amount_animals > 0),
	price NUMERIC,
	id_hunter INTEGER REFERENCES hunters,
	id_pricelist INTEGER REFERENCES price_list
);


COPY hunting_grounds(ground_name, square, max_num_sectors)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\hunting_grounds.cvg'	 DELIMITER '|';

COPY sectors(square, id_husbandry)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\sectors.cvg'	 DELIMITER '|';

COPY accounts
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\accounts.cvg'	 DELIMITER '|';
	
COPY huntsmen
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\huntsmen.cvg'	 DELIMITER '|';

COPY hunters
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\hunters.cvg'	 DELIMITER '|';

COPY price_list(animal, price, is_relevant, id_sector)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\price_list.cvg'	 DELIMITER '|';

COPY vouchers(duration_days, amount_animals, price, id_hunter, id_pricelist)
FROM 'C:\msys64\home\bryan\CourseDataBase\code\generator\vouchers.cvg'	 DELIMITER '|';

	
SELECT * FROM hunting_grounds;
SELECT * FROM accounts;