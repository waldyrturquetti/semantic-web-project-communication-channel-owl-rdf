import os

from flask import Flask, redirect
from flask_graphql import GraphQLView
from dotenv import load_dotenv

from app.schema.schema import schema

load_dotenv()

app = Flask(__name__)
app.debug = True

port = int(os.getenv("PORT", 8080))

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def default_route():
    return redirect('/graphql', code=302)


if __name__ == '__main__':
    app.run(port=port)
