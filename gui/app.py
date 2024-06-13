from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    print("index.html 실행")
    return render_template('index.html')

@app.route('/update_content/<page>')
def update_content(page):
    if page == 'addfile':
        print("addfile")
        return render_template('addfile.html')
    elif page == 'search':
        print("search")
        return render_template('search.html')
    elif page == 'setting':
        print("setting")
        return render_template('setting.html')
    else:
        return ''

@app.route('/question', methods=['POST'])
def question():
    data = request.json
    query = data.get('query')
    print(f"Received query: {query}")  # 로깅 추가

    # NtelsAI 서버로 요청 보내기
    try:
        response = requests.post(
            'http://192.168.15.94:8000/question',
            json={"query": query},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        answer = response.json().get('query', {}).get('content', 'No answer received')
    except requests.RequestException as e:
        print(f"Error fetching response: {e}")  # 로깅 추가
        answer = 'Error in fetching response'

    print(f"Returning answer: {answer}")  # 로깅 추가
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
