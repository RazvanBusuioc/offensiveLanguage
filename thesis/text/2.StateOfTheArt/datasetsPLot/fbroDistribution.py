import csv
import os
import plotly.graph_objects as go
import statistics
from matplotlib import pyplot as plt

file = open("/home/busu/Desktop/offensivelanguage/corpora/FB-RO-Offense/dataset.csv", "r")
reader = csv.reader(file)
header = next(reader)

classes = []
text = []
textLen = []

for row in reader:
    text.append(str(row[2]))
    textLen.append(len(str(row[2])))
    classes.append(str(row[3]))

OTHERNr = len([x for x in classes if x == "OTHER"])
INSULTNr = len([x for x in classes if x == "INSULT"])
ABUSENr = len([x for x in classes if x == "ABUSE"])
PROFANITYnr = len([x for x in classes if x == "PROFANITY"])

fig = go.Figure(data=[go.Bar(
    x=['OTHER', 'INSULT', 'ABUSE', 'PROFANITY'],
    y=[OTHERNr, INSULTNr, ABUSENr, PROFANITYnr],
    texttemplate="%{y}",
    marker_color=["red", "purple", "green", "blue"] # marker color can be a single color value or an iterable
)])
fig.update_layout(yaxis=dict(
        title='Number of comments',
        titlefont_size=32,
        tickfont_size=32,
    ),xaxis=dict(
        titlefont_size=32,
        tickfont_size=32,
    ),
    font=dict(
        family="Courier New, monospace",
        size=40,
    ))
fig.show()

print("Mean:" ,statistics.mean(textLen))
print("Median:" ,statistics.median(textLen))
print("Standard Dev:" ,statistics.stdev(textLen))
print("Minimum len", min(textLen))
print("Maximum len:", max(textLen))

dictionary = {}

for val in textLen:
    if val not in dictionary:
        dictionary[val] = 1
    else:
        dictionary[val] = dictionary[val] + 1

lens = list(dictionary.keys())
nrPerLen = list(dictionary.values())

import matplotlib.pyplot as plt

data = [x for x in textLen if x < 500 and x > 50]
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=data, bins=35, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Comment length (characters)')
plt.ylabel('Frequency')
maxfreq = n.max()
plt.show()

# import plotly.express as px
# fig = px.scatter(x=lens, y=nrPerLen, color_discrete_sequence=['blue'], trendline="lowess", trendline_color_override="green",  width=1000, height=500)

# fig.update_layout(yaxis=dict(
#         title='Number of comments',
#         titlefont_size=16,
#         tickfont_size=14,
#     ),xaxis=dict(
#         title='Comment length',
#         titlefont_size=16,
#         tickfont_size=14,
#     ))
# fig.show()



# file = open("/home/busu/Desktop/offensivelanguage/corpora/FB-RO-Offense/cutDataset.csv", "r")
# reader = csv.reader(file)
# header = next(reader)

# classes = []
# text = []
# textLen = []

# for row in reader:
#     text.append(str(row[2]))
#     textLen.append(len(str(row[2])))
#     classes.append(str(row[3]))

# OTHERNr = len([x for x in classes if x == "OTHER"])
# INSULTNr = len([x for x in classes if x == "INSULT"])
# ABUSENr = len([x for x in classes if x == "ABUSE"])
# PROFANITYnr = len([x for x in classes if x == "PROFANITY"])




# fig = go.Figure(data=[go.Bar(
#     x=['OTHER', 'INSULT', 'ABUSE', 'PROFANITY'],
#     y=[OTHERNr, INSULTNr, ABUSENr, PROFANITYnr],
#     texttemplate="%{y}",
#     marker_color=["red", "purple", "green", "blue"] # marker color can be a single color value or an iterable
# )])
# fig.update_layout(yaxis=dict(
#         title='Number of comments',
#         titlefont_size=16,
#         tickfont_size=14,
#     ),xaxis=dict(
#         titlefont_size=16,
#         tickfont_size=14,
#     ))
# fig.show()