from flask import request, jsonify
import requests
from bs4 import BeautifulSoup
import re


def set_routes(app):

    def validate_post_data(data: dict) -> bool:
        if not isinstance(data, dict):
            return False
        if not data.get('name') or not isinstance(data['name'], str):
            return False
        if data.get('age') and not isinstance(data['age'], int):
            return False
        return True

    @app.route('/', methods=['GET'])
    @api.doc(params={})
    def root():
        return 'Hello World!'

    @app.route('/healthz', methods=['GET', 'POST'])
    @api.doc(params={})
    def healthz():
        """
        /api entpoint
        GET - returns json= {'status': 'test'}
        POST -  {
                name - str not null
                age - int optionalf
                }
        :return:
        """
        if request.method == 'GET':
            return jsonify({'status': 'OK'})
        elif request.method == 'POST':
            if validate_post_data(request.json):
                return jsonify({'status': 'OK'})
            else:
                return jsonify({'status': 'bad input'}), 400

        else:
            return jsonify({'status': 'Bad method'})

    @app.route('/urls', methods=['GET'])
    @api.doc(params={})
    def urls():
        url='https://www.citilink.ru/catalog/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        data = []
        for category in soup.findAll('a', class_="CatalogLayout__item-link", attrs={'href': re.compile("^http(s)?://")}):
            data.append(category.get('href'))

        return jsonify({'data': data})