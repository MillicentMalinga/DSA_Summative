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
# G = nx.DiGraph()
# for path in pathlib.Path("csv_files").iterdir():
#     if path.is_file():
#         current_file = open(path, "r")
        
#         data = pd.read_csv(current_file.name)

#     # Setting title

    

#     # selected_career = st.multiselect('Select Career to visualize', careers_list)
#     # selected_career = st.selectbox(
#     #      'Which career path guide would you like to see?', careers_list)

#         sources = data['CourseOne']
#         targets = data['CourseTwo']

#         edge_data = zip(sources, targets)

#         for e in edge_data:
#             src = e[0]
#             dst = e[1]

#             # G.add_node(src)
#             # G.add_node(dst)
#             G.add_edge(src, dst)
#         current_file.close()
    # G = nx.DiGraph()
# career_graph = Network()
# career_graph.from_nx(G)
# nx.draw(G)
# plt.show()
# career_graph.show('output.html')
# st.text('Showing all career paths')
# st.title('Self-taught techies Guide')
#     # Define selection options and sort alphabetically
# careers_list = ['Software Engineering', 'Data Science', 'Web Development', 'App Development']
# careers_list.sort()

# # elif selected_career:
# #     G = nx.DiGraph()

# #     for edge in edge_data:
# #         if selected_career in edge[2]:
# #             G.add_edge(edge[0], edge[1])

# nx.draw_networkx(G, labels=G.nodes)
pos = nx.circular_layout(G)
nx.draw(G,pos,node_size=2000,font_size=50) 

careers_graph = Network(directed=True,

                    height='6000px',
                    width='100vw',
                    bgcolor='#222222',
                    font_color='white'
                    )
# careers_graph = Network()
# careers_graph.barnes_hut()
# # Take Networkx graph and translate it to a PyVis graph format
careers_graph.from_nx(G)
# careers_graph.show_buttons()

# # Generate network with specific layout settings
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
