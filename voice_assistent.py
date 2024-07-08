
import requests
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import webbrowser
import wolframalpha
from selenium import webdriver
import pywhatkit
import pyautogui
import time
from bs4 import BeautifulSoup
from googletrans import Translator


translator = Translator()


num = 1

# Function to speak output
def assistant_speaks(output):
    global num

    num += 1
    print("Assistant: ", output)

    
    convert_to_speak = gTTS(text=output, lang='en', slow=False)
    
   
    file = f"output{num}.mp3"
    convert_to_speak.save(file)

 
    playsound.playsound(file, True)

    
    os.remove(file)

# Function to get user audio input
def get_audio():
    recognizer = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Listening...")
        
        try:
            audio = recognizer.listen(source, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            pass

    print("Stop listening.")

    try:
       
        text = recognizer.recognize_google(audio, language='en').lower()
        print( text)
        return text

    except Exception as e:
        assistant_speaks("I couldn't understand you , please try again!")
        return 0

def process_text(input_text):
    try:
        if "search" in input_text:
            search_web(input_text)
        elif "translate" in input_text:
            translate_text(input_text)
        elif "weather" in input_text:
            assistant_speaks("Sure, please tell me the name of the city.")
            city = get_audio().lower()
            print("City:", city)
            get_weather(city)
        elif "who are you" in input_text  in input_text:
            speak = 'Hello, I am your personal assistant.'
            assistant_speaks(speak)
        elif "who made you" in input_text or "created you" in input_text:
            speak = "You made me."
            assistant_speaks(speak)
        elif "calculate" in input_text.lower():
            app_id = "YOUR_WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)
            indx = input_text.lower().split().index('calculate')
            query = input_text.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
        elif 'open' in input_text:
            open_application(input_text)
       
    except Exception as e:
        assistant_speaks("I don't understand, I can search the web for you, do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input_text)

# Function to perform web search
def search_web(input_text):
    driver = webdriver

    if 'youtube' in input_text.lower():
        assistant_speaks("Opening in YouTube")
        indx = input_text.lower().split().index('youtube')
        query = input_text.split()[indx + 1:]
        driver.open("http://www.youtube.com/results?search_query=" + '+'.join(query))
    elif 'wikipedia' in input_text.lower():
        assistant_speaks("Opening Wikipedia")
        indx = input_text.lower().split().index('wikipedia')
        query = input_text.split()[indx + 1:]
        driver.open("https://en.wikipedia.org/wiki/" + '_'.join(query))
    
        

# Function to open applications
def open_application(input_text):
    if "firefox" in input_text or "mozilla" in input_text:
        assistant_speaks("opening Mozilla Firefox")
        os.popen('/usr/bin/firefox')
    else:
        assistant_speaks("Application not available")


# Function to get weather information for a city
def get_weather(city):
    try:
        # Set the language parameter to request English language
        params = {
            "city": f"weather in {city}",
            "language": "en"
        }

       
        weather_url = "https://www.google.com/search"

       
        response = requests.get(weather_url, params=params)

      
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')

            
            location = soup.find('div', class_='BNeawe iBp4i AP7Wnd').get_text()
            temperature = soup.find('div', class_='BNeawe tAd8D AP7Wnd').get_text()

            result = f"Weather in {location}: {temperature}"
            print("Weather Result:", result)  
            assistant_speaks(result)
        else:
            assistant_speaks("Error: Unable to fetch weather information.")

    except Exception as e:
        assistant_speaks(f"Error: {str(e)}")

# Function to translate text
def translate_text(input_text):
    try:
        assistant_speaks("What is the text to translate?")
        text_to_translate = get_audio()
        assistant_speaks("To which language?")
        target_language = get_audio()
        
        if target_language == 'German':
            target_language = 'de'
        elif target_language == 'French':
            target_language = 'fr'
        
        translation = translator.translate(text_to_translate, dest=target_language)
        assistant_speaks(f"Translated text: {translation.text}")
    except Exception as e:
        assistant_speaks(f"Translation error: {str(e)}")

if __name__ == "__main__":
    # assistant_speaks("Hello! How can I assist you?")
    assistant_speaks("hello mohamed khedr ")
    while True:
        assistant_speaks("how can i help you ")
        user_input = get_audio()
        
        if "exit" in user_input or "bye" in user_input in user_input:
            assistant_speaks("Goodbye!")
            break
        
        process_text(user_input)
        