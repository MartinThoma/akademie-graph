#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# EXPLANATION:
# This file reads in the people.csv and the files from the /data folder, and
# uses these data to create the nodes-and-edges.js.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# LIBRARIES
# -----------------------------------------------------------------------------

import numpy as np



# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

class Node():
    """
    This class is used to represent nodes of the graph, i.e. people.
    """

    def __init__(self, id, name, major, group):

        # Basic properties
        self.id = id
        self.name = name
        self.major = major
        self.group = group

        # Complex properties that need to be calculated
        self.knows = 0
        self.known_by = 1



# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

def LightColor(group):
    colors = {1: '#F4Bf98', 
              3: '#E89885', 
              4: '#DBA1BB', 
              5: '#98B7F4', 
              6: '#84BBBF', 
              7: '#8DC9AF'}
    return colors[group]



def DarkColor(group):
    colors = {1: '#D86612',
              3: '#E23507',
              4: '#552437',
              5: '#234587',
              6: '#08545E',
              7: '#0A4F34'}
    return colors[group]



def create_adjacency_matrix(n_people):
    """
    This function loops over all files in /data and creates the adjacency
    matrix from it.
    """
    adjacency_array = []
    for i in range(n_people):
        row = np.loadtxt('./data/{}.csv'.format(i), usecols=[1])
        adjacency_array.append(row)
    return np.matrix(adjacency_array)



def get_node_by_id(list_of_nodes_, id):
    for node in list_of_nodes_:
        if node.id == id:
            return node


def create_nodes_and_edges(list_of_nodes_, adjacency_matrix_):
    """
    This function takes the list of nodes and the list of edges and creates
    the JSON file from them.
    """

    # Update the nodes: Every node gets told how many other nodes know it
    for node in sorted(list_of_nodes_, key=lambda x: x.id):
        node.knows = int(sum(np.ravel(adjacency_matrix[node.id])))
        node.known_by = int(np.ravel(sum(adjacency_matrix[:,node.id])))

    with open('nodes-and-edges.js', 'w+') as f:

        # Write the code for the Nodes to the file
        # This is just the preamble
        f.write('// The nodes for the graph \n')
        f.write('var nodes = [ \n')

        # And these are the actual data
        for node in sorted(list_of_nodes_, key=lambda x: x.id):
            f.write('\t{{ id: {id}, label: "{label}", title: "{title}", '
                    'value: {value}, group: {group}, color: {{ border: '
                    '"{border}", background: "{background}" }}, '
                    'original_color: {{ border: "{border}", background: '
                    '"{background}" }} }},\n'
                    .format(id=node.id,
                            label=node.name,
                            title='Name: {}<br>'\
                                  'Major: {}<br>'\
                                  'Group: {}<br>'\
                                  'Knows: {} people<br>'\
                                  'Known by: {} people<br>'\
                                  .format(node.name, node.major, node.group,
                                          node.knows, node.known_by),
                            value=node.known_by,
                            group=node.group,
                            border=DarkColor(int(node.group)),
                            background=LightColor(int(node.group))))

        # Close the Node array properly
        f.write(']; \n\n\n')

        # Create the edges...
        f.write('var edges = [\n')

        # Now loop over the adjacency matrix to calculate the edges
        n_people = len(adjacency_matrix_)
        id = 0
        for row in range(n_people):
            for col in range(row):

                # CASE 1: Both people said they know each other.
                # We draw an undirected edge between them
                if adjacency_matrix_[row, col] and adjacency_matrix_[col, row]:
                    startnode = get_node_by_id(list_of_nodes_, row)
                    color = DarkColor(int(startnode.group))
                    f.write('\t{{ id: {}, from: {}, to: {}, arrows: "to", '
                            'color: "{}", original_color: "{}"}},\n'
                            .format(id, row, col, color, color))
                    id += 1

                # CASE 2: Person in row knows person in col, but not vice versa
                if adjacency_matrix_[row, col] and not adjacency_matrix_[col, row]:
                    startnode = get_node_by_id(list_of_nodes_, row)
                    color = DarkColor(int(startnode.group))
                    f.write('\t{{ id: {}, from: {}, to: {}, arrows: "to", '
                            'color: "{}", original_color: "{}"}},\n'
                            .format(id, row, col, color, color))
                    id += 1

                # CASE 3: Person in col knows person in row, but not vice versa
                if not adjacency_matrix_[row, col] and adjacency_matrix_[col, row]:
                    startnode = get_node_by_id(list_of_nodes_, col)
                    color = DarkColor(int(startnode.group))
                    f.write('\t{{ id: {}, from: {}, to: {}, arrows: "to", '
                            'color: "{}", original_color: "{}"}},\n'
                            .format(id, col, row, color, color))
                    id += 1

        # Close the Edges array properly
        f.write('];')

    print 'Created nodes-and-edges.js!'



# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------

# This is where we keep track of all nodes
list_of_nodes = []

# Read in the people.csv and initialize the Nodes from these data
with open('people.csv', 'r') as f:
    for index, line in enumerate(f.readlines()):
        name, major, group = map(lambda x: x.strip(), line.split(','))
        new_node = Node(index, name, major, group)
        list_of_nodes.append(new_node)

# The number of people in the graph
n_people = len(list_of_nodes)

# Get the adjacency matrix from the files in /data/
adjacency_matrix = create_adjacency_matrix(n_people)

# Create the nodes-and-edges.js
create_nodes_and_edges(list_of_nodes, adjacency_matrix)