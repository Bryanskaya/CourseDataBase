-- Функции

-- Получить все путёвки на конкретного пользователя
DROP TYPE table_vouchers;
CREATE TYPE table_vouchers AS
(
	id_voucher		INTEGER,
	animal			TEXT,
	amount_animals 	INTEGER,
	duration_days 	INTEGER,
	id_sector		INTEGER,
	price 			NUMERIC
);

DROP FUNCTION ShowVouchersByIdHnt(id_hunter INTEGER);
CREATE OR REPLACE FUNCTION ShowVouchersByIdHnt(id_hnt INTEGER)
RETURNS SETOF table_vouchers
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT vouchers.id,
			   price_list.animal,
			   vouchers.amount_animals,
			   vouchers.duration_days,
			   price_list.id_sector,
			   vouchers.price
		FROM vouchers JOIN price_list ON vouchers.id_pricelist = price_list.id
		WHERE vouchers.id_hunter = id_hnt
	);
END;
$$
LANGUAGE PLpgSql;

/*SELECT *
FROM ShowVouchersByIdHnt(18178173);*/

-- Получить все путёвки в конкретном секторе
DROP TYPE table_sct_vouchers;
CREATE TYPE table_sct_vouchers AS
(
	ticket_num 		INTEGER,
	surname			VARCHAR(30),
	firstname		VARCHAR(30),
	patronymic		VARCHAR(30),
	date_of_birth	DATE,
	mobile_phone	VARCHAR(30),
	id_voucher		INTEGER,
	animal			TEXT,
	amount_animals 	INTEGER,
	duration_days 	INTEGER,
	price 			NUMERIC
);

DROP FUNCTION ShowVouchersByIdSct(id_hunter INTEGER);
CREATE OR REPLACE FUNCTION ShowVouchersByIdSct(id_sct INTEGER)
RETURNS SETOF table_sct_vouchers
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunters.ticket_num,
			   hunters.surname,
			   hunters.firstname,
			   hunters.patronymic,
			   hunters.date_of_birth,
			   hunters.mobile_phone,
			   vouchers.id,
			   price_list.animal,
			   vouchers.amount_animals,
			   vouchers.duration_days,
			   vouchers.price
		FROM vouchers JOIN price_list ON vouchers.id_pricelist = price_list.id
		JOIN hunters ON hunters.ticket_num = vouchers.id_hunter
		WHERE price_list.id_sector = id_sct
	);
END;
$$
LANGUAGE PLpgSql;

/*SELECT *
FROM ShowVouchersByIdSct(55);*/

-- Прайс лист путёвок только в секторе под номером (номер вводится)
DROP TYPE table_pricelist CASCADE;
CREATE TYPE table_pricelist AS
(
	id_pos			INTEGER,
	animal			TEXT,
	price		 	NUMERIC,
	id_sector		INTEGER,
	name_ground		VARCHAR(30)
); 

DROP FUNCTION ShowPriceListByIdSct(id_sct INTEGER);
CREATE OR REPLACE FUNCTION ShowPriceListByIdSct(id_sct INTEGER)
RETURNS SETOF table_pricelist
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT price_list.id,
			   price_list.animal,
			   price_list.price,
			   price_list.id_sector,
			   hunting_grounds.ground_name
		FROM price_list JOIN sectors ON price_list.id_sector = sectors.id
			JOIN hunting_grounds ON hunting_grounds.id = sectors.id_husbandry
		WHERE price_list.id_sector = id_sct and price_list.is_relevant = true
		ORDER BY price_list.animal
	);
END;
$$
LANGUAGE PLpgSql;

/*SELECT *
FROM ShowPriceListByIdSct(89);*/

-- Получить информацию следующего вида: 
-- название хозяйства - номер сектора - название животного - количество выданных путёвок - средняя цена
DROP TYPE table_genprices CASCADE;
CREATE TYPE table_genprices AS
(
	ground_name		VARCHAR(30),
	id_sector		INTEGER,
	animal			TEXT,
	num				BIGINT,
	avg_price		NUMERIC
);

