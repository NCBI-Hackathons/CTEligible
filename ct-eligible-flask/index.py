from flask import jsonify, make_response, render_template

from app import app


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()  # Run the app
