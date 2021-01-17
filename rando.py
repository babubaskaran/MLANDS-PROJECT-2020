# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index1.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}



@app.route('/api/model/<int:w>')

def model(w):
    # Make the prediction using our model with w, w^2, w^3.
    p = polyreg.predict([[w, w ** 2, w ** 3]])
    return {"value": str(p[0])} # Object must be a string.
