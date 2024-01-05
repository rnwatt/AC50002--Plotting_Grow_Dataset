import matplotlib.pyplot as plt
import pandas as pd

# Read in dataset to a data frame
# Filter this new df by validating the points are in the bounding box for Longitude and Latitude columns
def main():
    # https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html used in filterData()
    # for reading in csv file and filtering longitude and latitude values
    df = pd.read_csv("GrowLocations.csv")
    #Latitude and Longitude are switched around
    minLat = 50.681
    maxLat = 57.985
    minLong = -10.592
    maxLong = 1.6848
    filterDf = df[(df.Longitude >= minLat) & (df.Longitude <= maxLat) & (df.Latitude >= minLong) & (df.Latitude <= maxLong)]

    # https://www.tutorialspoint.com/matplotlib-plot-over-an-image-background-in-python and
    # https://realpython.com/visualizing-python-plt-scatter/ used for plotting
    #Read the map into a variable
    #Create a new figure with axes
    #ax.scatter - Plot the points of the df on the axes from plt.subplots
    #Display the map, with the bounding box values used for the extent
    mapPlot = plt.imread("map7.png")
    fig, ax = plt.subplots()
    plt.title("Plotting Grow Data")
    ax.scatter(filterDf['Latitude'], filterDf['Longitude'], color='blue', marker='o', label='GROW sensor')
    ax.imshow(mapPlot, extent=[minLong, maxLong, minLat, maxLat], aspect='auto')

    #plot labels and legend added from scatter label value, plots saved and shown
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.savefig('finalPlot.png')
    plt.show()


if __name__ == '__main__':
    main()