DROP FUNCTION ShowDeneralInfoPrices();
CREATE OR REPLACE FUNCTION ShowDeneralInfoPrices()
RETURNS SETOF table_genprices
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunting_grounds.ground_name,
			   temp_res.id_sector,
			   temp_res.animal,
			   temp_res.num,
			   temp_res.price
		FROM hunting_grounds JOIN sectors ON hunting_grounds.id = sectors.id_husbandry
			JOIN 
		(
			SELECT price_list.id_sector, price_list.animal, COUNT(vouchers.id_pricelist) AS num, ROUND(AVG(price_list.price), 2) AS price
			FROM price_list LEFT JOIN vouchers ON vouchers.id_pricelist = price_list.id
			GROUP BY price_list.id_sector, price_list.animal
			ORDER BY price_list.id_sector, price_list.animal
		) AS temp_res ON sectors.id = temp_res.id_sector
		ORDER BY hunting_grounds.ground_name, temp_res.id_sector
	);
END;
$$
LANGUAGE PLpgSql;


/*SELECT *
FROM ShowDeneralInfoPrices();*/

-- Получить информацию вида: название хозяйства -- номер сектора -- ФИО егеря + контакты
DROP TYPE table_hntmen CASCADE;
CREATE TYPE table_hntmen AS
(
	ground_name		VARCHAR(30),
	id_sector		INTEGER,
	surname 		VARCHAR(30),
	firstname 		VARCHAR(30),
	patronymic		VARCHAR(30),
	mobile_phone 	VARCHAR(30),
	email 			VARCHAR(40)
);

DROP FUNCTION ShowHuntmen();
CREATE OR REPLACE FUNCTION ShowHuntmen()
RETURNS SETOF table_hntmen
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunting_grounds.ground_name,
			   sectors.id,
			   huntsmen.surname, huntsmen.firstname, huntsmen.patronymic,
			   huntsmen.mobile_phone,
			   huntsmen.email
		FROM hunting_grounds JOIN sectors ON hunting_grounds.id = sectors.id_husbandry
			JOIN huntsmen ON sectors.id = huntsmen.id
		ORDER BY hunting_grounds.ground_name, sectors.id
	);
END;
$$
LANGUAGE PLpgSql;


/*SELECT *
FROM ShowHuntmen();*/


-- Найти охотника по ФИО и получить подробнейшую инфу о нём (включая все путёвки, которые у него есть)
-- СПОРНЫЙ МОМЕНТ, ЕСЛИ ДЕЛАТЬ ПО ЭТОЙ ФУНКЦИИ ТО ИНФА ПРО ОХОТНИКА БУДЕТ ПОСТОЯННО ДУБЛИРОВАТЬСЯ В ЗАВИСИМОСТИ ОТ КОЛИЧЕСТВА ПУТЁВОК
-- НО ЕСЛИ ДЕЛАТЬ В ДВЕ ФУНКЦИИ, ТО НУЖНО ТОГДА УЧИТЫВАТЬ ПОЛНОЕ СОВПАДЕНИЕ ПО ФИО НЕСКОЛЬКИХ ЧЕЛОВЕК
DROP TYPE table_hntr CASCADE;
CREATE TYPE table_hntr AS
(
	ticket_num 		INTEGER,
	surname 		VARCHAR(30),
	firstname 		VARCHAR(30),
	patronymic		VARCHAR(30),
	date_of_birth 	DATE,
	sex 			CHAR,
	mobile_phone 	VARCHAR(30),
	email 			VARCHAR(40),
	residence 		VARCHAR(100),
	id_voucher		INTEGER,
	animal			TEXT,
	num_animals		INTEGER,
	num_days		INTEGER,
	price			NUMERIC,
	id_sector		INTEGER
);


