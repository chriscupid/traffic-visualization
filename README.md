📊 Traffic Visualization
A simple data science project to visualize website traffic sources (search, direct, social media) over time using Python, Pandas, and Matplotlib.
 Features
Reads website traffic data from data/visitors.csv
Plots line charts of monthly visitors by source
Saves the visualization into the screenshots/ folder
Easy to reproduce with one script (plot.py)       

A) Dataset Preview (visitors.csv)
Month	Searches	Direct	Social Media

B) Installation & Setup
Clone the repository:
git clone https://github.com/chriscupid/traffic-visualization.git
cd traffic-visualization

Install required dependencies:
pip install -r requirements.txt

C) Usage
Run the script:
python plot.py

This will:
Read data from data/visitors.csv
Generate a line chart
Save the chart as screenshots/plot.png
Optionally display the chart in a window
 Example Output
 Requirements:
Python 3.8+
Pandas
Matplotlib

Install them with:
pip install -r requirements.txt
