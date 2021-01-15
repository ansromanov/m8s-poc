from flask import render_template
import connexion
import pymongo

# Create the application instance
app = connexion.App(__name__, specification_dir='.')

app.add_api('swagger.yml')

@app.route('/')
def root():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
