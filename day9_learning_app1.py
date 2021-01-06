def sentence_maker(phrase):
    intr = ("how", "why", "what", "whom", "who", "where", "when")
    capitalized = phrase.capitalize()

    if phrase.startswith(intr):
        return "{}?".format(capitalized)

    else:
        return "{}.".format(capitalized)

###print(sentence_maker("have a great day"))

results = []
print("If you do not have anything to Say then you can write: NO")
while True:
    user_input = input("Say Something: ")

    if user_input == "NO":
        break
    else:
        results.append(sentence_maker(user_input))


print(" ".join(results))






