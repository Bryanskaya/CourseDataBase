GRANT SELECT ON price_list TO huntsman;
GRANT SELECT ON accounts TO huntsman;
GRANT SELECT ON huntsmen TO huntsman;
GRANT SELECT ON hunters TO huntsman;
GRANT SELECT ON sectors TO huntsman;
GRANT SELECT ON vouchers TO huntsman;
GRANT SELECT ON hunting_grounds TO huntsman;

GRANT UPDATE ON vouchers TO huntsman;

GRANT DELETE ON vouchers TO huntsman;
GRANT DELETE ON hunters TO huntsman;

GRANT INSERT ON vouchers TO huntsman;

GRANT ALL PRIVILEGES ON SEQUENCE vouchers_id_seq TO huntsman;