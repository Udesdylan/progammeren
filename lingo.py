from multiprocessing import connection
import sqlite3
class Lingo():


    #Constructor
    def __init__(self):

        self.woord = str.lower (self.set_woord())
        self.beurt = 1
    
    def set_woord(self):
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.execute("SELECT * FROM vijfletters ORDER BY RANDOM()")
        for row in cursor:
            woord = row[0]
        connection.close()
        return woord

    def validate_input(self, invoer):
        
        self.beurt +=1

        #converteer invoer naar kleine letters
        invoer = str.lower(invoer)

        #controleer of invoer gelijk is aan het woord

        if (invoer == self.woord):

            return "Gewonnen"

        #controleer op 5 letter woord

        if (len(invoer)) != 5:

            return "Voer een woord in van 5 letters!"

        #vergelijk elke letter van de invoer met het woord

        uitvoer = ""

        for i in range(5):

            if (invoer[i] == self.woord[i]):

                uitvoer += str.upper(invoer[i])

            elif (invoer[i] in self.woord):

                uitvoer += invoer[i]

            else:

                uitvoer += "_"

        return uitvoer

        #Geef uitvoer string terug

        return "OK"
