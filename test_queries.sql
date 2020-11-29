--1. List all stands with a special type (name and special type)
SELECT stands.name, stands.special_type FROM stands
WHERE special.special_type != NULL;

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
INNER JOIN stand ON charid = primaryProtag
INNER JOIN namesake AS c_ns ON c_ns.charid = charid
INNER JOIN namesake AS s_ns ON s_ns.standid = standid
WHERE episodeid = 1;

--5. list the namesake artist for the antagonist of a given episode
SELECT artist
FROM Episodes
INNER JOIN stand ON charid = primaryAntag
INNER JOIN namesake AS c_ns ON c_ns.charid = charid
INNER JOIN namesake AS s_ns ON s_ns.standid = standid
WHERE episodeid = 1;

--6. find the hair color of a given character
SELECT hairColor FROM characters
WHERE characters.name = "Dio Brando";

--7. find the hair colors in a given season (1) in order of frequency
SELECT hairColor, COUNT(hairColor) AS color_occurence FROM characters
WHERE debutSeason = 1
GROUP BY hairColor
ORDER BY color_occurnce DESC;

--8. find the artists referenced in the show in order of frequency
SELECT artist AS artist_occurence FROM namesakes
GROUP BY artist
ORDER BY artist_occurnce DESC;

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

