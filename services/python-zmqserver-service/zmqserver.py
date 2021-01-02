import time
import zmq

HOST = '127.0.0.1'
PORT = '5556'

context = zmq.Context()
publisher = context.socket(zmq.PUB)
url = f'tcp://{HOST}:{PORT}'

def publish_message(message):
    try:
        publisher.bind(url)
        time.sleep(1)
        publisher.send_string(message)

    except Exception as e:
        print(f'error {e}')
    
    finally:
        publisher.unbind(url)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/downcase', methods=['GET'])
def lower_string():
    _strn = request.args.get('param')
    response = f'lower case of {_strn} is {_strn.lower()}'
    publish_message(response)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5010, debug=True)