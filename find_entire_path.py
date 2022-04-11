#import graph module ( implement directed graph and import module)
graph= {#lists}
#find all paths
def all(graph, entry, exit, path=[]): #function outputs list  of all paths
    path = path + [entry]
    if entry == exit:
        return path
    if not graph.has_key(entry):
        return []
    paths = []
    for node in graph[entry]:
        if node not in path:
            newpaths = all(graph, node, exit, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all()
#show graph. Import Matplotlib
