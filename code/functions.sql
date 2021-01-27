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
		WHERE price_list.id_sector = id_sct
	);
END;
$$
LANGUAGE PLpgSql;

/*SELECT *
FROM ShowPriceListByIdSct(95);*/




