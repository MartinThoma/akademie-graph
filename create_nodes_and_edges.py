#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# EXPLANATION:
# This file reads in the people.csv and the files from the /data folder, and
# uses these data to create the nodes-and-edges.js.
# -----------------------------------------------------------------------------



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
        self.known_by = 1



# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

def create_nodes_and_edges(list_of_nodes_, list_of_edges_):
    """
    This function takes the list of nodes and the list of edges and creates
    the JSON file from them.
    """

    with open('nodes-and-edges.js', 'w+') as f:

        # Write the code for the Nodes to the file
        # This is just the preamble
        f.write('// The nodes for the graph \n')
        f.write('var nodes = [ \n')

        # And these are the actual data
        for node in sorted(list_of_nodes_, key=lambda x: x.id):
            f.write('\t{{ id: {id}, label: "{label}", title: "{title}", '
                    'value: {value}, group: {group} }},\n'
                    .format(id=node.id,
                            label=node.name,
                            title='Name: {}<br>Fach: {}<br>AG: {}'.format(node.name, node.major, node.group),
                            value=node.known_by,
                            group=node.group))

        # Close the array properly
        f.write(']; \n\n\n')

        # Create the edges...
        f.write('var edges = [];')

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

# Create the nodes-and-edges.js
create_nodes_and_edges(list_of_nodes, [])
