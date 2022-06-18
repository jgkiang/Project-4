from flask import Flask, render_template, Response
# from config import app_key
import requests
import pandas as pd
from sqlalchemy import create_engine
app = Flask(__name__)


# create my own API from the data stored in Postgres database
@app.route('/get_marvel_dc')
def hello():
    engine = create_engine("postgresql://jqzzrfsdewgljj:e5fb494866ce503b8bced245afe5c2068f1c7a94a9a242a8b41413def015f15c@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d4k7shgqb7gn6i")
    df = pd.read_sql_table("marveldc",con=engine)
    return Response(df.to_json(orient="records"), mimetype='application/json')
# load the index.html when requesting the https://localhost:5000

@app.route('/')
def home():
    return render_template('index.html',text="Hi")

if __name__ == '__main__':
    app.run(debug=True)