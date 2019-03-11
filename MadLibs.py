# Aashir Khan
# Lab 6.1 - Mad Libs

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Enter the following information for an exhilarating story!").grid(row=1, column=0, sticky = W)

        Label(self, text="Adjective 1:").grid(row=2, column=0, sticky=W)
        self.adjective1_ent = Entry(self)
        self.adjective1_ent.grid(row=2, column=1, sticky=W)

        Label(self, text="Nationality:").grid(row=3, column=0, sticky=W)
        self.nationality_ent = Entry(self)
        self.nationality_ent.grid(row=3, column=1, sticky=W)

        Label(self, text="Name:").grid(row=4, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=4, column=1, sticky=W)

        Label(self, text="Noun:").grid(row=5, column=0, sticky=W)
        self.noun1_ent = StringVar()
        self.noun1_ent.set(None)
        nouns1 = ["garbage", "mud", "snow"]
        column = 1
        for part in nouns1:
            Radiobutton(self, text=part, variable=self.noun1_ent, value=part).grid(row=5, column=column, sticky=W)
            column += 1

        Label(self, text="Adjective(s) 2:").grid(row=6, column=0, sticky=W)
        self.is_thin = BooleanVar()
        Checkbutton(self, text="thin", variable=self.is_thin).grid(row=6, column=1, sticky=W)
        self.is_fluffy = BooleanVar()
        Checkbutton(self, text="fluffy", variable=self.is_fluffy).grid(row=6, column=2, sticky=W)
        self.is_round = BooleanVar()
        Checkbutton(self, text="round", variable=self.is_round).grid(row=6, column=3, sticky=W)

        Label(self, text="Adjective 3:").grid(row=7, column=0, sticky=W)
        self.adjective3_ent = Entry(self)
        self.adjective3_ent.grid(row=7, column=1, sticky=W)

        Label(self, text="Adjective 4:").grid(row=8, column=0, sticky=W)
        self.adjective4_ent = Entry(self)
        self.adjective4_ent.grid(row=8, column=1, sticky=W)

        Label(self, text="Topping(s):").grid(row=9, column=0, sticky=W)
        self.pancakes = BooleanVar()
        Checkbutton(self, text="pancakes", variable=self.pancakes).grid(row=9, column=1, sticky=W)
        self.bananas = BooleanVar()
        Checkbutton(self, text="bananas", variable=self.bananas).grid(row=9, column=2, sticky=W)
        self.tacos = BooleanVar()
        Checkbutton(self, text="tacos", variable=self.tacos).grid(row=9, column=3, sticky=W)

        Label(self, text="Number:").grid(row=10, column=0, sticky=W)
        self.number_ent = Entry(self)
        self.number_ent.grid(row=10, column=1, sticky=W)

        Label(self, text="Place:").grid(row=11, column=0, sticky=W)
        self.place_ent = StringVar()
        self.place_ent.set(None)
        place = ["toilet", "grill", "landfill"]
        column = 1
        for part in place:
            Radiobutton(self, text=part, variable=self.place_ent, value=part).grid(row=11, column=column, sticky=W)
            column += 1

        Button(self, text="Click for story", command=self.story).grid(row=12, column=0, sticky=W)
        self.story_txt = Text(self, width=100, height=20, wrap=WORD)
        self.story_txt.grid(row=14, column=0, columnspan=2)

    def story(self):
        adjective1 = self.adjective1_ent.get()
        adjective3 = self.adjective3_ent.get()
        adjective4 = self.adjective4_ent.get()
        nationality = self.nationality_ent.get()
        name = self.person_ent.get()
        noun = self.noun1_ent.get()
        number = self.number_ent.get()
        place = self.place_ent.get()
        adjective2 = ""
        toppings = ""

        if self.is_fluffy.get():
            adjective2 += "fluffy, "
        if self.is_thin.get():
            adjective2 += "thin, "
        if self.is_round.get():
            adjective2 += "round, "

        if self.pancakes.get():
            toppings += "pancakes, "
        if self.bananas.get():
            toppings += "bananas, "
        if self.tacos.get():
            toppings += "tacos,"

        story = "Pizza was invented by " + adjective1.lower() + " " + nationality.title() + " named " + name.title() + \
                ". " + "To make pizza, you need to take a lump of " + noun + "," + " and make a " + adjective2 \
                + "and moist circle. Then you cover it with " + adjective3.lower() + " sauce, " + adjective4.lower() + \
                " cheese, and freshly chopped " + toppings + "and peppers. " + "Next you have to bake it at " + number \
                + " degrees in a " + place +". " + "Now you are done! Enjoy the pizza!"

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


root = Tk()
root.title("Pizza Mad Lib")
app = Application(root)
root.mainloop()