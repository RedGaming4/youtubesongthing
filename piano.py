import time
import pyautogui
import pymongo


print(pyautogui.size())


def create_db(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    testdb = myclient["testdatabase"]

    mydata = testdb["Songs"]

    y = mydata.insert_one(mydict)

    all_songs = mydata.find()

    print("{mydict} has been added to the DB")
    print(mydata)
    print(testdb.list_collection_names())
    for song in all_songs:
        print(song)
    return mydata


def play_song(songs):
    for note in songs:
        if note in note_key_mapping:
            pyautogui.press(note_key_mapping[note])
            time.sleep(delay)

def get_input_():
    song = []  # array to store the song the user inputted
    user_input = input("""          
          What would you like to do?
          Press [1] to play your own song.
          Press [2] to request a song from DB
          """)
    
    if user_input == '1':
        for i in range(8):
            line = input(f"Line {i + 1} ")
            song.append(line)

        return song
    elif user_input == '2':
        i = input("What is the name of the song? ")

        return []


def main():
    #mydict = {
        #"Song Name": "Sunshine",
        #"Notes": [
            #"25677",
            #"76755",
            #"56780",
            #"09875",
            #"567",
            #"87665"
        #]
    #}

    song_lines = get_input_()

    if song_lines:
        song_sequence = ''.join(song_lines)
        song_list = list(song_sequence)
        play_song(song_list)

delay = 0.35
note_key_mapping = { 
    '1': '1',  # C
    '2': '2',  # D
    '3': '3',  # E
    '4': '4',  # F
    '5': '5',  # G
    '6': '6',  # A
    '7': '7',  # B
    '8': '8',  # C#
    '9': '9',  # D#
    '0': '0',  # E
}


main()