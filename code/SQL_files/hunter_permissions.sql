GRANT SELECT ON price_list TO hunter;
GRANT SELECT ON accounts TO hunter;
GRANT SELECT ON sectors TO hunter;
GRANT SELECT ON hunting_grounds TO hunter;
GRANT SELECT ON hunters TO hunter;
GRANT INSERT VALUES('id', 'amount_animals', 'price', 'id_hunter', 'id_pricelist', 'status') ON vouchers TO hunter;
