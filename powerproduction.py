# flask for web app.
import flask as fl
import csv
import requests
import pickle
import os
# numpy for numerical work.
import numpy as np
import pandas as pd
from sklearn.neighbors import RadiusNeighborsRegressor


# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index1.html')

# Add uniform route.
#@app.route('/api/uniform')
#def uniform():
#  return {"value": np.random.uniform()}

# Add normal route.
#@app.route('/api/normal')
#def normal():
#  return {"value": np.random.normal()}

# Add normal route.
@app.route("/powerproduction", methods=["POST"])
def powerproduction():
    if fl.request.method == "POST":
        speed = {}
        speed = float(fl.request.form['speed'])
        df = pd.read_csv("powerproduction.csv")

        df = df[df.power !=0]

        df = df.sort_values('speed')

        S = df['speed'].to_numpy()
        p = df['power'].to_numpy()

        neigh_radius = RadiusNeighborsRegressor(radius=1.7, weights='distance', p = 2)
        neigh_radius.fit(S.reshape(-1, 1), p)

        p_pred = neigh_radius.predict([[speed]])

        return {'value': p_pred[0]}

if __name__ == "__main__":
    app.run(debug=True)