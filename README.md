# 🎹 Auto Piano Player

## **Overview**

The **Auto Piano Player** is a fun project that utilizes Python to automate the playing of songs on a virtual piano using **`pyautogui`** for key presses and **`pymongo`** for song management. This script allows users to either input their own songs or request songs stored in a MongoDB database, playing them automatically with a specified delay.

## **Features**

- **Play Your Own Song**: Input a sequence of notes to play a custom song.
- **Request a Song from Database**: Fetch and play a song stored in the MongoDB database.
- **Automated Key Presses**: Simulate piano key presses using the **`pyautogui`** library.
- **YouTube Video Integration**: Utilize YouTube videos featuring electronic piano tutorials to create and play music automatically based on their content.
- **MongoDB Integration**: Store and retrieve song data for easy access.

## **Requirements**

To run this project, you will need:

- **Python 3.x**
- **`pyautogui`** library
- **`pymongo`** library
- **MongoDB** server running locally

You can install the required libraries using pip:

## WORK IN PROGRESS

**This is all for fun wanted to do it after seeing youtube videos where you could just play a piano by pressing the numpad keys**
**fun little dumb project. Not Done.**

```bash
pip install pyautogui pymongo

How It Works
Screen Size: The script starts by printing the size of the screen.

Database Connection: Connects to a local MongoDB database named testdatabase and accesses the Songs collection.

YouTube Video Utilization: The project leverages YouTube videos featuring electronic piano tutorials to guide the song playback, allowing for dynamic music generation based on the tutorial content.

Song Input: Prompts the user to either:

Input their own song note by note.
Request a song from the database.
Playing the Song: The song is played by simulating key presses based on a mapping of notes to keyboard keys.

Delay Management: Each note has a delay to simulate realistic playing speed.

Usage
Run the script, and follow the prompts to either enter your own song or request a song from the database.

bash
Copy code
python auto_piano_player.py
Example Input
To play a song, enter the notes as numbers (1-9, 0).
To request a song, input the name of the song you wish to play.
Note Key Mapping
The notes are mapped to keyboard numbers as follows:

1: C
2: D
3: E
4: F
5: G
6: A
7: B
8: C#
9: D#
0: E
