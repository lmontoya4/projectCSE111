CREATE TABLE stands(
standID INT,
charID INT,
name varchar(40),
range_type varchar(25),
ability_type varchar(25),
form_type varchar(25),
special_type varchar(25)
PRIMARY KEY(standID),
);


CREATE TABLE characters(
charID INT,
name varchar (40),
birth_year INT,
gender varchar (6),
hairColor varchar (10),
debutSeason INT,
PRIMARY KEY(charID)
);

CREATE TABLE namesakes(
reference varchar(40),
charID INT,
standID INT,
song varchar(40),
album varchar(40),
artist varchar(40),
genre varchar(40)
);

CREATE TABLE seasons(
season_number INT,
title varchar(40),
protagonistID INT,
antogonistID INT,
first_aired date,
last_aired date,
PRIMARY KEY(season_number)
);

CREATE TABLE episodes(
episodeID INT,
seasonID INT,
episode_name varchar(40),
air_date date,
intro_songID INT,
outro_songID INT,
primaryProtag INT,
secondaryProtag INT,
primaryAntag INT,
secondaryAntag INT,
PRIMARY KEY(episodeID),
FOREIGN KEY (intro_songID) REFERENCES songs(songID),
FOREIGN KEY (outro_songID) REFERENCES songs(songID)
);

CREATE TABLE songs(
songID INT,
title varchar(40),
artist varchar(40),
release_date date,
PRIMARY KEY(songID)
);