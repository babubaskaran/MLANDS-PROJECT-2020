# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  #return app.send_static_file('index.html')
  return "Hello World"

# Add uniform route.
@app.route('/api/uniform')
#@app.route('/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
#@app.route('/normal')
def normal():
  return {"value": np.random.normal()}