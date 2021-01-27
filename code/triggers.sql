-- Триггеры

-- На каждое добавление новой путёвки рассчитывается её цена 
DROP TRIGGER IF EXISTS TriggerCountWholePrice ON vouchers;

DROP FUNCTION proc_count_price() cascade;
CREATE OR REPLACE FUNCTION proc_count_price()
RETURNS TRIGGER
AS $$
BEGIN	
	UPDATE vouchers
	SET price = price_list.price * amount_animals
	FROM price_list
	WHERE vouchers.id_pricelist = price_list.id 
	and vouchers.id =
	(
		select max(id)
		from vouchers
	);
	
	RETURN NULL;
END;
$$
LANGUAGE PLpgSql;


CREATE TRIGGER TriggerCountWholePrice
AFTER INSERT ON vouchers
FOR EACH STATEMENT
EXECUTE PROCEDURE proc_count_price();


--INSERT INTO vouchers(duration_days, amount_animals, price, id_hunter, id_pricelist) VALUES (14, 5, 0, 60971869, 2);

