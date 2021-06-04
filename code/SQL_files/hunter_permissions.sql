GRANT SELECT ON price_list TO hunter;
GRANT SELECT ON accounts TO hunter;
GRANT SELECT ON sectors TO hunter;
GRANT SELECT ON hunting_grounds TO hunter;
GRANT SELECT ON hunters TO hunter;
GRANT SELECT ON vouchers TO hunter;
GRANT ALL PRIVILEGES ON SEQUENCE vouchers_id_seq TO hunter;
GRANT INSERT ON vouchers TO hunter;
GRANT DELETE ON vouchers TO hunter;
GRANT INSERT VALUES('id', 'amount_animals', 'price', 'id_hunter', 'id_pricelist', 'status') INTO vouchers TO hunter;

GRANT SELECT ON huntsmen TO hunter;


UPDATE accounts SET surname = 'Я' WHERE login = '11111111';
DELETE FROM accounts WHERE login='5555555555'