import pickle
from flask import Flask, request, jsonify

with open("model.pkl", 'rb') as file1:
    en_model = pickle.load(file1)
with open("count.pkl", 'rb') as file2:
    en_count = pickle.load(file2)
with open("ru_model.pkl", 'rb') as file3:
    ru_model = pickle.load(file3)
with open("ru_count.pkl", 'rb') as file4:
    ru_count = pickle.load(file4)

app = Flask(__name__)


@app.route('/getLabel', methods=['GET'])
def process_text_route():
    text = request.args.get('text')
    flag = request.args.get('flag')
    if not text and not flag:
        return jsonify({'error': 'Missing text or flag parameter'}), 400

    if flag == '0':
        result = get_label_en(text)
    elif flag == '1':
        result = get_label_ru(text)
    else:
        return jsonify({'error': "I don't know that flag"}), 400

    return jsonify({'label': result})


def get_label_en(text):
    predict_matrix = en_count.transform([text]).toarray()
    result = en_model.predict(predict_matrix)
    return int(result[0])


def get_label_ru(text):
    predict_matrix = ru_count.transform([text])
    result = ru_model.predict(predict_matrix)
    return int(result[0])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
