from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import sqlite3


QUESTION_PROMPT = """
THE PROGRAMMING LANGUAGE POLLS

What would you like to do?

 - 1 to add a language
 - 2 to remove a language
 - 3 to vote a language
 - 4 to get all languages
 - 5 to exit
"""


class Poll:
    CREATE_POLLS_TABLE = """CREATE TABLE IF NOT EXISTS polls(language, votes)"""
    DATABASE = "polls.db"
    CONN = sqlite3.connect(DATABASE)
    CUR = CONN.cursor()

    def __init__(self):
        self.CUR.execute(self.CREATE_POLLS_TABLE)

    def add_language(self, language):
        self.CUR.execute("INSERT INTO polls VALUES(?, 0)", (language.lower(),))
        self.CONN.commit()
        mb.showinfo("Success", "Language added")

    def remove_language(self, language):
        self.CUR.execute("DELETE FROM polls WHERE language=?", (language.lower(),))
        self.CONN.commit()
        mb.showinfo("Success", "Language removed")

    def vote_language(self, language):
        self.CUR.execute(
            "UPDATE polls SET votes=votes+1 WHERE language=?", (language.lower(),)
        )
        self.CONN.commit()
        self.get_all_languages()

    def get_all_languages(self):
        self.CUR.execute("SELECT * FROM polls")
        dbobj = self.CUR.fetchall()
        text = ""
        for language in dbobj:
            text += f"{language[0]}: {language[1]} Votes\n"
        mb.showinfo("Result", text)


if __name__ == "__main__":
    p = Poll()
    while True:
        option = sd.askinteger(
            "Question",
            QUESTION_PROMPT,
            minvalue=1,
            maxvalue=5,
        )
        if option == 1:
            language = sd.askstring("Question", "Enter the language to add")
            p.add_language(language)
        elif option == 2:
            language = sd.askstring("Question", "Enter the language to remove")
            p.remove_language(language)
        elif option == 3:
            language = sd.askstring("Question", "Enter the language to vote")
            p.vote_language(language)
        elif option == 4:
            p.get_all_languages()
        elif option == 5 or option is None:
            p.CONN.close()
            break;
