import sqlalchemy as db
import mariadb
from sqlalchemy.orm import declarative_base  # toto nam urcuje sposob ako budeme modelovat nase tabuly
from sqlalchemy.orm import sessionmaker  #
# docker run --hostname=562ba3b4a78d --mac-address=02:42:ac:11:00:02 --env=MARIADB_ROOT_PASSWORD=Password123! --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=GOSU_VERSION=1.14 --env=LANG=C.UTF-8 --env=MARIADB_VERSION=1:10.11.3+maria~ubu2204 --volume=/var/lib/mysql -p 127.0.0.1:3306:3306 --restart=no --label='org.opencontainers.image.authors=MariaDB Community' --label='org.opencontainers.image.base.name=docker.io/library/ubuntu:jammy' --label='org.opencontainers.image.description=MariaDB Database for relational SQL' --label='org.opencontainers.image.documentation=https://hub.docker.com/_/mariadb/' --label='org.opencontainers.image.licenses=GPL-2.0' --label='org.opencontainers.image.ref.name=ubuntu' --label='org.opencontainers.image.source=https://github.com/MariaDB/mariadb-docker' --label='org.opencontainers.image.title=MariaDB Database' --label='org.opencontainers.image.url=https://github.com/MariaDB/mariadb-docker' --label='org.opencontainers.image.vendor=MariaDB Community' --label='org.opencontainers.image.version=10.11.3' --runtime=runc -d mariadb:latest
engine = db.create_engine('mariadb+mariadbconnector://root:Password123!@127.0.0.1:3306/test')  # PSW nachadza sa iba na strane serveru

print(engine)

Base = declarative_base()

# M O D E L  TABULKY
class Employee(Base):  # Model databazy
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    meno = db.Column(db.String(length=100))
    priezvisko = db.Column(db.String(length=100))
    active = db.Column(db.Boolean, default=True)


Base.metadata.create_all(engine)

# S E S S I O N

Session = sessionmaker()  # objekt ktory nam umoznuje vytvarat sessiony
Session.configure(bind=engine)  # tu session spojime s databazou
session = Session()   # instancia triedy session

zamestnanec = db.insert(Employee).values(meno='Spongebob', priezvisko='Squarepants')
print(zamestnanec)
compiled = zamestnanec.compile()
print(compiled.params)




# vlozenie dalsich dvoch zamestnancov
zamestnanec2 = Employee(meno='Patrick', priezvisko='Nema', active=True)
# zamestnanec3 = Employee(meno='Crabs', priezvisko='Nema', active=True)

# session.add_all([zamestnanec2, zamestnanec3])
# session.commit()


# vlozenie jedneho zaznamu do databazy bez SEssion
#with engine.connect() as conn:
    #result = conn.execute(zamestnanec)
    #conn.commit()
'''
with Session() as session:
    vevericka = Employee(id=5454, meno='Vevericka', priezvisko='None', active=True)
    session.add(vevericka)
    session.commit()
'''

# vypis vsetko z tabulky

for i in session.query(Employee).all():
    print(vars(i))

# VYMAZE Z DATABAZY ZAMESTNANCA
zamestnanec = db.delete(Employee).where(Employee.id==2)
session.execute(zamestnanec)
session.commit()

# vypis vsetko z tabulky
print('\n\n\n\n NOVY PRINT DATABAZY')
for i in session.query(Employee).all():
    print(vars(i))


# vypis vsetko z tabulky
print('\n\n\n\n NOVY PRINT DATABAZY')
for i in session.query(Employee).filter(Employee.meno=='Spongebob'):
    print(vars(i))

