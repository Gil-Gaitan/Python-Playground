# Setup Kaggle API and download dataset
# pip install kaggle                        install kaggle
# kaggle --version                          check if installed
# GET YOUR API KEY FROM KAGGLE - go to profile -> account -> create new API token, it will download a .json
# mkdir ~/.kaggle                           create a directory for the API key
# mv ~/Downloads/kaggle.json ~/.kaggle/     move the API key to the directory
# chmod 600 ~/.kaggle/kaggle.json           change permissions
# kaggle datasets list                      list all datasets
# kaggle datasets download -d uciml/iris    download dataset    <---- 1.
# unzip iris.zip                            unzip the dataset in project folder
# GET PANDAS AND MATPLOTLIB - going with VM because pandas
# python3 -m venv kaggle_env                create a virtual environment
# source kaggle_env/bin/activate            activate the virtual environment
# pip install pandas matplotlib             install pandas and matplotlib
# pip install seaborn                       install seaborn for pair plotting
# python -c "import pandas as pd; import matplotlib.pyplot as plt; print('Ready')"  check if installed
# python -c "import seaborn as sns; print('Seaborn is ready!')"  check if seaborn is installed
# Ready to go. Start python to play around. Or run the script from the terminal

import pandas as pd  # data processing
import matplotlib.pyplot as plt  # For histogram plot
import seaborn as sns  # https://www.kaggle.com/code/saurav9786/seaborn-tutorial

# Load the CSV
df = pd.read_csv("iris.csv", index_col=0)  #     <--- 2.

print("\nDisplay data info:")
print(df.info())

print("\nPrint head:")
print(df.head())  #                             <--- 3.

print("\nPrint Tail:")
print(df.tail())  #                             <--- 4.

print("\nDisplay summary statistics:")  #        <--- 5.
print(df.describe())

print("\nCheck for missing values:")
print(df.isnull().sum())

# Plot a histogram https://www.kaggle.com/code/holfyuen/tutorial-histograms-and-kdes-in-python
df.hist(figsize=(10, 6), bins=20, edgecolor="black")  # Create df histogram
plt.suptitle("Histogram of Iris Dataset Features")  # title
plt.show()  # Display the plot


# Try making scatter plots
# Want to try these out.
plt.figure(figsize=(8, 6))  # Create a new figure

# Create plot
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"], alpha=0.7, edgecolors="black")

plt.xlabel("Sepal Length (cm)")  # x labeled with a String
plt.ylabel("Sepal Width (cm)")  # y same
plt.title("Scatter Plot of Sepal Length vs Sepal Width")  # add title
plt.show()

# Pairplot, frame color by species, diagonal with histogram
# found on https://www.kaggle.com/code/mervinpraison/seaborn-pairplot-with-iris-dataset
sns.pairplot(df, hue="Species", diag_kind="hist")
plt.show()

# Ensure only working with numerical columns
numeric_df = df.select_dtypes(include=["float64", "int64"])  # Exclude non-numeric data

print(numeric_df.corr())

# Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Pairwise
sns.pairplot(df, hue="Species", diag_kind="hist", markers=["o", "s", "D"])
plt.suptitle("Pairwise Relationships of Iris Dataset", size=16)
plt.show()
