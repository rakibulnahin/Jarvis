# import speech_recognition as sr
#
# r1 = sr.Recognizer()
#
# def open_application(app):
#     print("open application", app)
#
# def open_website(app):
#     print("open application", app)
#
# def search_website(app):
#     print("open application", app)
#
# while True:
#     with sr.Microphone() as source:
#         print("say first")
#         s = r1.listen(source, phrase_time_limit=5)
#         rocg = r1.recognize_google(s)
#         print("first", rocg)
#         if rocg == "bye":
#             break
#         elif "open application" in rocg:
#             param = rocg.replace("open application ", "")
#             open_application(param)

