import pickle
from flask import Flask, request, jsonify

with open("model.pkl", 'rb') as file1:
    model = pickle.load(file1)
with open("count.pkl", 'rb') as file2:
    count = pickle.load(file2)

app = Flask(__name__)


@app.route('/getLabel', methods=['GET'])
def process_text_route():
    text = request.args.get('text')
    if not text:
        return jsonify({'error': 'Missing text parameter'}), 400

    result = get_label(text)
    return jsonify({'label': result})


def get_label(text):
    predict_matrix = count.transform([text]).toarray()
    result = model.predict(predict_matrix)
    return int(result[0])


if __name__ == '__main__':
    app.run(port=5000)
