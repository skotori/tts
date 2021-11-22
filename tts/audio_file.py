import uuid

import soundfile as sf

base_path = 'D:/workspace/tts/file/'

def do_save(audios):
    file_id = str(uuid.uuid4()).replace('-', '')
    file_path = base_path + file_id + '.wav'

    sf.write(file_path, audios, 24000)

    return file_id
