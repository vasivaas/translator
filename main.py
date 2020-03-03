import requests
import json
import tkinter as tk

win = tk.Tk()
win.title("Translator v2.0")
win.geometry("250x100")

class Translate:
    URL_PATH = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
    KEY = "trnsl.1.1.20200124T162732Z.8f2dc5ca095fdbc6.0b4daffb305365be376f12ac6d759fd1cc54f436"

    def __init__(self,lang):
        self.url = Translate.URL_PATH
        self.key = Translate.KEY
        self.lang = lang

    def translate(self):
        datas = {'key': self.key, 'lang': self.lang, 'text': self.text}
        r = requests.post(self.url, data=datas)
        if json.loads(r.text)['code'] == 200:
            word = json.loads(r.text)['text'][0]
            if self.text == word:
                return "Not found"
            else:
                return word
        else:
            return False

    def translation(self):
        self.text = entry.get()
        label1 = tk.Label(win, text=f"Translate : {self.translate()}", bg="white")
        label1.grid(row=2, column=0)


en_uk = Translate(lang="en-uk")
uk_en = Translate(lang="uk-en")

label = tk.Label(win, text="Enter Word :")
label.grid(row=0, column=0, sticky="W")

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="Translate en-uk", command=en_uk.translation)
button.grid(row=1, column=2)

button1 = tk.Button(win, text="Translate uk-en", command=uk_en.translation)
button1.grid(row=2, column=2)

win.mainloop()
