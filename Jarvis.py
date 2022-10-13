import speech_recognition as sr
import pyttsx3
import webbrowser
import os

class Jarvis:

    text = "Hello Sir"

    def text_to_speech(self, statement):
        engine = pyttsx3.init()
        engine.say(statement)
        engine.runAndWait()

    r1 = sr.Recognizer()

    application_dict = {
        "google chrome": "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "university": "D:\BRACU\Fall2021",
        "python": "C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3/bin/pycharm64.exe",
        "entertainment": "E:/",
        "movies": "E:\Movies",
        "projects": "F:\Projects",
        "system": "C:/"

    }

    website_dict = {
        "youtube": "https://www.youtube.com/",
        "facebook": "https://www.facebook.com/",
        "university": "https://bux.bracu.ac.bd/dashboard",
        "google drive": "https://drive.google.com/drive/u/0/my-drive"
    }

    def open_application(self, app):
        print("application is: ", app)
        if app in self.application_dict.keys():
            os.startfile(self.application_dict[app])
        else:
            print("Application not found, try again please")
            self.text_to_speech("Application not found, try again please")
            self.text = "Application not found, try again please"

    def open_website(self, website):
        if website in self.website_dict.keys():
            os.startfile(self.website_dict[website])
        else:
            print("Website not found try again please")
            self.text_to_speech("Website not found try again please")

    def search_website(self, search):
        print("here")
        os.startfile("https://www.google.com/search?q="+search)

    function_dict = {
        "open application": open_application,
        "open website": open_website,
        "search website": search_website,
    }

    function_dict_keys = list(function_dict.keys())

    def start(self):

        while True:
            with sr.Microphone() as request_source:
                try:
                    print("request your command sir", self.function_dict_keys)
                    self.text_to_speech("request your command sir")
                    listening_to_request = self.r1.listen(request_source, phrase_time_limit=10)
                    recognizing_request = (self.r1.recognize_google(listening_to_request))
                    recognizing_request = str(recognizing_request).lower()
                    print(recognizing_request)
                    self.text = recognizing_request

                    if "open application" in recognizing_request:
                        param = str(recognizing_request).replace("open application ", "")
                        self.function_dict["open application"](self, param)
                    elif "open website" in recognizing_request:
                        param = str(recognizing_request).replace("open website ", "")
                        self.function_dict["open website"](self, param)
                    elif "search website" in str(recognizing_request).lower():
                        param = recognizing_request.replace("search website ", "")
                        print("Param", param)
                        os.startfile("https://www.google.com/search?q="+param)
                    elif recognizing_request in ["no", "end task", "bye bye"]:
                        self.text_to_speech("Thank you for using me, take care")
                        break

                    # if recognizing_request+"" in self.function_dict_keys:
                    #     self.function_dict[recognizing_request+""](self)
                    # elif recognizing_request in ["no", "end task", "bye bye"]:
                    #     self.text_to_speech("Thank you using me, take care")
                    #     break
                    # else:
                    #     self.text_to_speech("Sir I did not understand")
                    #     print("Sir I did not understand")

                    # self.text_to_speech("Would you like me do some thing else")
                    # print("Would you like me do some thing else")
                    # listening_to_request = self.r1.listen(request_source, phrase_time_limit=5)
                    # recognizing_request = (self.r1.recognize_google(listening_to_request))+""
                    # print(recognizing_request.lower())
                    #
                    # if recognizing_request in ["no", "end task", "bye bye"]:
                    #     self.text_to_speech("Thank you using me, take care")
                    #     break
                    # elif recognizing_request in ["yes", "ok"]:
                    #     continue

                except():
                    print("Sorry could not understand you ")
                    break


# jarvis = Jarvis()

# jarvis.start()
# jarvis.start()