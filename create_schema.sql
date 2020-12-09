CREATE TABLE stands(
standID INT,
charID INT,
s_name varchar(40),
range_type varchar(25),
ability_type varchar(25),
form_type varchar(25),
special_type varchar(25)
);

CREATE TABLE characters(
charID INT,
c_name varchar (40),
birth_year INT,
gender varchar (15),
hairColor varchar (10),
debutSeason INT
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
antagonistID INT,
first_aired date,
last_aired date
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
secondaryAntag INT
);

CREATE TABLE songs(
songID INT,
title varchar(40),
artist varchar(40),
release_date date
);