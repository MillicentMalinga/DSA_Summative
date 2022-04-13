# Import dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
# Read dataset
data = pd.read_csv('data/data.csv')

# Setting title

st.title('Self-taught techies Guide')
# Define selection options and sort alphabetically
careers_list = ['Software Engineering', 'Data Science', 'Web Development', 'App Development']
careers_list.sort()

# selected_career = st.multiselect('Select Career to visualize', careers_list)
selected_career = st.selectbox(
     'Which career path guide would you like to see?', careers_list)

sources = data['Course_from']
targets = data['Course_to']
career = data['is_prerequisite_of']
edge_data = zip(sources, targets, career)

# Set info message on initial site load
if selected_career is None:
    
    # weights = data['weight']

    # creating graph
    G = nx.DiGraph()
    

    for e in edge_data:
        src = e[0]
        dst = e[1]

        # G.add_node(src)
        # G.add_node(dst)
        G.add_edge(src, dst)

    # G = nx.DiGraph()
    st.text('Showing all career paths')

elif selected_career:
    G = nx.DiGraph()

    for edge in edge_data:
        if selected_career in edge[2]:
            G.add_edge(edge[0], edge[1])



careers_graph = Network(directed=True,
                    height='1000px',
                    width='750px',
                    bgcolor='#222222',
                    font_color='white'
                    )

# Take Networkx graph and translate it to a PyVis graph format
careers_graph.from_nx(G)

# Generate network with specific layout settings
careers_graph.repulsion(
                    node_distance=420,
                    central_gravity=0.33,
                    spring_length=110,
                    spring_strength=0.10,
                    damping=0.95
                    )

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
components.html(HtmlFile.read(), height=435)

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
