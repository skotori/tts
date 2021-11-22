import cn2an

from zhon.hanzi import punctuation
import string

def do_replace(text):
    # 阿拉伯数字转中文数字
    text = cn2an.transform(text, "an2cn")

    # 中文标点符号转停顿音符
    # ＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､　、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。
    chinese_punctuation_str = punctuation
    for i in chinese_punctuation_str:
        text = text.replace(i, '#3')

    # 英语标点符号转停顿音符
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    english_punctuation_str = string.punctuation
    for i in english_punctuation_str:
        if i != '#':
            text = text.replace(i, '#3')

    # 空格转停顿音符
    text = text.replace(' ', '#3')

    return text
