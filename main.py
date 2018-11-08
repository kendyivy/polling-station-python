from flask import (Flask,
                    render_template,
                   request,
                   make_response,
                   redirect,
                   jsonify
                    )
import json
import models
from datetime import datetime
from peewee import IntegrityError
from models  import Polling
 
app = Flask('app')
@app.route('/')
def index():
    models.initialize()
    return render_template("index.html")





@app.route('/polling', methods=['POST', 'GET'])
def register():
  data = dict(request.form.items())
  

  if data.get('description', None):
        Polling.create(
            understand_index=data.get('understand_index',3),
            reccomendation=data.get('reccomendation', 'felician'),
)
  return render_template("polling.html")


@app.route('/pollingstations')
def see_pollings():
  models.initialize()
  pollings = Polling.select()
  results = []
  for polling in pollings:
    results.append(
      {
        'understand_index':polling.understand_index,
        'reccomendations':polling.reccomendations,
        
      }
    )
  return render_template("all_pollings.html", pollings=pollings)



app.run(debug=True, host='0.0.0.0', port=8080)