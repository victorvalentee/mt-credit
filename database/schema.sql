CREATE TABLE IF NOT EXISTS cards (
    exp_date VARCHAR NOT NULL,
    holder_name VARCHAR NOT NULL,
    card_number VARCHAR NOT NULL,
    cvv INTEGER NOT NULL,
    PRIMARY KEY(holder_name, card_number, cvv)
);
