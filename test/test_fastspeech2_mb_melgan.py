from tts import fastspeech2_mb_melgan, audio_file

input_text = "我要发布一下测试环境服务，2021年11月18日，My name is Tom"

mels, audios = fastspeech2_mb_melgan.do_synthesis(input_text)
file_id = audio_file.do_save(audios)

print(file_id)
