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

        # Additional properties from the questionaire
        self.age = 0
        self.academies = 0
        self.waylength = 0
        self.hiking = 0
        self.lake = 0
        self.choir = 0
        self.games = 0
        self.drinks = 0
        self.sleep = 0
        self.number = 0
        self.hotness = 0
        self.hookups = 0
        self.description = '' 


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

def LightColor(group):
    colors = {1: 'rgb(230, 91, 119)', 
              3: 'rgb(146, 181, 242)', 
              4: 'rgb(238, 165, 77)', 
              5: 'rgb(100, 174, 100)', 
              6: 'rgb(255, 227, 77)', 
              7: 'rgb(129, 77, 168)'}
    return colors[group]



def DarkColor(group):
    colors = {1: 'rgb(220, 20, 60)',
              3: 'rgb(100, 149, 237)',
              4: 'rgb(230, 126, 0)',
              5: 'rgb(34, 139, 34)',
              6: 'rgb(255, 215, 0)',
              7: 'rgb(75, 0, 130)'}
    return colors[group]



def create_adjacency_matrix(n_people):
    """
    This function loops over all files in /data and creates the adjacency
    matrix from it.
    """
    adjacency_array = []
    for i in range(n_people):
        row = np.loadtxt('./data/{}.csv'.format(i), usecols=[1], delimiter=',')
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
            f.write('\t{{ id: {id}, '
                         'label: "{label}", '
                         'title: "<small style=\'font-family: Roboto Slab;\'>'
                                 'Name: {label} <br>'
                                 'Fach: {major} <br>'
                                 'AG: {group} <br>'
                                 '---<br>'
                                 'Kennt {knows} Leute <br>'
                                 'Wird gekannt von {known_by} Leuten <br>'
                                 '---<br>'
                                 'Alter: {age} <br>'
                                 'Anzahl Sommerakademien: {academies} <br>'
                                 'Anfahrtsdauer: {waylength} <br>'
                                 'Wander-Tage: {hiking} <br>'
                                 'See-Tage: {lake} <br>'
                                 'Chor-Tage: {choir} <br>'
                                 'Spieleabende: {games} <br>'
                                 'Beitrag zur Barkasse: {drinks} <br>'
                                 'Schlaf pro Nacht: {sleep} <br>'
                                 'Lieblingszahl: {number} <br>'
                                 'Eigene Attraktivität: {hotness} <br>'
                                 'Hookup-Schätzung: {hookups} <br>'
                                 'Neubeuern in einem Wort: {description}'
                                 '</small>", '
                         'value: {value}, '
                         'group: {group}, '
                         'color: {{ border: "{border}", '
                                   'background: "{background}", '
                                   'highlight: {{ border: "{border}", '
                                                 'background: "{background}" }} }}, '
                         'original_color: {{ border: "{border}", '
                                            'background: "{background}", '
                                            'highlight: {{ border: "{border}", '
                                                          'background: "{background}" }} }}, '
                         'age: {age}, '
                         'academies: {academies}, '
                         'waylength: {waylength}, '
                         'hiking: {hiking}, '
                         'lake: {lake}, '
                         'choir: {choir}, '
                         'games: {games}, '
                         'drinks: {drinks}, '
                         'sleep: {sleep}, '
                         'number: {number}, '
                         'hotness: {hotness}, '
                         'hookups: {hookups}, '
                         'description: "{description}" }},\n'
                        .format(id=node.id,
                                label=node.name,
                                major=node.major,
                                group=node.group,
                                knows=node.knows,
                                known_by=node.known_by,
                                value=node.known_by,
                                border=DarkColor(int(node.group)),
                                background=LightColor(int(node.group)),
                                age=node.age,
                                academies=node.academies,
                                waylength=node.waylength,
                                hiking=node.hiking,
                                lake=node.lake,
                                choir=node.choir,
                                games=node.games,
                                drinks=node.drinks,
                                sleep=node.sleep,
                                number=node.number,
                                hotness=node.hotness,
                                hookups=node.hookups,
                                description=node.description))

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