import pandas as pd
import plotly_express as pe
import statistics as st
import csv
import plotly.graph_objects as pgo

data = pd.read_csv("savings.csv")

graph = pe.scatter(data, y = "quant_saved" , color = "rem_any")

# ------------------------------------------------------------------------------

with open('savings.csv') as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

total_entries = len(savings_data)
total_people_given_reminder = 0

for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1


fig = pgo.Figure(pgo.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

# --------------  Mean / Median / Mode / Stdev of the amount saved by all of them ----------------------

amount_saved_by_all = []

for j in savings_data : 
    amount_saved_by_all.append(float(j[0]))

meanAll = st.mean(amount_saved_by_all)

medianAll = st.median(amount_saved_by_all) 

modeAll = st.mode(amount_saved_by_all)

stdevAll = st.stdev(amount_saved_by_all)

print("--------------------------------------------------------")
print("Mean of the amount saved by all of them : " , meanAll)
print("Median of the amount saved by all of them : " , medianAll)
print("Mode of the amount saved by all of them : " , modeAll)
print("Stdev of the amount saved by all of them : " , stdevAll)

reminded_savings = []
not_reminded_savings = []

for data in savings_data:
  if int(data[3]) == 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

print("Results for people who were reminded to save")
print(f"Mean of savings - {st.mean(reminded_savings)}")
print(f"Median of savings - {st.median(reminded_savings)}")
print(f"Mode of savings - {st.mode(reminded_savings)}")

print("Results for people who were not reminded to save")
print(f"Mean of savings - {st.mean(not_reminded_savings)}")
print(f"Median of savings - {st.median(not_reminded_savings)}")
print(f"Mode of savings - {st.mode(not_reminded_savings)}")



