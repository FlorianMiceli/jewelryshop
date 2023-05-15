CREATE TABLE CHAINES(
    typeProduit VARCHAR(10) NOT NULL,
    idChaine VARCHAR(21) NOT NULL,
    nomChaine VARCHAR(50),
    prixChaine NUMERIC(10, 2) check (prixChaine >= 0),
    stock INT check (Stock >= 0) NOT NULL,
    catalogue INT,
    PRIMARY KEY (typeProduit, idChaine)
);

CREATE TABLE COLLIERS(
    typeProduit VARCHAR(10) NOT NULL,
    idCollier VARCHAR(21) NOT NULL,
    idChaine VARCHAR(21),
    nomProduit VARCHAR(10),
    nomCollier VARCHAR(50),
    prixCollier NUMERIC(10, 2) check (prixCollier >= 0),
    disponibilite BOOLEAN,
    catalogue INT,
    PRIMARY KEY (typeProduit, idCollier),
    FOREIGN KEY (idChaine, nomProduit) references CHAINES(idChaine, typeProduit)
);

CREATE TABLE PERLES(
    typeProduit VARCHAR(10) NOT NULL,
    idPerle VARCHAR(21) NOT NULL,
    nomPerle VARCHAR(50),
    prixPerle NUMERIC(10, 2) check (PrixPerle >= 0),
    stock INT check (Stock >= 0) NOT NULL,
    catalogue INT,
    PRIMARY KEY (typeProduit, idPerle)
);

CREATE TABLE PENDENTIFS(
    idCollier VARCHAR(21),
    nomProduit VARCHAR(10),
    idPerle VARCHAR(21),
    typeProduit VARCHAR(10),
    nbPerle INT check (nbPerle >= 0),
    FOREIGN KEY (idCollier, nomProduit) references COLLIERS(idCollier, typeProduit),
    FOREIGN KEY (idPerle, typeProduit) references PERLES(idPerle, typeProduit)
);

CREATE TABLE COLLIERS_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    typeProduit VARCHAR(10) NOT NULL,
    idCollier VARCHAR(21) NOT NULL,
    idChaine VARCHAR(21),
    nomProduit VARCHAR(10),
    nomCollier VARCHAR(50),
    prixCollier NUMERIC(10, 2) check (prixCollier >= 0),
    disponibilite BOOLEAN,
    catalogue INT
);

CREATE TABLE PERLES_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    typeProduit VARCHAR(10) NOT NULL,
    idPerle VARCHAR(21) NOT NULL,
    nomPerle VARCHAR(50),
    prixPerle NUMERIC(10, 2) check (prixPerle >= 0),
    stock INT check (stock >= 0),
    catalogue INT
);

CREATE TABLE CHAINES_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    typeProduit VARCHAR(10) NOT NULL,
    idChaine VARCHAR(21) NOT NULL,
    nomChaine VARCHAR(50),
    prixChaine NUMERIC(10, 2) check (prixChaine >= 0),
    stock INT check (stock >= 0) NOT NULL,
    catalogue INT
);

CREATE TABLE PENDENTIFS_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    idCollier VARCHAR(21) NOT NULL,
    nomProduit VARCHAR(10),
    idPerle VARCHAR(21) NOT NULL,
    typeProduit VARCHAR(10) NOT NULL,
    nbPerle INT check (nbPerle >= 0)
);

CREATE TABLE CARTES(
    idCarte VARCHAR(21) PRIMARY KEY NOT NULL,
    nomCarte VARCHAR(50),
    prixCarte INT Check (prixCarte >= 0),
    descCarte TEXT,
    numBoutique INT
);

CREATE TABLE CLIENTS(
    idClient VARCHAR(21) PRIMARY KEY NOT NULL,
    nomClient VARCHAR(50) NOT NULL,
    prenomClient VARCHAR(50) NOT NULL,
    idCarte VARCHAR(21) references CARTES(idCarte),
    numBoutique INT NOT NULL,
    numRue INT,
    nomRue TEXT,
    codePostal INT,
    ville TEXT,
    mail TEXT,
    tel INT,
    points INT check (points >= 0)
);

CREATE TABLE TRANSACTIONS_LOCALES(
    idTransaction INT PRIMARY KEY NOT NULL,
    idClient VARCHAR(21) references CLIENTS(idClient),
    montant NUMERIC(10, 2),
    pointsImpliques INT,
    dateTransac Timestamp,
    descTransac TEXT,
    idProduit VARCHAR(21),
    typeProduit VARCHAR(10)
);

CREATE TABLE TRANSACTIONS_LOCALES_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    idTransaction INT,
    idClient VARCHAR(21),
    montant NUMERIC(10, 2),
    pointsImpliques INT,
    dateTransac Timestamp,
    descTransac TEXT,
    idProduit VARCHAR(21),
    typeProduit VARCHAR(10)
);

CREATE TABLE CLIENTS_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    idClient VARCHAR(21) NOT NULL,
    nomClient VARCHAR(50) NOT NULL,
    prenomClient VARCHAR(50) NOT NULL,
    idCarte VARCHAR(21),
    numBoutique INT NOT NULL,
    numRue INT,
    nomRue TEXT,
    codePostal INT,
    ville TEXT,
    mail TEXT,
    tel INT,
    points INT check (points >= 0)
);

CREATE TABLE CARTES_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    userid text NOT NULL,
    idCarte VARCHAR(21) PRIMARY KEY NOT NULL,
    nomCarte VARCHAR(50),
    prixCarte INT Check (prixCarte >= 0),
    descCarte TEXT,
    numBoutique INT
);

CREATE TABLE PROMOTIONS(
    typeProduit VARCHAR(10),
    nomProduit VARCHAR(50),
    idProduit VARCHAR(21),
    points INT,
    dateDebut timestamp,
    dateFin timestamp,
    pourcentageReduction INT check (pourcentageReduction > 0),
    descEvenement TEXT
);

CREATE TABLE PROMOTIONS_audit(
    operation char(1) NOT NULL,
    stamp timestamp NOT NULL,
    typeProduit VARCHAR(10),
    nomProduit VARCHAR(50),
    idProduit Varchar(21),
    Points INT,
    dateDebut timestamp,
    dateFin timestamp,
    pourcentageReduction INT check (pourcentageReduction > 0),
    descEvenement TEXT
);