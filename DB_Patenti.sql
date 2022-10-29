drop table if exists DatiPatenti;

create table DatiPatenti 
(
	Codice 	  		char(10) primary key,
	Nome 	  		varchar(20),
	Cognome	  		varchar(20),
	DataNascita 	date,
	LuogoNascita 	varchar(50),
	Tipo 			varchar(20),
	EnteEmettitore 	varchar(10),
	DataEmissione 	date,
	DataScadenza 	date,
	Foto			bytea,
	SecretID		varchar(10) primary key,
	ChiavePrivata	decimal,
	N				decimal,
);

insert into DatiPatenti values 	('UD1234567A',	'Marco',	'Rossi',	'1991-01-01',	'Udine',		'B',	'MC-UD',	'2020-02-20',	'2030-01-01',	'WM562WT1FM'),
								('UD2345678B',	'Maria',	'Bianchi',	'1992-02-02',	'Udine',		'A-B',	'MC-UD',	'2019-03-21',	'2029-02-02',	'HO781EI7BK'),
								('UD3456789C',	'Mario',	'Verdi',	'1993-03-03',	'Udine',		'A-B',	'MC-UD',	'2020-04-22',	'2030-03-03',	'HE814DH6WK'),
								('UD4567890D',	'Luca',		'Gialli',	'1994-04-04',	'Palmanova',	'B',	'MC-UD',	'2021-05-23',	'2031-04-04',	'UO321ZL7NW'),
								('UD5678901E',	'Giulia',	'Neri',		'1995-05-05',	'San Daniele',	'B',	'MC-UD',	'2022-06-24',	'2032-05-05',	'JL682MH1PT'),
								('UD6789012F',	'Monica',	'Viola',	'1996-06-06',	'San Daniele',	'B',	'MC-UD',	'2022-07-25',	'2032-06-06',	'YJ478NW6SD'),
								('UD7890123G',	'Giacomo',	'Rosa',		'1997-07-07',	'Palmanova',	'B',	'MC-UD',	'2018-08-26',	'2028-07-07',	'DY665QL6AU'),
								('UD8901234H',	'Fabio',	'Blu',		'1998-08-08',	'Gorizia',		'A-B',	'MC-GO',	'2018-09-27',	'2028-08-08',	'TU334QD1KS'),
								('UD9012345I',	'Luigi',	'Grigi',	'1999-09-09',	'Trieste',		'B',	'MC-TS',	'2019-10-28',	'2029-09-09',	'ND742XB5CW'),
								('UD0123456J',	'Aldo',		'Azzurri',	'2000-10-10',	'Udine',		'B',	'MC-UD',	'2020-11-29',	'2030-10-10',	'AN321WM1ER');