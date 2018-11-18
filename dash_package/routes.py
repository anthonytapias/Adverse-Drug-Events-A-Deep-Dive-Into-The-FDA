
# needed for routes/queries to show up online
from flask import render_template, jsonify, json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_sqlalchemy import SQLAlchemy
from dash_package.__init__ import app, db
from dash_package.models import *
from dash_package.dashboard import *
from dash_package import server
from dash_package.queries import *

#needed for routes/queries to run
from sqlalchemy import create_engine, func, or_
from sqlalchemy.orm import sessionmaker
import numpy as np
import operator


@server.route('/q')
def top_five_most_common_brands():
    list_of_all_brands_in_all_events = db.session.query(Brands.name).join(Brands_Events).join(Adverse_Events).all()
    list_of_cleaned_brands = []
    for i in list_of_all_brands_in_all_events:
        for y in i:
            list_of_cleaned_brands.append(y)
    dict_of_brands = {}
    for i in list_of_cleaned_brands:
        if i in dict_of_brands:
            dict_of_brands[i] += 1
        else:
            dict_of_brands[i] = 1
    sorted_list_of_tupes = sorted(dict_of_brands.items(), key=operator.itemgetter(1))
    return str(sorted_list_of_tupes[-5:])

# routes
# @app.callback(Output('graph-from-dropdown', 'figure'), # output a graph
#               [Input('holiday-drop-down', 'value')]) # our function render_content (below) will take as an input a value from the dropdown menu in the dashboard.py file.
# def render_content(value): #we pass in a value from the dropdown menu in dashboard.py
#     if value == 'Christmas': #if the value is 'Christmas', then we create a dictionary of parameters to fill in the graph whose id is 'graph from dropdown' in dashboard.py
#         return {'data': [
#                 {'x': [1, 2, 3], 'y': [5, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#                 ],
#         'layout': {
#             'title': 'Dash Data Visualization'
#             }
#             }
#     else:
#         return None # else return nothing (but automatically defaults to outputting a graph because of our decorator so just outputs a blank graph)
