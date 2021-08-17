"""Note that any terms in the antiSlurs.txt file that are deemed condescending, racially, religiously,
politcally, and/or sexually objectionable are not meant to demonsrate that we mean any of those things
but for the sake of the bot being able to delete those messages from the server"""

def slur():
    with open("antiSlurs") as file:
        lines = file.read().splitlines() # Gives List of string values
        return lines
