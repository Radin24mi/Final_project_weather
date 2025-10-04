# Final_project_weather

Weather Data Analysis & Visualization

This project performs data cleaning, transformation, and visualization on a weather dataset.
It focuses on analyzing temperature and humidity trends across different cities, detecting heatwaves, and exploring correlations between variables.

📂 Dataset

Input file: weather_dataset.csv

Converted to: weather_dataset.json for flexible use.

The dataset includes:

time: Date and time of observation

location_id: City/Location identifier

temperature_2m (°C): Air temperature at 2 meters above ground

relative_humidity_2m (%): Relative humidity at 2 meters above ground

🛠️ Workflow
1. Data Cleaning & Preprocessing

Converted time to datetime format

Casted location_id as categorical

Converted temperature & humidity to float

Extracted time components: year, month, day, hour

Defined seasons (Winter, Spring, Summer, Autumn) based on month

2. Aggregations

Monthly averages of temperature & humidity

Yearly averages for long-term trends

Seasonal statistics (mean, max, min) per city

Diurnal cycle (hourly average temperature and humidity)

Detection of extreme weather days (>40°C or >90% humidity)

3. Visualizations

📈 Line plots for monthly & yearly temperature/humidity per city

📊 Bar plots for seasonal averages

📉 Trend plots (temperature trends over 50 years)

🔥 Heatwave analysis: number of days above 35°C per year

🔗 Scatter plots & regression plots showing correlation between temperature and humidity

🟦 Heatmaps for correlation and seasonal patterns

🌀 Pairplots to compare cities and seasons

📦 Boxplots for seasonal temperature distributions

🗓️ Year-Month heatmap for one city

4. Correlation Analysis

Pairwise correlation between temperature & humidity for each city

Heatmaps to visualize correlation strength

5. Clustering

Applied K-Means clustering to group cities by average temperature & humidity

📊 Example Outputs

Monthly & yearly trends of temperature and humidity

Heatmaps showing correlation across cities

Scatter plots for relationships between variables

Boxplots showing seasonal variations

Clustered cities based on weather patterns

🚀 Usage

Place your dataset file in the same directory:

weather_dataset.csv


Run the Python script (or Jupyter notebook).

Plots and printed statistics will be generated automatically.

📦 Dependencies

Make sure you have the following libraries installed:

pip install pandas numpy matplotlib seaborn scikit-learn

🔮 Future Improvements

Add predictive modeling (e.g., forecasting temperature trends)

Include more climate variables (wind, precipitation, etc.)

Interactive dashboards with Plotly or Streamlit
