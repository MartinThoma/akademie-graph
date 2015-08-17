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
from itertools import product


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
        self.age          = 0
        self.academies    = 0
        self.waylength    = 0
        self.hiking       = 0
        self.lake         = 0
        self.choir        = 0
        self.games        = 0
        self.drinks       = 0
        self.sleep        = 0
        self.number       = 0
        self.hotness      = 0
        self.hookups      = 0
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


def isEven(number):
    return not number%2==0


def create_adjacency_matrix(n_people):
    """
    This function loops over all files in /data and creates the adjacency
    matrix from it.
    """
    adjacency_array = []
    for i in range(n_people):
        try:
            row = np.loadtxt('./data/{}.csv'.format(i), usecols=[1], delimiter=',')
        except IOError:
            row = np.array(n_people*[0])
        adjacency_array.append(row)
    return np.matrix(adjacency_array)


def apply_warshall_algorithm(w):

    N = len(w)
    d = [N*[0] for _ in range(N)]

    for i, j in product(range(N), range(N)):
        if w[i, j] == 0:
            d[i][j] = np.inf
        else:
            d[i][j] = w[i, j]

    d = np.array(d)
    
    for k in range(N):
        for i, j in product(range(N), range(N)):
            d[i, j] = min(d[i, j], d[i, k] + d[k, j])

    return d


def get_bar_sum():
    """Sums up all contributions to the bar"""
    barsumme = 0
    for node in list_of_nodes:
        if node.drinks == "'?'":
            continue
        barsumme += int(node.drinks)
    print barsumme


def scrabble_score(word):
    """Calculates the scrabble score of a word"""
    score = {'a': 1, 'b': 3, 'c': 4, 'd': 1, 'e': 1, 'f': 4,
         'g': 2, 'h': 2, 'i': 1, 'j': 6, 'k': 4, 'l': 2,
         'm': 3, 'n': 1, 'o': 2, 'p': 4, 'q': 10, 'r': 1,
         's': 1, 't': 1, 'u': 1, 'v': 6, 'w': 3, 'x': 8,
         'y': 10, 'z': 3}
    
    if len(word) > 15:
        return 0
    total = []
    for letter in word:
        if letter not in score.keys():
            continue
        total.append(score[letter.lower()])
    return sum(total)


def replace_umlauts(string):
    """Replaces the German umlauts in a string"""
    result = string.lower()
    result = result.replace('ß', 'ss')
    result = result.replace('ä', 'ae')
    result = result.replace('ö', 'oe')
    result = result.replace('ü', 'ue')
    return result


def calculate_all_scrabble_scores():
    """Calculates the scrabble score for all words"""
    for node in list_of_nodes:
        word = replace_umlauts(node.description)
        if word == "'?'":
            continue
        print word, scrabble_score(word)


def minDistance(pos):
    distances = []
    x, y = pos
    for _ in positions:
        x_, y_ = _
        distances.append((x-x_)**2 + (y-y_)**2)
    if not distances:
        return 20001
    else:
        return np.min(distances)


