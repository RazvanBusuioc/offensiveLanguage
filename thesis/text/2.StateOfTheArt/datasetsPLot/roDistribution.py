import csv
import os
import plotly.graph_objects as go
import statistics
from matplotlib import pyplot as plt
import numpy as np
import plotly.io as pio


file = open("/home/busu/Desktop/offensivelanguage/corpora/RO-Offense/train.csv", "r")
reader = csv.reader(file)
header = next(reader)

classes = []
text = []
textLen = []

for row in reader:
    text.append(str(row[1]))
    textLen.append(len(str(row[1])))
    classes.append(str(row[2]))

OTHERNr = len([x for x in classes if x == "OTHER"])
INSULTNr = len([x for x in classes if x == "INSULT"])
ABUSENr = len([x for x in classes if x == "ABUSE"])
PROFANITYnr = len([x for x in classes if x == "PROFANITY"])

file = open("/home/busu/Desktop/offensivelanguage/corpora/RO-Offense/test.csv", "r")
reader = csv.reader(file)
header = next(reader)

for row in reader:
    text.append(str(row[1]))
    textLen.append(len(str(row[1])))
    classes.append(str(row[2]))

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
        size=32,
    ))
pio.write_image(fig, 'filename.png', width=2048, height=1536)
fig.show()

file.close()

file = open("/home/busu/Desktop/offensivelanguage/corpora/RO-Offense/test.csv", "r")
reader = csv.reader(file)
header = next(reader)

for row in reader:
    text.append(str(row[1]))
    textLen.append(len(str(row[1])))
    classes.append(str(row[2]))
    
file.close()

print("Mean:" ,statistics.mean(textLen))
print("Median:" ,statistics.median(textLen))
print("Standard Dev:" ,statistics.stdev(textLen))
print("Minimum len", min(textLen))
print("Maximum len:", max(textLen))

dictionary = {}

for val in textLen:
    if val > 800 or val < 50:
        continue
    if val not in dictionary:
        dictionary[val] = 1
    else:
        dictionary[val] = dictionary[val] + 1

lens = list(dictionary.keys())
nrPerLen = list(dictionary.values())

# fig, ax = plt.subplots(figsize =(10, 7))
# ax.hist([x for x in textLen if x < 500 and x > 50], bins = 50)
 
# # Show plot
# plt.show()

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

import matplotlib.pyplot as plt

data = [x for x in textLen if x < 500 and x > 50]
# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=data, bins=50, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Comment length (characters)')
plt.ylabel('Frequency')
maxfreq = n.max()
# Set a clean upper y-axis limit.
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()