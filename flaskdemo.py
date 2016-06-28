import json
from repository import Repository
from flask import Flask, request, g, abort, jsonify, Response


# default configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create app object
app = Flask(__name__)

# read default config from the above variables, and allow override with environment variable
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# utility function - flask.jsonify doesn't json arrays unless they're wrapped in an object
# Todo: pretty print the json
def jsonify_array(obj):
    return Response(json.dumps(obj),  mimetype='application/json')


def get_repo():
    # This attaches a repository instance to "g" or the global request context.
    # This way, only one database connection per http request gets created, even if you
    # make multiple calls to get_repo().
    repo = getattr(g, 'repository', None)
    if repo is None:
        repo = Repository(DATABASE)
        g.repository = repo

    return repo


# called  automaticallyw hen we're done a request - close connection to DB
@app.teardown_appcontext
def close_db_connection(exception):
    repo = get_repo()
    if repo is not None:
        repo.dispose()


# Base route for the Api
api_base = '/api/Entries/'


# Checks if the params contains a query that we don't support.
# Returns false in this case, otherwise true.
def validate_query_params(expected: list, params: list) -> bool:
    for key in params:
        if key not in expected:
            return False
    return True


@app.route(api_base)
def api_list_entries():
    if not validate_query_params(['keyword'], request.args):
        return 'Unsupported query parameter', 400

    keyword = request.args.get('keyword')
    object_result = get_repo().list_entries(keyword)

    return jsonify_array(object_result)


@app.route(api_base + '<int:id>')
def api_get_entry(id: int) -> object:
    object_result = get_repo().get_entry(id)

    if object_result is None:
        abort(404)  # 404 Not Found

    return jsonify(object_result)  # Returning an object in flask automagically makes it a 200 OK


if __name__ == '__main__':
    with open('schema.sql') as f, Repository(DATABASE) as repo:
        print('Repopulating the demo database.')
        repo.init_db(f.read())
    # Run the app
    app.run(debug=True, threaded=True, host='0.0.0.0')
