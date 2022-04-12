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
careers_list = ['Software Engineering', 'Data Science', 'Web Developer', 'Mobile App Developer']
careers_list.sort()

selected_careers = st.multiselect('Select Career to visualize', careers_list)

# Set info message on initial site load
if len(selected_careers) == 0:
    sources = data['Course_from']
    targets = data['Course_to']
    weights = data['weight']

    # creating graph
    G = nx.DiGraph()
    edge_data = zip(sources, targets)

    for e in edge_data:
        src = e[0]
        dst = e[1]

        # G.add_node(src)
        # G.add_node(dst)
        G.add_edges_from(edge_data)

    # G = nx.DiGraph()
    st.text('Choose at least 1 career path to view')

# Create network graph when user selects >= 1 item
# else:
#     df_select = data.loc[data['Course_from'].isin(selected_careers) | \
#                                 data['Course_to'].isin(selected_careers)]
#     df_select = df_select.reset_index(drop=True)

#     # Create networkx graph object from pandas dataframe
#     G = nx.from_pandas_edgelist(df_select, 'Course_from', 'Course_to', 'weight')

    # Initiate PyVis network object
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
    <h6><a href="https://github.com/kennethleungty/Pyvis-Network-Graph-Streamlit" target="_blank">GitHub Repo</a></h6>
    <h6><a href="https://kennethleungty.medium.com" target="_blank">Medium article</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
    )
