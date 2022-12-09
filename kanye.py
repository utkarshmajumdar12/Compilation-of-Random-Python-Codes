import requests
from tkinter import *

#Command
def get_kanye_quote():

    response = requests.get("https://api.kanye.rest")
    data = response.json()
    quote = data['quote']
    
    label_quote.config(text=quote)

#UI
window = Tk()
window.title("Kanye Quotes")

#Label-quote

label_quote = Label(text="0")
label_quote.grid(column=1, row =0)

#button
get_quote = Button(text="Get a quote", command= get_kanye_quote)
get_quote.grid(column=2, row=0)

window.mainloop()