DROP FUNCTION ShowHuntersBySFP(surname VARCHAR(30), firstname VARCHAR(30), patronymic VARCHAR(30));
CREATE OR REPLACE FUNCTION ShowHuntersBySFP(t_surname VARCHAR(30), t_firstname VARCHAR(30), t_patronymic VARCHAR(30))
RETURNS SETOF table_hntr
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunters.ticket_num,
			   hunters.surname, hunters.firstname, hunters.patronymic,
			   hunters.date_of_birth,
			   hunters.sex,
			   hunters.mobile_phone,
			   hunters.email,
			   hunters.residence,
			   vouchers.id,
			   price_list.animal,
			   vouchers.amount_animals,
			   vouchers.duration_days,
			   vouchers.price,
			   price_list.id_sector
		FROM hunters JOIN vouchers ON hunters.ticket_num = vouchers.id_hunter
			JOIN price_list ON vouchers.id_pricelist = price_list.id
		WHERE hunters.surname = t_surname AND hunters.firstname = t_firstname AND hunters.patronymic = t_patronymic
		ORDER BY price_list.animal
	);
END;
$$
LANGUAGE PLpgSql;


/*SELECT * FROM ShowHuntersBySFP('Шубина', 'Анна', 'Болеславовна');*/

-- Получить некоторую информацию об охотнике по ФИО
DROP TYPE table_hntr_part1 CASCADE;
CREATE TYPE table_hntr_part1 AS
(
	ticket_num 		INTEGER,
	surname 		VARCHAR(30),
	firstname 		VARCHAR(30),
	patronymic		VARCHAR(30),
	date_of_birth 	DATE,
	sex 			CHAR,
	mobile_phone 	VARCHAR(30),
	email 			VARCHAR(40),
	residence 		VARCHAR(100)
);


DROP FUNCTION ShowHunterBySFP(surname VARCHAR(30), firstname VARCHAR(30), patronymic VARCHAR(30));
CREATE OR REPLACE FUNCTION ShowHunterBySFP(t_surname VARCHAR(30), t_firstname VARCHAR(30), t_patronymic VARCHAR(30))
RETURNS SETOF table_hntr_part1
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunters.ticket_num,
			   hunters.surname, hunters.firstname, hunters.patronymic,
			   hunters.date_of_birth,
			   hunters.sex,
			   hunters.mobile_phone,
			   hunters.email,
			   hunters.residence
		FROM hunters
		WHERE hunters.surname = t_surname AND hunters.firstname = t_firstname AND hunters.patronymic = t_patronymic
	);
END;
$$
LANGUAGE PLpgSql;

/*SELECT * FROM ShowHunterBySFP('Шубина', 'Анна', 'Болеславовна');*/


-- Получить всех охотников, которых охотятся в конкретном секторе
DROP TYPE table_hntr_sct CASCADE;
CREATE TYPE table_hntr_sct AS
(
	ticket_num 		INTEGER,
	surname 		VARCHAR(30),
	firstname 		VARCHAR(30),
	patronymic		VARCHAR(30),
	mobile_phone 	VARCHAR(30),
	email 			VARCHAR(40),
	id_voucher		INTEGER,
	animal			TEXT,
	num_animals		INTEGER,
	num_days		INTEGER,
	price			NUMERIC
);


DROP FUNCTION ShowHuntersByIdSct(id_sct INTEGER);
CREATE OR REPLACE FUNCTION ShowHuntersByIdSct(id_sct INTEGER)
RETURNS SETOF table_hntr_sct
AS $$
BEGIN
	RETURN QUERY
	(
		SELECT hunters.ticket_num,
			   hunters.surname, hunters.firstname, hunters.patronymic,
			   hunters.mobile_phone,
			   hunters.email,
			   vouchers.id,
			   price_list.animal,
			   vouchers.amount_animals,
			   vouchers.duration_days,
			   vouchers.price
		FROM hunters JOIN vouchers ON hunters.ticket_num = vouchers.id_hunter
			JOIN price_list ON vouchers.id_pricelist = price_list.id
		WHERE price_list.id_sector = id_sct
		ORDER BY hunters.surname, hunters.firstname, hunters.patronymic, price_list.animal
	);
END;
$$
LANGUAGE PLpgSql;


/*SELECT * FROM ShowHuntersByIdSct(10);*/