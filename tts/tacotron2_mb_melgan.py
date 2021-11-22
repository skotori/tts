import tensorflow as tf

from tensorflow_tts.inference import AutoConfig
from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor

config_base_path = 'D:/workspace/tts/tts/config/'
model_base_path = 'D:/workspace/tts/tts/model/'

# processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-baker-ch")
processor = AutoProcessor.from_pretrained(pretrained_path=model_base_path + 'baker_mapper.json')

# tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-baker-ch", name="tacotron2")
tacotron2_config = AutoConfig.from_pretrained(config_base_path + 'tacotron2.baker.v1.yaml')
tacotron2 = TFAutoModel.from_pretrained(
    config=tacotron2_config,
    pretrained_path=model_base_path + 'tacotron2.h5',
    name="tacotron2"
)

# mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-baker-ch", name="mb_melgan")
mb_melgan_config = AutoConfig.from_pretrained(config_base_path + 'mb_melgan.baker.v1.yaml')
mb_melgan = TFAutoModel.from_pretrained(
    config=mb_melgan_config,
    pretrained_path=model_base_path + 'mb_melgan.h5',
    name="mb_melgan"
)

def do_synthesis(input_text):
    input_ids = processor.text_to_sequence(input_text, inference=True)

    # 文字转梅尔
    _, mel_outputs, stop_token_prediction, alignment_history = tacotron2.inference(
        tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        tf.convert_to_tensor([len(input_ids)], tf.int32),
        tf.convert_to_tensor([0], dtype=tf.int32)
    )

    # 语音合成
    # 移除 tacotron2 在结尾生成的噪音符号 :v.
    remove_end = 1024
    audio = mb_melgan.inference(mel_outputs)[0, :-remove_end, 0]

    return mel_outputs.numpy(), alignment_history.numpy(), audio.numpy()
