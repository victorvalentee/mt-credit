DROP TABLE IF EXISTS cards;
CREATE TABLE cards (
    exp_date TEXT NOT NULL,
    holder_name TEXT NOT NULL,
    card_number TEXT NOT NULL,
    cvv INTEGER NOT NULL,
    PRIMARY KEY(holder_name, card_number, cvv)
) STRICT;

-- As mentioned in the README file, data validation is going to be 
-- implemented as database constraints (as much as possible).
DROP TRIGGER IF EXISTS data_validation;

CREATE TRIGGER data_validation
BEFORE insert ON cards
FOR EACH ROW
BEGIN
    SELECT RAISE(ABORT, 'Account holder name must have at least 3 characters.')
    WHERE LENGTH(NEW.holder_name) < 3;
END;

CREATE TRIGGER block_updates
BEFORE UPDATE ON cards
BEGIN
    SELECT RAISE(ABORT, "Updates not allowed. A new card must be issued.");
END;