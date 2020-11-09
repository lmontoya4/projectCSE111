CREATE TABLE stands(
standID INT,
charID INT,
name varchar(25),
range_type varchar(25),
ability_type varchar(25),
form_type varchar(25),
special_type varchar(25)
PRIMARY KEY(standID),
);


CREATE TABLE characters(
charID INT,
name varchar (30),
birth_year INT,
gender varchar (6),
hairColor varchar (10),
debutSeason INT,
PRIMARY KEY(charID)
);

CREATE TABLE namesakes(
reference varchar(25),
charID INT,
standID INT,
song varchar(25),
album varchar(25),
artist varchar(25),
genre varchar(25)
);

CREATE TABLE seasons(
season_number INT,
title varchar(25),
protagonistID INT,
antogonistID INT,
first_aired date,
last_aired date,
PRIMARY KEY(season_number)
);

CREATE TABLE episodes(
episodeID INT,
seasonID INT,
air_date date,
intro_songID INT,
outro_songID INT,
primaryProtag INT,
primaryProtagStand INT,
secondaryProtag INT,
secondaryProtagStand INT,
primaryAntag INT,
primaryAntagStand INT,
secondaryAntag INT,
secondaryAntagStand INT,
PRIMARY KEY(episodeID),
FOREIGN KEY (intro_songID) REFERENCES songs(songID),
FOREIGN KEY (outro_songID) REFERENCES songs(songID)
);

CREATE TABLE songs(
songID INT,
tittle varchar(25),
artist varchar(25),
release_date date,
PRIMARY KEY(songID)
);
