import tensorflow as tf

from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor

processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-baker-ch")
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-baker-ch", name="fastspeech2")
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-baker-ch", name="mb_melgan")

def do_synthesis(input_text):
    input_ids = processor.text_to_sequence(input_text, inference=True)

    # 文字转梅尔
    mel_before, mel_outputs, duration_outputs, _, _ = fastspeech2.inference(
        tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        f0_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        energy_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # 语音合成
    remove_end = 1
    audio = mb_melgan.inference(mel_outputs)[0, :-remove_end, 0]

    return mel_outputs.numpy(), audio.numpy()
