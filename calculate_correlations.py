#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import os
import numpy as np
import pprint
import pandas as pd
import codecs
import matplotlib.pyplot as plt
import statsmodels.api as sm

# -----------------------------------------------------------------------------
# EXPLANATION:
# This file reads in the questionaire answers of all people and calculates the
# correlations coefficients.
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# GENERAL FUNCTIONS
# -----------------------------------------------------------------------------

def resize_labels():
    ax = plt.gca()
    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontsize(10)
    plt.tight_layout()

def replace_umlauts(string):
    result = u'{}'.format(string)
    result = result.replace(u'ß', 'ss')
    result = result.replace(u'ä', 'ae')
    result = result.replace(u'ö', 'oe')
    result = result.replace(u'ü', 'ue')
    return result


# -----------------------------------------------------------------------------
# READING IN THE DATA
# -----------------------------------------------------------------------------

features = ['age', 'academies', 'waylength', 'hiking', 'lake', 'choir',
            'games', 'drinks', 'sleep', 'number', 'hotness', 'hookups',
            'description']
feature_names = ['Alter', 'Sommerakademien', 'Anfahrtsdauer', 'Wander-Tage',
                 'See-Tage', 'Chor-Tage', 'Spieleabende', 'Barkasse', 'Schlaf',
                 'Lieblingszahl', 'Eigene Attraktivitaet', 'Fremde Betten',
                 'In einem Wort']

data = {}
for i in range(len(features)):
    data[features[i]] = []
data['id'] = []
data['fach'] = []
data['ag'] = []

people = np.loadtxt('people.csv', delimiter=', ', dtype=str)

for i in range(97):

    try:
        with codecs.open('./data-answers/{}.csv'.format(i), 'r',
                         encoding="utf-8") as f:

            answers = f.readlines()

            for j in range(12):
                if (answers[j].strip()  and answers[j].strip() != '-1'):
                    data[features[j]].append(float(answers[j].strip()))
                else:
                    data[features[j]].append(float('nan'))

            dummy = replace_umlauts( answers[12].strip() )
            if (dummy and dummy!='-1'):
                data[features[12]].append( dummy )
            else:
                data[features[12]].append( '' )

            data['id'].append(i)
            data['fach'].append(people[i][1])
            data['ag'].append(people[i][2])

    except IOError:
        pass

# Create a Pandas DataFrame from the Data
df = pd.DataFrame(data)


# -----------------------------------------------------------------------------
# CALCULATE THE CORRELATIONS
# -----------------------------------------------------------------------------

"""
correlations = df[features[:-1]].corr()

sm.graphics.plot_corr(correlations, xnames=feature_names[:-1], normcolor=True)
plt.title('Korrelationsmatrix')
resize_labels()
plt.savefig('correlations.pdf', bbox_inches='tight')
"""

print df.to_csv(index_label='index', na_rep='?', quotechar='"')



