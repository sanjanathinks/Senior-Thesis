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

def greedy_coloring(graph):
  # Order nodes in descending degree
  nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
  #print(nodes)
  # Set an empty map for colors
  color_map = {}

  # For every node in our graph
  for node in nodes:
      # create a boolean array that inserts True for each node
      # True means that the vertex has not been assigned a color yet
    available_colors = [True] * len(nodes)
    # We are now looping through each neighbor for a specific node in our graph
    for neighbor in graph[node]:
        # if we find the neighbor node in our map of colors, this means it has been already assigned a color
      if neighbor in color_map:
        # we now find the color of that neighbor. note that this color is used by that neighbor
        color = color_map[neighbor]
        # since the color has been used by the neighbor, we set the used color to False, meaning that a vertex has been assigned that color,
        # and that the color cannot be used in the neighbors of a particular vertex.
        available_colors[color] = False
    # enumerate() returns a list of tupes in which the first element is the index (where the element is placed in the available_colors array) and the second is the value
    for color, available in enumerate(available_colors):
    # the color is a part of available_colors 
      if available:
          # we assign an unused color for that particular node 
          color_map[node] = color
          # break because we don't want that color to be used again
          break
            
  return color_map

filename = "/Users/sanjp/Documents/web-polblogs.txt"
graph = create_graph(filename)
t0 = time.perf_counter()
greedy_coloring(graph)
t1 = time.perf_counter()
total_time = t1-t0
print(total_time)
#pprint.pprint((delta_coloring(filename)))
#with open('notre_dame_g.txt', 'wt') as out:
    #pprint.pprint(greedy_coloring(filename), stream=out)

