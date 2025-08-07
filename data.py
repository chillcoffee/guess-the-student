import pandas

question_data = []

df = pandas.read_csv('sections/scientists.csv')
lastnames = df ['Lastname'].tolist()
firstnames = df ['Firstname'].tolist()


for i in range(len(lastnames)):
    dict_name = {}
    dict_name['lastname'] = lastnames[i]
    dict_name['firstname'] = firstnames[i]
    question_data.append(dict_name)

print(question_data)
