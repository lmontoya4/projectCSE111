import sqlite3
from sqlite3 import Error
#python sql setup functions
def openConnection(_dbFile):
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)
    return


#The main feature of the app
def episodeDive(conn):
    season = None
    episode = None
    print("select a season number (1-5)")
    season = int(input())
    firstEpisode = None
    lastEpisode = None
    
    #grab number of episodes in the selected season
    try:
        sql = """SELECT MIN(episodeID), MAX(episodeID) FROM episodes
                 WHERE seasonID = ?;"""
        args = [season]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        firstEpisode = rows[0][0]
        lastEpisode = rows[0][1]
    except Error as e:
        conn.rollback()
        print(e)
        print("deep dive failed due to bad input (season)")
        return

    #prompt user to pick an episode from the given season to obtain information about
    print("Select an episode ("+ str(firstEpisode) + "-" + str(lastEpisode) + ")")
    episode = int(input())

    #format the episode into string to make sql id work
    episodeArg = "owo" #temporary init value
    if len(str(episode)) == 1:
        episodeArg = "00" + str(episode)
    elif len(str(episode)) == 2: 
        episodeArg = "0" + str(episode)
    else:
        episodeArg = str(episode)

    #ALL OF THE VALUES FROM THE SELECTED EPISODE
    episodeID = None
    seasonID = None
    episode_name = None
    air_date = None
    intro_songID = None
    outro_songID = None
    primaryProtagID = None
    secondaryProtagID = None
    primaryAntagID = None
    secondaryAntagID = None

    try:
        sql = """SELECT * FROM episodes
                 WHERE episodeID = ?;"""
        args = [episodeArg]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Invalid Episode Number")
            return
        episodeID = rows[0][0]
        seasonID = rows[0][1]
        episode_name = rows[0][2]
        air_date = rows[0][3]
        intro_songID = rows[0][4]
        outro_songID = rows[0][5]
        primaryProtagID = rows[0][6]
        secondaryProtagID = rows[0][7]
        primaryAntagID = rows[0][8]
        secondaryAntagID = rows[0][9]
    except Error as e:
        conn.rollback()
        print(e)
        print("deep dive failed due to bad input (episode)")
        return

    #Display General Episode Information
    print("Season: " + str(seasonID) + "\nEpisode: " + str(episodeID))
    print("Title: " + str(episode_name))
    print("Air Date: " + str(air_date))
    
    #Intro Song Query
    introSongName = None
    if intro_songID != None:
        try:
            sql = """SELECT title FROM songs
                     WHERE songID = ?;"""
            args = [intro_songID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            if len(rows) != 0:
                introSongName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Intro Song: " + str(introSongName))
    else:
        print("Intro Song: Not Present in the Episode")

    #Outro Song Query
    outroSongName = None
    if outro_songID != None:
        try:
            sql = """SELECT title FROM songs
                     WHERE songID = ?;"""
            args = [outro_songID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            if len(rows) != 0:
                outroSongName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Outro Song: " + str(outroSongName))
    else:
        print("Outro Song: Not Present in the Episode")

    #Primary Protagoist Query
    primaryProtagName = None
    if primaryProtagID != None:
        try:
            sql = """SELECT c_name FROM characters
                     WHERE charID = ?;"""
            args = [primaryProtagID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            primaryProtagName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Primary Protagonist: " + str(primaryProtagName))
    else:
        print("Primary Protagonist: is unavailable")

    #Seconadry Protagonist Query
    secondaryProtagName = None
    if secondaryProtagID != None:
        try:
            sql = """SELECT c_name FROM characters
                     WHERE charID = ?;"""
            args = [secondaryProtagID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            secondaryProtagName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Secondary Protagonist: " + str(secondaryProtagName))

    #Primary Antagonist Query
    primaryAntagName = None
    if primaryAntagID != None:
        try:
            sql = """SELECT c_name FROM characters
                     WHERE charID = ?;"""
            args = [primaryAntagID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            primaryAntagName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Primary Antagonist: " + str(primaryAntagName))

    #Secondary Antagonist Query
    secondaryAntagName = None
    if secondaryAntagID != None:
        try:
            sql = """SELECT c_name FROM characters
                     WHERE charID = ?;"""
            args = [secondaryAntagID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            secondaryAntagName = rows[0][0]
        except Error as e:
            conn.rollback()
            print(e)
        print("Secondary Antagonist: " + str(secondaryAntagName))

    return

#Specific character input for the app
def characterInfo(conn, name):
    characterName = name
    charID = None
    birthYear = None
    charGender = None
    hairColor = None
    debutSeason = None
    try:
        sql = """SELECT * FROM characters
                WHERE c_name = ?;"""
        args = [characterName]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Invalid Character Name\n")
            return
        charID = rows[0][0]
        birthYear = rows[0][2]
        charGender = rows[0][3]
        hairColor = rows[0][4]
        debutSeason = rows[0][5]
    except Error as e:
        conn.rollback()
        print(e)  
    if charID == None:
        print("Invalid Character Name")
        return

    print("Name: " + characterName)
    if birthYear != None:
        print("Birth Year: " + str(birthYear))
    if charGender != None:
        print("Gender: " + charGender)
    if hairColor != None:
        print("Hair Color: " + hairColor)
    
    #print debut season title
    try:
        sql = """SELECT title FROM seasons
                WHERE season_number = ?;"""
        args = [debutSeason]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        print("Debut Season: " + rows[0][0])
    except Error as e:
        conn.rollback()
        print(e)

    try:
        sql = """SELECT s_name FROM stands
                WHERE charID = ?;"""
        args = [charID]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Stand: None")
        else:
            print("Stand: " + str(rows[0][0]))
    except Error as e:
        conn.rollback()
        print(e)

    #try:
     #   sql = """SELECT charID FROM namesakes
     #           WHERE charID = ?;"""
     #   args = [charID]
     #   cur = conn.cursor()
     #   cur.execute(sql, args)
     #   rows = cur.fetchall()
     #   if rows[0] != None:
    namesakeInfo(conn, characterName)
    #except Error as e:
     #   conn.rollback()
     #   print(e)

    return

#specific stand input for the app
def standInfo(conn, name):
    stand_name = name
    standID = None
    charID = None
    #name varchar(40),
    range_type = None
    ability_type = None
    form_type = None
    special_type = None
    try:
        sql = """SELECT * FROM stands
                WHERE s_name = ?;"""
        args = [name]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Invalid Stand Name")
            return
        standID = rows[0][0]
        charID = rows[0][1]
        range_type = rows[0][3]
        ability_type = rows[0][4]
        form_type = rows[0][5]
        special_type = rows[0][6]
    except Error as e:
        conn.rollback()
        print(e)
    if standID == None:
        print("Invalid Stand Name")
        return

    print("Name: " + stand_name)

    if charID != None: #get the stands user name
        try:
            sql = """SELECT c_name FROM characters
                    WHERE charID = ?;"""
            args = [charID]
            cur = conn.cursor()
            cur.execute(sql, args)
            rows = cur.fetchall()
            if rows[0][0] != None:
                print("User: " + rows[0][0])
        except Error as e:
            conn.rollback()
            print(e)
    
    if range_type != None:
        print("Range: " + range_type)
    if ability_type != None:
        print("Ability: " + ability_type)
    if form_type != None:
        print("Form: " + form_type)
    if special_type != None:
        print("Special: " + special_type)

    #try:
     #   sql = """SELECT standID FROM namesakes
     #           WHERE standID = ?;"""
     #   args = [standID]
     #   cur = conn.cursor()
     #   cur.execute(sql, args)
     #   rows = cur.fetchall()
     #   if rows[0][0] != None:
    namesakeInfo(conn, stand_name)
    #except Error as e:
     #   conn.rollback()
     #   print(e)

    return

def namesakeInfo(conn, name):
    reference = name
    charID = None
    standID = None
    song = None
    album = None
    artist = None
    genre = None

    try:
        sql = """SELECT * FROM namesakes
                WHERE reference = ?;"""
        args = [reference]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Namesake Unavailable\n")
            return
        charID = rows[0][1]
        standID = rows[0][2]
        song = rows[0][3]
        album = rows[0][4]
        artist = rows[0][5]
        genre = rows[0][6]
    except Error as e:
        conn.rollback()
        print(e)
    if charID == None and standID == None:
        print("Reference Unavailable")
        return
    else:
        print("-Namesake Info-")

    if song != None:
        print("Song: " + song)
    if album != None:
        print("Album: " + album)
    print("Artist: " + artist)
    print("Genre: " + genre)
    print()
    return

def songInfo(conn, name):
    song_name = name
    songID = None
    #title varchar(40),
    artist = None
    release_date = None

    try:
        sql = """SELECT * FROM songs
                WHERE title = ?;"""
        args = [song_name]
        cur = conn.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Invalid Song Name\n")
            return
        songID = rows[0][0]
        artist = rows[0][2]
        release_date = rows[0][3]
    except Error as e:
        conn.rollback()
        print(e)
    
    if songID == None:
        print("Song Unavailable\n")
        return
    
    print("Title: " + song_name)
    print("Artist: " + artist)
    print("Release Date: " + str(release_date))
    print()
    return

def apploop(conn):
    #the begining of the program
    print("Jojo databse :)")

    done = False
    user_selection = 0

    while not done:
        print("Enter a value to select one of the available options\n Episode Dive [1]\n Character Info [2]\n Stand Info [3]\n Song Info [4]\n Quit [0]")
        user_selection = int(input())
        if user_selection == 1:
            episodeDive(conn)

        elif user_selection == 2:
            print("Please enter the name of the character you would like the information about")
            characterInfo(conn, str(input()))

        elif user_selection == 3:
            print("Please enter the name of the stand you would like information about")
            standInfo(conn, str(input()))

        elif user_selection == 4:
            print("Please enter the name of the song you would like information about")
            songInfo(conn, str(input()))

        elif user_selection == 0:
            done = True

        else:
            print("command not recognized")
    return

def main():
    database = r"jojo_database.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        apploop(conn)
    closeConnection(conn, database)

if __name__ == '__main__':
    main()     