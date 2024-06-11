from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/question', methods=['POST'])
def question():
    data = request.json
    query = data.get('query')

    # NtelsAI 서버로 요청 보내기
    response = requests.post(
        'http://192.168.15.94:8000/question',
        json={"query": query},
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        answer = response.json().get('query', {}).get('content', 'No answer received')
    else:
        answer = 'Error in fetching response'

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)
