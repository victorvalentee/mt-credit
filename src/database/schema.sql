DROP TABLE IF EXISTS cards;
CREATE TABLE cards (
    exp_date TEXT NOT NULL,
    holder_name TEXT NOT NULL,
    card_number TEXT NOT NULL,
    cvv INTEGER,
    credit_card_hash TEXT,
    PRIMARY KEY(holder_name, card_number)
) STRICT;

-- As mentioned in the README file, data validation is going to be 
-- implemented as database constraints (as much as possible).
DROP TRIGGER IF EXISTS data_validation;

CREATE TRIGGER data_validation
BEFORE INSERT ON cards
FOR EACH ROW
BEGIN
    SELECT RAISE(ABORT, 'Account holder name must have at least 3 characters.')
    WHERE LENGTH(NEW.holder_name) < 3;

    SELECT RAISE(ABORT, 'CVV must have either 3 or 4 characters.')
    WHERE NEW.cvv IS NOT NULL AND (LENGTH(NEW.cvv) < 3 OR LENGTH(NEW.cvv) > 4);

    SELECT RAISE(ABORT, '"exp_date" must be in the format YYYY-MM-DD.')
    WHERE DATE(NEW.exp_date) IS NULL;

    SELECT RAISE(ABORT, '"exp_date" must be in the future.')
    WHERE NEW.exp_date <= DATE('now');
END;

CREATE TRIGGER exp_date_end_of_month
AFTER INSERT ON cards
BEGIN
    -- Set NEW.exp_date to the end of the month.
    UPDATE cards 
    SET exp_date = DATE(NEW.exp_date, '+1 month', 'start of month', '-1 day')
    WHERE holder_name = NEW.holder_name 
        AND card_number = NEW.card_number;
END;
