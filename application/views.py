from flask import Response, make_response, Request, request, session
from flask import render_template, flash, redirect, url_for
from application import application
from . import main

########################This starts the page renders#######################################


@application.route('/home', methods=['GET', 'POST'])
@application.route('/', methods=['GET', 'POST'])
def index():
    response = Response("")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    response.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    response.headers['Access-Control-Allow-Origin'] = '*'
    response = make_response(render_template('index.html',
                                             title='Rockset Demo'))
    return response

@application.route('/results', methods=['GET', 'POST'])
def submit():
        year = str(int(request.args['year']))
        response = Response("")
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
        response.headers["Pragma"] = "no-cache" # HTTP 1.0.
        response.headers["Expires"] = "0" # Proxies.
        response.headers['Access-Control-Allow-Origin'] = '*'
        popularity, revenue, genre, production_companies = main.main(year)
        response = make_response(render_template('results.html',
                                                 title='Rockset Demo Results',
                                                 year=year,
                                                 popularity = popularity,
                                                 revenue = revenue,
                                                 genre = genre,
                                                 production_companies = production_companies))
        return response
