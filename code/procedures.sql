-- Процедуры

-- Выдать новую путёвку
CREATE OR REPLACE PROCEDURE AddVoucher(num_days INTEGER, num_animals INTEGER, price NUMERIC, id_hnt INTEGER, id_prclist INTEGER)
AS $$
BEGIN	
	INSERT INTO vouchers VALUES (num_days, num_animals, price, id_hnt, id_prclist);
	RAISE INFO 'Запись добавлена';
END;
$$
LANGUAGE PLpgSql;

CALL AddVoucher(10, 2, 0, 26703800, 1);

