# 📊 Matplotlib for Data Visualization Cheat Sheet (with Descriptions)

# --------------------------------------------------
# 📦 Step 1: Import necessary libraries
# --------------------------------------------------
import pandas as pd  # For handling tabular data
import matplotlib.pyplot as plt  # Main plotting library
import numpy as np  # For numerical computations

# --------------------------------------------------
# 📁 Step 2: Load and preview data
# --------------------------------------------------
infy = pd.read_csv('../data_modules/infy_dv.csv')  # Load dataset from file
infy.head()  # Display first few rows to inspect the data

# --------------------------------------------------
# 🧹 Step 3: Clean and prepare data for plotting
# --------------------------------------------------
infy_close = infy[['Date', 'Close Price']]  # Keep only Date and Close Price columns
infy_close.set_index('Date', inplace=True)  # Set 'Date' column as index for time series plot

# --------------------------------------------------
# 📈 Step 4: Basic Line Plot
# --------------------------------------------------
plt.plot(infy_close)  # Plot closing price vs. date
plt.show()  # Display the plot

# --------------------------------------------------
# 🎨 Step 5: Customized Plot
# --------------------------------------------------
plt.figure(figsize=(14, 5))  # Set figure size (width=14, height=5)
plt.plot(infy_close, 'b')  # Plot blue line for closing price
plt.plot(infy_close, 'ro')  # Overlay red circles for data points
plt.grid(True)  # Add grid lines to the plot
plt.title('Infosys Close Price Representation')  # Add title to plot
plt.xlabel('Trading Days')  # Label x-axis
plt.ylabel('Infosys Close Price')  # Label y-axis
plt.show()  # Show the customized plot

# --------------------------------------------------
# 📊 Step 6: Plot with Multiple Datasets (Close & Open)
# --------------------------------------------------
infy2 = pd.read_csv('../data_modules/infy_dv.csv')  # Load data again (new copy)
infy2 = infy2[['Date', 'Close Price', 'Open Price']]  # Select Date, Close, and Open
infy2.set_index('Date', inplace=True)  # Set Date as index

plt.figure(figsize=(14, 5))  # Set figure size
plt.plot(infy2['Close Price'], lw=1.5, label='Close Price')  # Line for Close Price
plt.plot(infy2['Open Price'], lw=1.5, label='Open Price')  # Line for Open Price
plt.plot(infy2, 'ro')  # Red circle markers for all points
plt.grid(True)  # Add grid
plt.legend(loc=0)  # Add legend at best location
plt.axis('tight')  # Fit axes tightly around data
plt.xlabel('Time')  # Label x-axis
plt.ylabel('Index')  # Label y-axis
plt.title('Representative plot with two datasets')  # Add title
plt.show()  # Show the plot

# --------------------------------------------------
# 🔵 Step 7: Scatter Plot (Optional)
# --------------------------------------------------
y = np.random.standard_normal((100, 2))  # Generate 100 random (x, y) points
plt.figure(figsize=(7, 5))  # Set plot size
plt.scatter(y[:, 0], y[:, 1], marker='o')  # Create scatter plot with circles
plt.grid(True)  # Add grid
plt.xlabel('1st dataset')  # Label x-axis
plt.ylabel('2nd dataset')  # Label y-axis
plt.title('Scatter Plot')  # Add title
plt.show()  # Display scatter plot

# --------------------------------------------------
# 📉 Step 8: Histogram (Optional)
# --------------------------------------------------
np.random.seed(100)  # Set seed for reproducibility
y = np.random.standard_normal(size=1000)  # Generate 1000 random values
plt.figure(figsize=(10, 5))  # Set plot size
plt.hist(y, label=['Returns Distribution'])  # Create histogram
plt.grid(True)  # Add grid
plt.legend(loc=0)  # Add legend at best location
plt.ylabel('Frequency')  # Label y-axis
plt.xlabel('Returns in Percentage')  # Label x-axis
plt.title('Histogram')  # Add title
plt.show()  # Show histogram
