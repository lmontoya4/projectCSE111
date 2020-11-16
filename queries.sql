CREATE TABLE IF NOT EXISTS stands(
standID INT,
charID INT,
name varchar(25),
range_type varchar(25),
ability_type varchar(25),
form_type varchar(25),
special_type varchar(25),
PRIMARY KEY(standID)
);


CREATE TABLE IF NOT EXISTS characters(
charID INT,
name varchar (30),
birth_year INT,
gender varchar (6),
hairColor varchar (10),
debutSeason INT,
PRIMARY KEY(charID)
);

CREATE TABLE IF NOT EXISTS namesakes(
reference varchar(25),
charID INT,
standID INT,
song varchar(25),
album varchar(25),
artist varchar(25),
genre varchar(25),
PRIMARY KEY(reference)
);

CREATE TABLE IF NOT EXISTS seasons(
season_number INT,
title varchar(25),
protagonistID INT,
antogonistID INT,
first_aired date,
last_aired date,
PRIMARY KEY(season_number)
);

CREATE TABLE IF NOT EXISTS episodes(
episodeID INT,
seasonID INT,
episode_name varchar(25),
air_date date,
intro_songID INT,
outro_songID INT,
primaryProtag INT,
secondaryProtag INT,
primaryAntag INT,
secondaryAntag INT,
PRIMARY KEY(episodeID)
);

CREATE TABLE IF NOT EXISTS songs(
songID INT,
title varchar(25),
artist varchar(25),
release_date date,
PRIMARY KEY(songID)
);





INSERT INTO characters
VALUES
    (001, "Jonathan Joestar", 1868, "male", "blue", 1),
    (002, "Will Anthonio Zeppeli", 1838, "male", "brown", 1),
    (003, "Robert E. O. Speedwagon", 1863, "male", "blond", 1),
    (004, "Erina Joestar", 1869, "female", "blonde", 1),
    (005, "Poco", NULL, "male", "brown", 1),
    (006, "George Joestar I", NULL, "male", "blue", 1),
    (007, "Tonpetty", NULL, "male", "white", 1),
    (008, "Straizo", 1863, "male", "black", 1),
    (009, "Dire", NULL, "male", "blond", 1),
    (010, "Dio Brando", 1867, "male", "blond", 1),
    (011, "Wang Chan", 1500, "male", "black", 1),
    (012, "Jack the Ripper", NULL, "male", "auburn", 1),
    (013, "Tarkus", 1500, "male", "auburn", 1),
    (014, "Bruford", 1500, "male", "black", 1),
    (015, "Dario Brando", 1827, "male", "white", 1);


INSERT INTO stands
VALUES
    (001, 033, "Star Platinum", "close", "reconnaissance", "natural humanoid", NULL),
    (002, 034, "Magicians Red", "close", "reconnaissance", "natural humanoid", NULL),
    (003, 016, "Hermit Purple", "close", "reconnaissance", "natural non-humanoid", NULL),
    (004, 035, "Hierophant Green", "long", "reconnaissance", "artificial humanoid", NULL),
    (005, 036, "Silver Chariot", "close", NULL, "artificial humanoid", NULL),
    (006, 037, "The Fool", "close", "materialized", "artificial non-humanoid", NULL),
    (007, 010, "The World", "close", "range irrelevant", "natural-humanoid", NULL),
    (008, 055, "Tower of Gray", "long", NULL, "natural non-humanoid", NULL),
    (009, 056, "Dark Blue Moon", "close", NULL, "natural non-humanoid", NULL),
    (010, 057, "Strength", "close", "materialized", "artificial non-humanoid", NULL),
    (011, 058, "Ebony Devil", "long", "materialized", "natural non-humanoid", NULL),
    (012, 059, "Yellow Temperance", "close", "materialized", "natural non-humanoid", NULL),
    (013, 060, "Hanged Man", "long", NULL, "natural non-humanoid", NULL),
    (014, 043, "Emperor", "close", NULL, "artificial non-humanoid", NULL),
    (015, 061, "Empress", "long", "materialized", "natural humanoid", NULL),
    (016, 062, "Wheel of Fortune", "close", "materialized", "artificial non-humanoid", NULL);
INSERT INTO seasons
VALUES
    (1, "Phantom Blood", 001, 010, '2012-10-05', '2012-11-30'),
    (2, "Battle Tendency", 016, 024, '2012-12-07', '2013-04-05'),
    (3, "Stardust Crusaders", 033, 010, '2014-04-04', '2015-06-19'),
    (4, "Diamond is Unbreakable", 068, 085, '2016-04-01', '2016-12-23'),
    (5, "Golden Wind", 096, 105, '2018-10-05', '2019-07-28');

