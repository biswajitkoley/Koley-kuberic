import requests
import pandas
import scipy
import numpy
import sys


TRAIN_DATA_URL = "https://storage.googleapis.com/kubric-hiring/linreg_train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/kubric-hiring/linreg_test.csv"

response = requests.get(TRAIN_DATA_URL)
with open('train_area.csv', 'w') as file:
    file.write(response.content.decode('utf-8')[5:2753])
with open('train_price.csv', 'w') as file:
    file.write(response.content.decode('utf-8')[2759:])
y = numpy.array(pandas.read_csv('train_price.csv').columns)
x = numpy.array(pandas.read_csv('train_area.csv').columns)
x = numpy.array(list(map(float, x)))
y = numpy.array(list(map(float, y)))
slope, intercept, _, _, _ = stats.linregress(x, y)
def predict_price(area) -> float:
    """
    This method must accept as input an array `area` (represents a list of areas sizes in sq feet) and must return the respective predicted prices (price per sq foot) using the linear regression model that you build.

    You can run this program from the command line using `python3 regression.py`.
    """
    return intercept + slope * area
    # YOUR IMPLEMENTATION HERE
    ...


if __name__ == "__main__":
    # DO NOT CHANGE THE FOLLOWING CODE
    from data import validation_data
    areas = numpy.array(list(validation_data.keys()))
    prices = numpy.array(list(validation_data.values()))
    predicted_prices = predict_price(areas)
    rmse = numpy.sqrt(numpy.mean((predicted_prices - prices) ** 2))
    try:
        assert rmse < 170
    except AssertionError:
        print(f"Root mean squared error is too high - {rmse}. Expected it to be under 170")
        sys.exit(1)
    print(f"Success. RMSE = {rmse}")
