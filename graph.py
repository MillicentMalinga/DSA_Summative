from os import listdir
import os
import pathlib
from pyvis.network import Network
from matplotlib import pyplot as plt
import spacy
from spacypdfreader import pdf_reader
from spacy import displacy
import re
import networkx as nx
import pyvis
from pyvis.physics import *

import pandas as pd
G = nx.DiGraph()
for path in pathlib.Path("dsa_test/pdf_files").iterdir():
    if path.is_file():
        file = os.path.splitext(path.name)[0]
        current_file = open(path, "r")
       
        

        nlp = spacy.load("en_core_web_sm")
        doc = pdf_reader(current_file.name, nlp)

        pattern = r"LESSON [A-Z0-9_]\w+"
        mwt_ents = []

        for match in re.finditer(pattern, doc.text):
            start, end = match.span()
            span = doc.char_span(start, end)
            if span is not None:

                mwt_ents.append((span.text))
        # print(mwt_ents)
        courses = []
        for sent in doc.sents:
            for mwt_ent in mwt_ents:
                if mwt_ent in str(sent) and str(sent) not in courses:
                    sent = re.sub('[^a-zA-Z0-9 \n\.]', ' ', str(sent))
                    courses.append(sent)
        # print(courses)

        cleaned = []
        for course in courses:
            course = re.sub('\n\n', ',', course)
            course = re.sub('\n', '', course)
            cleaned.append(course)
        # for course in courses:
        #     print(course)
        # print(cleaned)
        final = []
        for i in cleaned:
            final.append(i.split(','))
        # print(final)
        list_of_courses = []
        for i in final:
            for k in range(len(i)):
                if i[k] in mwt_ents:
                    list_of_courses.append(i[k+1])
        # print(list_of_courses)
            
        # relation= (path.name).removesuffix()
        course_edges = []
        for i in range(len(list_of_courses) - 1):
            course_edges.append((list_of_courses[i], list_of_courses[i+1], file))

        for i in course_edges:
            G.add_edge(i[0], i[1])



        # Calling DataFrame constructor on list
        # with indices and columns specified
        df = pd.DataFrame(course_edges, columns =['CourseOne', 'CourseTwo' , 'Relation'])
        df.to_csv(f'dsa_test/csv_files/{file}.csv')
        current_file.close()

graph =  Network(directed=True,
                    height='100vh',
                    width='100vw',
                    bgcolor='#222222',
                    font_color='white'
                    )

graph.from_nx(G)
print("Drawing Graph")
pyvis.physics.Layout(graph)
graph.show('output.html')
print("Done drawing graph")
# print(G.nodes)