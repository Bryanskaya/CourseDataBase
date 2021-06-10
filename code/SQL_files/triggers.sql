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
	
	RAISE INFO 'Итоговая сумма путёвки подсчитана';
	RETURN NULL;
END;
$$
LANGUAGE PLpgSql;


CREATE TRIGGER TriggerCountWholePrice
AFTER INSERT ON vouchers
FOR EACH STATEMENT
EXECUTE PROCEDURE proc_count_price();


--INSERT INTO vouchers(duration_days, amount_animals, price, id_hunter, id_pricelist) VALUES (14, 5, 0, 60971869, 2);

-- Удаление единственного админа
DROP TRIGGER IF EXISTS ProhibitDelAdmin ON accounts;

DROP FUNCTION ProhibitDelAdmin() cascade;
CREATE OR REPLACE FUNCTION ProhibitDelAdmin()
RETURNS TRIGGER
AS $$
BEGIN	
	IF OLD.type_role = 'админ' AND (
		SELECT count(*)
		FROM accounts
		WHERE type_role = 'админ') < 2
	THEN
	RAISE EXCEPTION 'Profibited to delete a single admin';
	END IF;
	RETURN OLD;
END;
$$
LANGUAGE PLpgSql;

CREATE TRIGGER ProhibitDelAdmin
BEFORE DELETE ON accounts
FOR EACH ROW
EXECUTE PROCEDURE ProhibitDelAdmin();

-- PostgreSQL

-- Каскадное удаление охотника
DROP TRIGGER IF EXISTS FullDelHunter ON accounts;

DROP FUNCTION FullDelHunter() cascade;
CREATE OR REPLACE FUNCTION FullDelHunter()
RETURNS TRIGGER
AS $$
BEGIN	
	IF OLD.type_role != 'охотник'
	THEN
	RETURN OLD;
	END IF;
	DELETE FROM vouchers
	WHERE vouchers.id_hunter IN (
		SELECT hunters.ticket_num
		FROM hunters
		WHERE hunters.login = OLD.login);
	DELETE FROM hunters
	WHERE hunters.login = OLD.login;
	RAISE INFO 'Hunter was successfully deleted';
	RETURN OLD;
END;
$$
LANGUAGE PLpgSql;

CREATE TRIGGER FullDelHunter
BEFORE DELETE ON accounts
FOR EACH ROW
EXECUTE PROCEDURE FullDelHunter();

-- PostgreSQL

-- Каскадное удаление егеря
DROP TRIGGER IF EXISTS FullDelHuntsman ON accounts;

DROP FUNCTION FullDelHuntsman() cascade;
CREATE OR REPLACE FUNCTION FullDelHuntsman()
RETURNS TRIGGER
AS $$
BEGIN	
	IF OLD.type_role != 'егерь'
	THEN
	RETURN OLD;
	END IF;
	DELETE FROM huntsmen
	WHERE huntsmen.login = OLD.login;
	RAISE INFO 'Huntsman was successfully deleted';
	RETURN OLD;
END;
$$
LANGUAGE PLpgSql;

CREATE TRIGGER FullDelHuntsman
BEFORE DELETE ON accounts
FOR EACH ROW
EXECUTE PROCEDURE FullDelHuntsman();

-- PostgreSQL


-- Добавление егеря
DROP TRIGGER IF EXISTS AddHuntsman ON huntsmen;

DROP FUNCTION AddHuntsman() cascade;
CREATE OR REPLACE FUNCTION AddHuntsman()
RETURNS TRIGGER
AS $$
BEGIN
	IF NEW.id IN (
		SELECT huntsmen.id
		FROM huntsmen)
	THEN
	RAISE EXCEPTION 'Such sector has already busy';
	END IF;
	RETURN NEW;
END;
$$
LANGUAGE PLpgSql;

CREATE TRIGGER AddHuntsman
BEFORE INSERT ON huntsmen
FOR EACH ROW
EXECUTE PROCEDURE AddHuntsman();

--INSERT INTO accounts VALUES ('test_trig4', '1', '1', 'test', 'test', '', '2000-05-01', 'м', '+7-898-898-89-89', 'test@mail.com', 'егерь');
--INSERT INTO huntsmen VALUES (37, 'test_trig4');

