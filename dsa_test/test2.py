# Import dependencies
from cProfile import label
from csv import reader
import pathlib
from matplotlib import pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

sources = []
targets = []
list_of_tuples = []
for path in pathlib.Path("csv_files").iterdir():
    if path.is_file():
       with open(path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        next(csv_reader)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples.extend(list(map(tuple, csv_reader)))
for i in list_of_tuples:
    sources.append(i[1])
    targets.append(i[2])
values = []
color = []
for i in range(340):
    values.append(1)
    color.append('red')
G = Network()
G.add_nodes(sources, value=values, color=color, label=sources)
for i in list_of_tuples:
    G.add_edge(i[1], i[2])
G.show('output.html')