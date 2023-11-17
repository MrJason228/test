CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(70)
);
INSERT INTO categories(name) VALUES ('Electronic');
INSERT INTO categories(name) VALUES ('Furniture');
INSERT INTO categories(name) VALUES ('Toys');


CREATE TABLE IF NOT EXISTS information(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(70),
        email VARCHAR(70),
        phone_number VARCAHR(50)
);
INSERT INTO information(username, email, phone_number) VALUES ('Міхаїл Петрович', 'misha01@gmail.com', '+380681234567');
INSERT INTO information(username, email, phone_number) VALUES ('Андрій Читачіло', 'supermegaemail002@ukr.net', '+380986783214');
INSERT INTO information(username, email, phone_number) VALUES ('Євгеній Галусчай', 'gabsburgchai@gmail.com', '+380962206050')
