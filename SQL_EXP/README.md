# SQL EXP

tento súbor je popis k ukážke kódu pre pripojenie k databáze 
SQL = mariadb aka MySQL.

## Kontajner v dockeri
Databáza nám beží v izolovanom kontajneri v dockeri a pripájame sa 
na ňu cez localhost a port 3306.

```bash
docker run -p 127.0.0.1:3306:3306  --name mdb2 -e MARIADB_ROOT_PASSWORD=Password123! -d mariadb:latest
```


## Pripojenie do konzoly

K bežiacemu kontajneru máme možnosť priamo sa pripojiť pomocou
príkazu:
``` bash
docker exec -it mdb2 mariadb --user root -pPassword123!
```

Musíme vytvoriť databázu test pomocou príkazu SQL

``` sql
CREATE DATABASE test;
USE DATABASE test;
```

## SQLAlchemy

Kód v súbore sql_exp.py nám demonštruje ako sa dajú v SQL vytvárať
tabuľky, ukladať jeden alebo viacero záznamov, vymazávať alebo filtrovať
dáta pomocou podmienok.

``` sql
SELECT * FROM employees;
```

Pomocou tohto záznamu zobrazíme všetko v tabuľke employees,
ktorú nám vytvoril python.
