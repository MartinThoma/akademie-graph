#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# EXPLANATION:
# This file fills the folder /data with dummy files (necessary for development
# purposes while we don't have real data yet)
# -----------------------------------------------------------------------------

import numpy as np

# Get the number of people
n_people = 0
with open('people.csv', 'r') as f:
    n_people = len(f.readlines())

# Create a dummy file for each person
for i in range(n_people):

    with open('./data/{}.csv'.format(i), 'w+') as f:
        for j in range(n_people):
            number = int(np.random.uniform(0,1) < 0.75)
            if j==i:
                number = 0
            f.write('{}, {}\n'.format(j, number))