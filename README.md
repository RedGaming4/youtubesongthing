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

```bash
pip install pyautogui pymongo
