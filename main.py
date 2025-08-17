
import speech_recognition as sr   
import webbrowser                 
import pyttsx3                    
import pywhatkit   
import google.generativeai as genai             

recognizer = sr.Recognizer() #helps to recognize the voice
engine = pyttsx3.init()      #initializing the text to speach

genai.configure(api_key="AIzaSyC2XeuXLzl0qrLipNKr_pZNhEKioMiW2oc")

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])


def speak(text):
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if c.lower().startswith("open"): # open the website when you say jarvis open google.
        site_name = c.lower().split("open", 1)[1].strip()          
        webbrowser.open(f"https://www.{site_name}.com")

    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:]) 
        pywhatkit.playonyt(song)

    elif c.lower().startswith("search"):
        query = c.lower().split("search", 1)[1].strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
        else:
            print("Please say what you want to search.")
    else:
        response = chat.send_message(c)
        speak(response.text)
        print(response.text)

if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening..!")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah")
                with sr.Microphone() as source:
                    print("What you want..!")
                    audio = r.listen(source) 
                    command = r.recognize_google(audio)

                    processCommand(command) 

        except Exception as e:
            print("error; {0}".format(e))