INSERT INTO episodes
VALUES
    (001, 1, "Dio the Invader", 2012-10-06, 01, 10, 001,NULL,010,NULL),

    (002, 1, "A Letter from the Past", 2012-10-12,01, 10,001,NULL,010,NULL),

    (003, 1, "Youth with Dio", 2012-10-19, 01, 10,001,NULL,010,NULL),

    (004, 1, "Overdrive", 2012-10-26, 01, 10,001,NULL,010,NULL),
    (005, 1, "The Dark Knights", 2012-11-02, 01, 10,001,NULL,010,NULL),
    (006, 1, "Pluck for Tomorrow", 2012-11-09, 01, 10,001,NULL,010,NULL),
    (007, 1, "The Successor", 2012-11-16, 01, 10,001,NULL,010,NULL),
    (008, 1, "Bloody Battle! JoJo & Dio", 2012-11-23, 01, 10,001,NULL,010,NULL),
    (009, 1, "The Final Ripple!", 2012-11-30, 01, 10,001,NULL,010,NULL);
   

INSERT INTO songs
VALUES
    (01, "JoJo ~Sono Chi no Sadame~", "Hiroaki 'TOMMY' Tominaga", '2012-11-21'),
    (02, "BLOODY STREAM", "Coda", '2013-01-30'),
    (03, "STAND PROUD", "Jin Hashimoto", '2014-04-23'),
    (04, "JoJo Sono Chi no Kioku", "JO STARS", '2015-01-28'),
    (05, "Crazy Noisy Bizarre Town", "THE DU", '2016-04-27'),
    (06, "chase", "batta", 2016-07-27),
    (07, "Great Days", "Karen Aoki & Daisuke Hasegawa",'2016-10-19'),
    (08, "Fighting Gold", "Coda", 2018-10-13),
    (09, "Uragirimono no Requiem", "Daisuke Hasegawa",'2019-03-27'),
    (10, "Roundabout", "Yes", 1971-11-26),
    (11, "Walk Like an Egyptian", "The Bangles", '1986-01-02'),
    (12, "Last Train Home", "Pat Methany Group", '1987-07-07'),
    (13, "Akuyaku Kyosoyoku", "Makoto Yasumura", '2015-01-23'),
    (14, "I Want You", "Savage Garden", '1996-05-27'),
    (15, "Freek'n You", "Jodeci", '1995-05-30'),
    (16, "Modern Crusaders", "Enigma", '2000-01-14');

INSERT INTO namesakes
VALUES 
    ("Will Anthonio Zeppeli", 002, NULL, NULL, NULL, "Led Zeppelin", "rock"),
    ("Robert E.O. Speedwagon", 003, NULL, NULL, NULL, "REO Speedwagon", "rock"),
    ("Poco", 005, NULL, NULL, NULL, "poco", "country rock"),
    ("Tonpetty", 007, NULL, NULL, NULL, "Tom Petty", "rock"),
    ("Straizo", 008, NULL, NULL, NULL, "Dire Straits", "rock"),
    ("Dire", 009, NULL, NULL, NULL, "Dire Straits", "rock"),
    ("Dio Brando", 010, NULL, NULL, NULL, "DIO", "heavy metal"),
    ("Wang Chan", 011, NULL, NULL, NULL, "Wang Chung", "new wave"),
    ("Tarkus", 013, NULL, NULL, "Tarkus", "Emerson, Lake & Palmer", "progressive rock"),
    ("Bruford", 014, NULL, NULL, NULL, "Bill Bruford", "progressive rock");



--1. List all stands with a special type (name and special type)
SELECT stands.name, stands.special_type FROM stands
WHERE stands.special_type != NULL;

--2. list all namesake songs for a given season
SELECT namesakes.song FROM namesakes
INNER JOIN stands ON stands.standID = namesakes.standID
INNER JOIN characters ON characters.charID = stands.charID
WHERE characters.debutSeason = 5 AND namesakes.song != NULL;

--3. list all namesake artists for a given season
SELECT namesakes.artist FROM namesakes
INNER JOIN stands ON stands.standID = namesakes.standID
INNER JOIN characters ON characters.charID = stands.charID
WHERE characters.debutSeason = 5;

--4. list the namesake artist for the protagonist of a given episode
SELECT artist
FROM Episodes
INNER JOIN stands ON charid = primaryProtag
INNER JOIN namesakes AS c_ns ON c_ns.charid = charid
INNER JOIN namesakes AS s_ns ON s_ns.standid = standid
WHERE episodeid = 1;

--5. list the namesake artist for the antagonist of a given episode
SELECT artist
FROM Episodes
INNER JOIN stands ON charid = primaryAntag
INNER JOIN namesakes AS c_ns ON c_ns.charid = charid
INNER JOIN namesakes AS s_ns ON s_ns.standid = standid
WHERE episodeid = 1;

