import csv
import spacy
import pandas as pd
import textacy

queries = pd.read_csv('noun_input.csv')
queries_list = [queries.columns.values.tolist()] + queries.values.tolist()

projectOutput = input("Enter a name for this project folder: ")
outputcsv = projectOutput +".csv"
f = csv.writer(open(outputcsv, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL","Question","Nouns"])

nlp =spacy.load("en_core_web_sm")

patterns = [[{"POS": "ADV"}, {"POS": "VERB"}],[{"POS": "VERB"}, {"POS": "ADV"}],[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "ADV"}]]


for query in queries_list:
    url = query[0]
    question = query[1]
    doc = nlp(question)
    nouns = list(doc.noun_chunks)
    verbs = []
    verb_phrases = textacy.extract.token_matches(doc, patterns=patterns)
    for verb_phrase in verb_phrases:
        verbs.append(verb_phrase)
    f.writerow([url,question,nouns,verbs])