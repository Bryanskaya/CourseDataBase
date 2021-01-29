-- Процедуры

-- Выдать новую путёвку
CREATE OR REPLACE PROCEDURE AddVoucher(num_days INTEGER, num_animals INTEGER, price NUMERIC, id_hnt INTEGER, id_prclist INTEGER)
AS $$
BEGIN	
	INSERT INTO vouchers(duration_days, amount_animals, price, id_hunter, id_pricelist)
	VALUES (num_days, num_animals, price, id_hnt, id_prclist);
	RAISE INFO 'Путёвка добавлена';
END;
$$
LANGUAGE PLpgSql;

/*CALL AddVoucher(10, 21, 0, 26703800, 1);*/


-- Удалить (закрыть) путёвку по её id
CREATE OR REPLACE PROCEDURE DelVoucher(id_vch INTEGER)
AS $$
BEGIN	
	DELETE FROM vouchers WHERE vouchers.id = id_vch;
	RAISE INFO 'Путёвка удалена';
END;
$$
LANGUAGE PLpgSql;

/*CALL DelVoucher(1);*/


-- Пометить позицию в прайс листе сектора как неактуальную
CREATE OR REPLACE PROCEDURE MarkPointPriceListIrrelevant(name_animal TEXT, id_sct INTEGER)
AS $$
BEGIN	
	UPDATE price_list
	SET is_relevant = false
	WHERE animal = name_animal AND id_sector = id_sct;
	
	RAISE INFO 'Позиция в прайс листе помечена неактуальной';
END;
$$
LANGUAGE PLpgSql;
	

/*CALL MarkPointPriceListIrrelevant('чирок', 89);*/


-- Добавить позицию в прайс лист
CREATE OR REPLACE PROCEDURE AddPointPriceList(name_animal TEXT, price NUMERIC, id_sct INTEGER)
AS $$
BEGIN	
	CALL MarkPointPriceListIrrelevant(name_animal, id_sct);
	
	INSERT INTO price_list(animal, price, is_relevant, id_sector)
	VALUES (name_animal, price, true, id_sct);
	
	RAISE INFO 'Позиция в прайс лист добавлена';
END;
$$
LANGUAGE PLpgSql;
	

/*CALL AddPointPriceList('чирок', 1000, 89);*/


