from tts import tacotron2_mb_melgan, audio_file, word_file, phonology_symbol

# text = "我要发布一下测试环境服务，1234567890元，2021年11月19日18时16分10秒，1/2，88%，36℃。My name is Tom."
file_path = 'D:/workspace/tts/file/test.docx'
text = word_file.do_read(file_path)

print(text)

input_text = phonology_symbol.do_replace(text)

print(input_text)

mels, alignment_history, audios = tacotron2_mb_melgan.do_synthesis(input_text)
file_id = audio_file.do_save(audios)

print(file_id)