def xy_from_group(group):
    
    def pol2cart(rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        return [x, y]

    number = {'1':0, '3':1, '4':2, '5':3, '6':4, '7':5}[group]
    
    x_, y_ = pol2cart(1500, np.pi/3*number)
    x = x_ + np.random.normal(0, 250)
    y = y_ + np.random.normal(0, 250)
    while minDistance([x, y]) < 20000:
        x = x_ + np.random.normal(0, 250)
        y = y_ + np.random.normal(0, 250)
    positions.append([x, y])
    return (x, y)



def get_node_by_id(list_of_nodes_, id):
    for node in list_of_nodes_:
        if node.id == id:
            return node


def average_known_people():
    """Prints the average number of people known by one person"""
    print 'Knows', np.mean([sum(list(np.ravel(adjacency_matrix[i]))) 
                            for i in range(n_people)])
    print 'Is known', np.mean([sum(adjacency_matrix[:,i])
                               for i in range(n_people)])



def create_nodes_and_edges(list_of_nodes_, adjacency_matrix_):
    """
    This function takes the list of nodes and the list of edges and creates
    the JSON file from them.
    """

    # Random numbers for the labels
    random_numbers = np.arange(len(list_of_nodes_))
    np.random.shuffle(random_numbers)
    print random_numbers

    # Update the nodes: Every node gets told how many other nodes know it
    for node in sorted(list_of_nodes_, key=lambda x: x.id):
        node.knows = int(sum(np.ravel(adjacency_matrix[node.id])))
        node.known_by = int(np.ravel(sum(adjacency_matrix[:,node.id])))

    # Update the nodes: Every node gets its questionaire answers
    for node in sorted(list_of_nodes_, key=lambda x: x.id):
        try:
            with open('./data-answers/{}.csv'.format(node.id), 'r') as f:
                answers = f.readlines()
                node.age         = answers[0].strip()  if (answers[0].strip()  and answers[0].strip() != '-1') else "'?'"
                node.academies   = answers[1].strip()  if (answers[1].strip()  and answers[1].strip() != '-1') else "'?'"
                node.waylength   = answers[2].strip()  if (answers[2].strip()  and answers[2].strip() != '-1') else "'?'"
                node.hiking      = answers[3].strip()  if (answers[3].strip()  and answers[3].strip() != '-1') else "'?'"
                node.lake        = answers[4].strip()  if (answers[4].strip()  and answers[4].strip() != '-1') else "'?'"
                node.choir       = answers[5].strip()  if (answers[5].strip()  and answers[5].strip() != '-1') else "'?'"
                node.games       = answers[6].strip()  if (answers[6].strip()  and answers[6].strip() != '-1') else "'?'"
                node.drinks      = answers[7].strip()  if (answers[7].strip()  and answers[7].strip() != '-1') else "'?'"
                node.sleep       = answers[8].strip()  if (answers[8].strip()  and answers[8].strip() != '-1') else "'?'"
                node.number      = answers[9].strip()  if (answers[9].strip()  and answers[9].strip() != '-1') else "'?'"
                node.hotness     = answers[10].strip() if (answers[10].strip() and answers[10].strip()!= '-1') else "'?'"
                node.hookups     = answers[11].strip() if (answers[11].strip() and answers[11].strip()!= '-1') else "'?'"
                node.description = answers[12].strip() if (answers[12].strip() and answers[12].strip()!= '-1') else "'?'"
            
        except IOError:
            node.age         = "'?'"
            node.academies   = "'?'"
            node.waylength   = "'?'"
            node.hiking      = "'?'"
            node.lake        = "'?'"
            node.choir       = "'?'"
            node.games       = "'?'"
            node.drinks      = "'?'"
            node.sleep       = "'?'"
            node.number      = "'?'"
            node.hotness     = "'?'"
            node.hookups     = "'?'"
            node.description = "?"

    with open('nodes-and-edges.js', 'w+') as f:

        # Write the code for the Nodes to the file
        # This is just the preamble
        f.write('// The nodes for the graph \n')
        f.write('var nodes = [ \n')

        # And these are the actual data
        for node in sorted(list_of_nodes_, key=lambda x: x.id):
            pos = xy_from_group(node.group)
            f.write('\t{{ id: {id}, '
                         'label: "{random_number}", '
                         'title: "<small style=\'font-family: Roboto Slab;\'>'
#                                 'Name: {label} <br>'
#                                 'Fach: {major} <br>'
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
                         'knows: {knows}, '
                         'known_by: {known_by}, '
                         'x: {x}, '
                         'y: {y}, '
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
                                random_number=random_numbers[node.id],
                                label=node.name,
                                major=node.major,
                                group=node.group,
                                x=pos[0],
                                y=pos[1],
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
                    f.write('\t{{ id: {}, from: {}, to: {}, '
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

# This is where we keep track of all Node position
positions = []

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

# Apply the Warshall-algorithm to the adjacency matrix
##np.set_printoptions(threshold='nan')
##print set(np.ravel(apply_warshall_algorithm(adjacency_matrix)))

