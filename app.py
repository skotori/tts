from flask import Flask, request, jsonify, Response

from tts import tacotron2_mb_melgan, audio_file, phonology_symbol

app = Flask(__name__)

@app.route('/')
@app.route('/hi')
def hi():
    return 'hi'

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_data()
    text = data.decode()

    print(text)

    input_text = phonology_symbol.do_replace(text)
    mels, alignment_history, audios = tacotron2_mb_melgan.do_synthesis(input_text)
    file_id = audio_file.do_save(audios)

    print(file_id)

    result = {
        'code': 1,
        'msg': '成功',
        'data': '/download/' + file_id
    }
    return jsonify(result)

@app.route('/download/<file_id>', methods=['GET'])
def download(file_id):
    print(file_id)

    file_name = file_id + '.wav'
    file_path = audio_file.base_path + file_name

    def send_file():
        with open(file_path, 'rb') as target_file:
            while 1:
                data = target_file.read(20 * 1024 * 1024)
                if not data:
                    break
                yield data

    response = Response(send_file(), content_type='application/octet-stream')
    response.headers["Content-disposition"] = 'attachment; filename=' + file_name
    return response

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8888)
