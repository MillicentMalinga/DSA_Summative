# Import dependencies
from cProfile import label
import pathlib
from matplotlib import pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
# Read dataset
from new import G

# pos = nx.circular_layout(G)
nx.draw_kamada_kawai(G)

# careers_graph = Network(directed=True,

#                     height='6000px',
#                     width='100vw',
#                     bgcolor='#222222',
#                     font_color='white'
#                     )
careers_graph = Network(directed=True, height='100vh', width='100vw')
# careers_graph.barnes_hut()
# # Take Networkx graph and translate it to a PyVis graph format
careers_graph.from_nx(G, default_node_size=50, default_edge_weight=10)
# careers_graph.show_buttons()
careers_graph.set_options('''{"nodes":
 {"font": {"size": 80 }},
 "edges": {"color": {"inherit": true},
 "smooth": false},"interaction": {"navigationButtons": true },
 "physics": {
 "minVelocity": 0.75, 
 "node_distance": "1000"
  }}''')
# # Generate network with specific layout settings
# careers_graph.repulsion(node_distance=750)

# Save and read graph as HTML file (on Streamlit Sharing)
try:
    path = '/tmp'
    careers_graph.save_graph(f'{path}/course_graph.html')
    HtmlFile = open(f'{path}/course_graph.html', 'r', encoding='utf-8')

# Save and read graph as HTML file (locally)
except:
    path = 'html_files'
    careers_graph.save_graph(f'{path}/course_graph.html')
    HtmlFile = open(f'{path}/course_graph.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=1000, width=1000)

# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://github.com/MillicentMalinga/DSA_Summative" target="_blank">GitHub Repo</a></h6>
    <h6><a href="htt/h5>ps://.medium.com" target="_blank">Medium article</a></h6>
    <h5>Created by:</h5>
    <ul>
    <li>Millicent Malinga</li>
    <li>Ntutu Sekonyela</li>
    <li>Sarah Sunday Moses</li>
    <h6>Disclaimer: The data contained here is from research done by students. The path could change according to what you want.</h6>
    """, unsafe_allow_html=True
    )
