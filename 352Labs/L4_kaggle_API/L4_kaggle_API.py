# Setup Kaggle API and download dataset
# pip install kaggle                        install kaggle
# kaggle --version                          check if installed
# GET YOUR API KEY FROM KAGGLE - go to profile -> account -> create new API token
# mkdir ~/.kaggle                           create a directory for the API key
# mv ~/Downloads/kaggle.json ~/.kaggle/     move the API key to the directory
# chmod 600 ~/.kaggle/kaggle.json           change permissions
# kaggle datasets list                      list all datasets
# kaggle datasets download -d uciml/iris    download dataset
# unzip iris.zip                            unzip the dataset in project folder
# GET PANDAS AND MATPLOTLIB - going with VM because pandas
# python3 -m venv kaggle_env                create a virtual environment
# source kaggle_env/bin/activate            activate the virtual environment
# pip install pandas matplotlib             install pandas and matplotlib
# pip install seaborn                       install seaborn for pair plotting
# python -c "import pandas as pd; import matplotlib.pyplot as plt; print('Ready')"  check if installed
# python -c "import seaborn as sns; print('Seaborn is ready!')"  check if seaborn is installed
# python                                    start python

import pandas as pd
import matplotlib.pyplot as plt  # For histogram plot
import seaborn as sns  # Make it pop

df = pd.read_csv(
    "iris.csv", index_col=0
)  # Load the CSV and use the first column as the index

# Display some inital information about the dataset
print(df.head())  # Display the first few rows
print(df.info())  # Display the data types and non-null values
print(df.describe())  # Display summary statistics
print(df.isnull().sum())  # Check for missing values


# Plot a histogram
df.hist(figsize=(10, 6), bins=20, edgecolor="black")  # Create a histogram with 20 bins
plt.suptitle("Histogram of Iris Dataset Features")  # Add a title
plt.show()  # Display the plot


# Plot a scatter plot
# This is how they make basketball shotcharts and plot advanced player data
# I could use this in an app I built that gets NBA API data for my favorite players
plt.figure(figsize=(8, 6))  # Create a new figure
plt.scatter(
    df["SepalLengthCm"], df["SepalWidthCm"], alpha=0.7, edgecolors="black"
)  # Create plot
plt.xlabel("Sepal Length (cm)")  # x labeled with a String
plt.ylabel("Sepal Width (cm)")  # y same
plt.title("Scatter Plot of Sepal Length vs Sepal Width")  # add title
plt.show()  # Display it
sns.pairplot(
    df, hue="Species", diag_kind="hist"
)  # Pairplot, frame color by species, diagonal with histogram
plt.show()  # Display the plot

# Ensure we are only working with numerical columns
numeric_df = df.select_dtypes(include=["float64", "int64"])  # Exclude non-numeric data

# Print the correlation matrix
print(numeric_df.corr())

# Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