--6. find the hair color of a given character
SELECT hairColor FROM characters
WHERE characters.name = "Dio Brando";

--7. find the hair colors in a given season (1) in order of frequency
SELECT hairColor, COUNT(hairColor) AS color_occurence FROM characters
WHERE debutSeason = 1
GROUP BY hairColor
ORDER BY color_occurence DESC;

--8. find the artists referenced in the show in order of frequency
SELECT artist AS artist_occurence FROM namesakes
GROUP BY artist
ORDER BY artist_occurence DESC;

--9. find the stand name and range of a given character
SELECT stands.name, stands.rangetype FROM characters
INNER JOIN characters ON characters.charID = stands.charID
WHERE characters.name = "Joseph Joestar"

--10. find the artist reference of a given stand name
SELECT artist FROM stands
INNER JOIN namesakes ON namesakes.standID = stands.standID
WHERE stands.name = "Killer Queen";


--11. Given a character, check if in which season it appeared and and in which episodes.
--name=Jonathan Joestar

SELECT title,episode_name
FROM characters,seasons,episodes
WHERE debutSeason=season_number AND debutSeason=seasonID AND name='Jonathan Joestar';

--12.how many  different intro and outro songs are in each season

SELECT title,COUNT(DISTINCT intro_songID),COUNT(DISTINCT outro_songID)
FROM seasons, episodes
WHERE season_number=seasonID
GROUP BY title; 

--13.how many characters are in each season

SELECT title,COUNT(charID) as num_char
FROM characters,seasons
WHERE season_number=debutSeason
GROUP BY title;

--14. which character were  not the protagonist or antagonist

SELECT title, name
FROM characters,seasons
WHERE season_number=debutSeason
EXCEPT 
SELECT  title, name
FROM characters,seasons
WHERE season_number=debutSeason AND (charID =protagonistID OR charID= antogonistID);


--15. Which character appeared in the most episodes and is a secondaryProtag
SELECT name,MAX(num_appeared)
FROM(
SELECT name, COUNT(name) AS num_appeared
FROM
(SELECT  title, name
FROM characters,seasons, episodes
WHERE season_number=debutSeason AND season_number=seasonID AND charID=secondaryProtag
GROUP BY title));


--16. Given a season, give information and protagonists

SELECT title,first_aired,last_aired,name AS character
FROM seasons,characters
WHERE charID= protagonistID;

--17. how many female and how many male characters are in each season->grouped


SELECT  title, gender,COUNT(name) AS num_appeared
FROM characters,seasons
WHERE season_number=debutSeason 
GROUP BY title,gender;


--18.calculate how old each character is today based on their birth_year
SELECT name, strftime('%Y','now') - birth_year AS age
FROM characters;

--19.which season is the longest

SELECT title, MAX(days_it_lasted)
FROM(
SELECT title, julianday(last_aired)- julianday(first_aired) AS days_it_lasted          
FROM seasons);

--20.which season is the shortest
SELECT title, MIN(days_it_lasted)
FROM(
SELECT title, julianday(last_aired) - julianday(first_aired) AS days_it_lasted          
FROM seasons);


--fix a specific record
UPDATE characters
SET name= 'Jonathan Joestar', debutSeason = 1
WHERE charID = 001;


--delete records
DELETE FROM characters WHERE name='Will Anthonio Zeppeli';
DELETE FROM stands WHERE standID=001;
DELETE FROM episodes WHERE episodeID=001;
DELETE FROM namesakes WHERE reference='Will Anthonio Zeppeli';

--add record(002, "Will Anthonio Zeppeli", 1838, "male", "brown", 1)
UPDATE characters
SET charID=002,name='Will Anthonio Zeppeli',birth_year=1838,
gender='male',hairColor='brown',debutSeason =1;

--add record(001,033,"Star Platinum","close","reconnaissance","natural humanoid",NULL)
UPDATE stands
SET standID=001,charID=033,name='Star Platinum',range_type='close',
ability_type='reconnaissance',form_type='natural humanoid',special_type=NULL;

--add record(001, 1, "Dio the Invader", 2012-10-06, 01, 10, 001,NULL,010,NULL)
UPDATE episodes
SET episodeID=001,seasonID=1,episode_name='Dio the Invader',air_date=2012-10-06,intro_songID=01,outro_songID=10,
primaryProtag=010,secondaryProtag=NULL,primaryAntag=010,
secondaryAntag=NULL;


--add record ("Will Anthonio Zeppeli",002, NULL, NULL, NULL,"Led Zeppelin","rock")
UPDATE namesakes
SET 
reference='Will Anthonio Zeppeli',charID=002,standID=NULL,song=NULL,
album=NULL,artist='Led Zeppelin',genre='rock';



