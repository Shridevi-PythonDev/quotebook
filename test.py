def sentence_maker(phrase):
    interrogatives = ("how", "why", "what")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(sentence_maker('how are you doing'))

import pandas
df1  = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Name","Age","Value"],index=['first','second'])
print(df1)

df2 = pandas.DataFrame([{"Name":"Sam", "Surname":"Singh"},{"Name":"Hari"}])
print(df2)

print(type(df1))
print(dir(df1))
print(df1.mean())
print(df1.mean().mean())
print(type(df1.mean()))
print(df1)
print(df1.Age)
print(type(df1.Age))
print(df1.Age.max())
print(df1.Age.mean())
