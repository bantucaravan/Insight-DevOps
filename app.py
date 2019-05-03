import datetime
import os
import json

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session
import pandas as pd

#import TEST

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success')) # request at the url for the 'success' function
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    results = []
    
    qry = db_session.query(Items)
    #qry = Items.query
    results = qry.all()
    #results = str(results).replace('<', '&lt;')
    #results = results.replace('>', '&gt;')
    results = {i : json.loads(str(rep)) for i, rep in enumerate(results)}
    results = pd.read_json(json.dumps(results), orient= 'index').to_html()

    return results
    #return str(results) #+ str(len(results))
    #return print(str(results) + str(len(results))) # debug only

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=5001)
