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
# Read dataset
G = nx.Graph(label=True)
sources = []
targets = []
list_of_tuples = []
for path in pathlib.Path("csv_files").iterdir():
    if path.is_file():
       with open(path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples.extend(list(map(tuple, csv_reader)))
for i in list_of_tuples:
    G.add_edge(i[1], i[2])
print(len(list_of_tuples))
G.name = "Careers"
print(nx.is_connected(G))
print(G.name)
net = Network()
net.from_nx(G)
net.show_buttons()
# net.show('output.html')
# print(G.nodes)
print(nx.is_tree(G))