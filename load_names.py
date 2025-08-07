import pandas

def get_from_csv():
    df = pandas.read_csv('sections/scientists.csv')
    lastnames = df ['Lastname'].tolist()
    firstname = df ['Firstname'].tolist()

    return lastnames, firstname

