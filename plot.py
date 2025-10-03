import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make sure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

# Read CSV
df = pd.read_csv("data/visitors.csv")

months = df['month'].tolist()
searches = df['searches'].tolist()
direct = df['direct'].tolist()
social = df['social_media'].tolist()

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(11,6))

bars1 = ax.bar(x - width, searches, width, label='Searches', color='#2A9DF4')
bars2 = ax.bar(x, direct, width, label='Direct', color='#E87EA6')
bars3 = ax.bar(x + width, social, width, label='Social Media', color='#F4B400')

# Titles and labels
ax.set_title("Visitors by web traffic sources")
ax.set_xlabel("months")
ax.set_ylabel("visitors in thousands")
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Add values on bars
for bar in bars1 + bars2 + bars3:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

plt.tight_layout()
plt.savefig("screenshots/plot.png", dpi=150, bbox_inches='tight')
print("Plot saved at screenshots/plot.png")