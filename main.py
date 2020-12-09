import sqlite3
import csv
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")




#modification queries
def updateNamesakes(_conn):
    print("updating table namesakes..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()

def updateSeasons(_conn):
    print("updating table seasons..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()   

def updateEpisodes(_conn):
    print("updating table episodes..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()

def updateStands(_conn):
    print("updating table stands..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()


def updateCharacters(_conn):
    print("updating table characters..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()

def updateSongs(_conn):
    print("updating table songs..")
    c= _conn.cursor()
    sqlToUpdate= ''''''
    c.execute(sqlToUpdate)
    _conn.commit()


#select queries
def characterInfo(_conn,name):
    c= _conn.cursor()
    createView1= '''CREATE VIEW character_season(char_name,gender,char_birthY,char_hair,season_name, isProtagonist,isAntagonist) AS
                    SELECT name,gender,birth_year,hairColor,title,
                    CASE 
                    WHEN protagonistID= charID THEN 'true'
                    ELSE 'false'
                    END AS isProtagonist,
                    CASE 
                    WHEN antogonistID= charID THEN 'true'
                    ELSE 'false'
                    END AS isAntagonist
                    FROM characters,seasons
                    WHERE debutSeason=season_number AND name='{0}';'''.format(name)
    
    
    
    createView2='''CREATE VIEW character_episodes(char_name,season_name,ep_name, isprimaryProtag,issecondaryProtag,isprimaryAntag,issecondaryAntag) AS
                    SELECT name,title,episode_name,
                    CASE 
                    WHEN primaryProtag= charID THEN 'true'
                    ELSE 'false'
                    END AS isprimaryProtag,
                    CASE 
                    WHEN secondaryProtag= charID THEN 'true'
                    ELSE 'false'
                    END AS issecondaryProtag,
                    CASE 
                    WHEN primaryAntag= charID THEN 'true'
                    ELSE 'false'
                    END AS isprimaryAntag,
                    CASE 
                    WHEN secondaryAntag= charID THEN 'true'
                    ELSE 'false'
                    END AS issecondaryAntag
                    FROM characters,seasons,episodes
                    WHERE debutSeason=season_number AND seasonID=season_number AND name='{0}'
                    GROUP BY name,title,episode_name;'''.format(name)
    
    c.execute(createView1)
    c.execute(createView2)
    sqlGETCharacter_Season_Info= "SELECT * FROM character_season;"
    c.execute(sqlGETCharacter_Season_Info)
    #[char_name,gender,char_birthY,char_hair,season_name,isProtagonist,isAntagonist]
    
    rows=c.fetchall()

    char_name= rows[0][0]
    gender=rows[0][1]
    char_birthY=rows[0][2]
    char_hair=rows[0][3]
    season_name=rows[0][4]
    isProtagonist=rows[0][5]
    isAntagonist=rows[0][6]
    print("name:  " + char_name)
    print("gender:" + gender)
    print("hair color: " + char_hair)
    print("seasons: "+ season_name)

    sqlGETCharacter_Age= "SELECT strftime('%Y','now') - char_birthY AS age FROM character_season;"
    c.execute(sqlGETCharacter_Age)
    rows=c.fetchall()
    age=rows[0][0]

    print("Age: ")
    print(age)
    
    if isProtagonist == "true":
        print("role= Protagonist")
    
    if isAntagonist== "true":
        print("role= Antagonist")
    
    #check if hes a primary protagonist, secondary protagonist, primary antagonist, secondary protagonist
    sqlGETCharacter_Episode_Info="SELECT ep_name FROM character_episodes;"
    #[char_name,season_name,ep_name, isprimaryProtag,issecondaryProtag,isprimaryAntag,issecondaryAntag]
    
    c.execute(sqlGETCharacter_Episode_Info)
    rows=c.fetchall()
    #print all episodes charter appeared in:
    print("Appeared in the following episodes:")
    counter=1
    for row in rows:
        l='Episode {} {:<20}\n'.format(counter,row[0])
        counter+=1
        print(l)
   
   
    dropView1= "DROP view character_season;"
    dropView2="DROP view character_episodes;"
    c.execute(dropView1)
    c.execute(dropView2)
    _conn.commit()

def seasonInfo(_conn,number):
    c= _conn.cursor()
    createView3='''CREATE VIEW season_characters(season_name,char_name,first_aired,last_aired,
                    isProtagonist,isAntagonist) AS
                    SELECT title,name,first_aired,last_aired,
                    CASE 
                    WHEN protagonistID= charID THEN 'true'
                    ELSE 'false'
                    END AS isProtagonist,
                    CASE 
                    WHEN antogonistID= charID THEN 'true'
                    ELSE 'false'
                    END AS isAntagonist
                    FROM characters,seasons
                    WHERE debutSeason=season_number AND season_number={0}
                    GROUP BY title,name,first_aired,last_aired;'''.format(number)
   
    createView4='''CREATE VIEW season_episodes(season_name,ep_name,intro_song_ID,outro_song_ID) AS
                SELECT title,episode_name,intro_songID,outro_songID
                FROM seasons,episodes
                WHERE season_number={0} AND season_number=seasonID
                GROUP BY title,episode_name;'''.format(number)
    
    #[season_name,char_name,first_aired,last_aired,isProtagonist,isAntagonist]
    
    c.execute(createView3)
    c.execute(createView4)
    
    c.execute("SELECT * FROM season_characters")
    rows=c.fetchall()
    name=rows[0][0]

    print("Name of Season:  "+ name)
    
    sqlGetMainProtagonist= "SELECT char_name FROM season_characters WHERE isProtagonist='true';"
    c.execute(sqlGetMainProtagonist)
    rows=c.fetchall()
    protagonist=rows[0][0]

    sqlGetMainAntagonist= "SELECT char_name FROM season_characters WHERE isAntagonist='true';"
    c.execute(sqlGetMainAntagonist)
    rows=c.fetchall()
    antagonist=rows[0][0]

    print("Main Protagonist:  "+ protagonist)
    print("Main Antagonist:  "+ antagonist)
    #characters in season
    sqlGetnumOfChars="SELECT COUNT(char_name) as num_char FROM season_characters;"
    c.execute(sqlGetnumOfChars)
    rows=c.fetchall()
    numOfChars=rows[0][0]
    print("number of characters:")
    print(numOfChars)
    sqlGetSeason_characteraInfo= "SELECT char_name FROM  season_characters;"
    c.execute(sqlGetSeason_characteraInfo)
    rows=c.fetchall()
    print("list of characters:")
    for row in rows:
        l='{}\n'.format(row[0])
        print(l)
    #episodes in season
    sqlGetnumOfEps="SELECT COUNT(ep_name) FROM season_episodes;"
    c.execute(sqlGetnumOfEps)
    rows=c.fetchall()
    numOfEps=rows[0][0]
    print("number of episodes:")
    print(numOfEps) 
    sqlGetSeason_episodesInfo= "SELECT ep_name FROM season_episodes;"
    c.execute(sqlGetSeason_episodesInfo)
    rows=c.fetchall()
    print("list of episodes:")
    count=0
    for row in rows:
        l='Episode {} : {}\n'.format(count,row[0])
        print(l)
        count+=1
    
    #songs in season
    sqlGetnumOfSongs="SELECT COUNT(DISTINCT intro_song_ID),COUNT(DISTINCT outro_song_ID) FROM season_episodes;"
    c.execute(sqlGetnumOfSongs)
    rows=c.fetchall()
    numOfSongs=rows[0][0]
    print("number of songs:")
    print(numOfSongs)
    sqlGetSeason_introSongs= "SELECT DISTINCT title,artist,release_date FROM season_episodes,songs WHERE songID= intro_song_ID;"
    c.execute(sqlGetSeason_introSongs)
    rows=c.fetchall()
    print("list of intro songs:")
    for row in rows:
        l='{}\n'.format(row[0])
        print(l)
    
    sqlGetSeason_outroSongs= "SELECT DISTINCT title,artist,release_date FROM season_episodes,songs WHERE songID=outro_song_ID;"
    c.execute(sqlGetSeason_outroSongs)
    rows=c.fetchall()
    print("list of outro songs:")
    for row in rows:
        l='{}\n'.format(row[0])
        print(l)
    
    dropView3="DROP view season_characters;"
    dropView4="DROP view season_episodes;"
    c.execute(dropView3)
    c.execute(dropView4)
    _conn.commit()


 

def main():
    database = r"data/showDB.sqlite"

    #charName= "Jonathan Joestar"
    num=1

    # create a database connection
    conn = openConnection(database)
    with conn:
        #characterInfo(conn,charName)
        seasonInfo(conn,num)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
