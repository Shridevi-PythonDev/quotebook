#### Enter multiple user inputs. Seperate sentences with "." or "?" depending on the interogatives and capitalize the first word

def sentence_maker(phrase):
    interogatives = ("how", "why", "what", "where", "whose")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []

print("If you don't have anything to Say then write : NO ")
while True:
    
    user_input = input("Say Something: ")
    if user_input == "NO":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))


