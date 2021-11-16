#!/usr/bin/python

from collections import defaultdict
import random
import sys
import pprint
import time


def create_graph(filename):
    # default dict provides a default value for a key that does not exist
    # here, we're setting it to a blank list
    graph = defaultdict(list)

    # creating the graph
    with open(filename) as f:
        # for every line, we find parent node, neighbor node and append them to each other
        for line in f:
            r = line.strip().split(" ")
            u, v = [int(x) for x in r]

            graph[u].append(v)
            graph[v].append(u)

    return graph


def delta_coloring(graph):

    # we first find the number of colors, which is max degree + 1
    ncolor = max(len(neighbours) for neighbours in graph.values()) + 1
    # then, we list all of the colors from 0 to ncolor
    colors = list(range(0, ncolor))

    # here, we create a random sampling of 100 colors for each vertex
    # i chose to use sets, because they resulted in a faster runtime and were more efficient
    vertcolors = {v: set(random.sample(colors, 100)) for v in graph}

    # creating a dictionary for the colorings
    colorings = {}
    # here, we initialize our conflict graph, in which we have all of the vertices, but no edges.
    conflict_graph = {v: [] for v in graph}  

    # here, we are trying to find conflicts in our color sampling
    # we pick a vertex in the graph, v
    for v in graph:
        # we iterate over its neighbors, graph[v]
        for u in graph[v]:
            
            # since we are using sets, we check to see if an item is present in both sets
            # this means that we are checking for edge (u, v) if L[u] intersects with L[v] or not
            if not vertcolors[v].isdisjoint(vertcolors[u]):
                # if they do intersect, we store this as an edge of both u and v
                conflict_graph[v].append(u)

    # here, we will greedily color the conflict graph
    for v in conflict_graph:
        for u in conflict_graph[v]:  
            # if u has already been colored
            if u in colorings:
                # we are deleting it from L[v]
                vertcolors[v].discard(colorings[u])
            # here, we are coloring v with any arbitrary color remaining in L[v]
            if vertcolors[v]:
                # we pick the min value that is left in vertcolors[v]
                colorings[v] = min(vertcolors[v])
            else:
                raise Exception("the algorithm has failed")

    return colorings


filename = "/Users/sanjp/Documents/web-polblogs.txt"
#pprint.pprint((delta_coloring(filename)))
graph = create_graph(filename)
t0 = time.perf_counter()
delta_coloring(graph)
t1 = time.perf_counter()
total_time = t1-t0
print(total_time)
#with open('web_polblogs_d', 'wt') as out:
    #pprint.pprint(delta_coloring(filename), stream=out)
