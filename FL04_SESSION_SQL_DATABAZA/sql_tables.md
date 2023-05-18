# UVOD DO SQL

Strukturovany Query Languague

SHOW DATABASES;

CREATE DATABASE testdb;

<code>USE testdb;</code>

CREATE TABLE inventar 
(
    id int NOT NULL PRIMARY KEY,
    Item varchar(255) NOT NULL
    );

INSERT INTO inventar(id, item) VALUES (54243, 'stolicka');

SELECT * FROM inventar;

SELECT id FROM inventar

SELECT * FROM inventar ORDER BY id ASC;

SELECT COUNT(*) AS Count FROM inventar;

DELETE FROM inventar WHERE id = 54365463;

## RELATIONSHIP

Prepojenie tabuliek cez tzv FOREIGN KEY