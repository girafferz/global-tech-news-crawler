import re

def bodyTextJa(input):
    out = input.replace('あります', 'ある')
    out = out.replace('です。', '。')
    out = out.replace('します。', '。')
    out = out.replace('分かりました', '分かった');
    out = out.replace('しています', 'している')
    out = out.replace('ありません。', 'ない。')
    out = out.replace('ことです。', 'こと。')
    out = out.replace('のですか', 'のか')
    out = out.replace('かもしれません。', 'かもしれない。')
    out = out.replace('&quot;', '"')
    out = out.replace(' - クオラ', '')
    out = out.replace('', '')
    out = out.replace('', '')
    out = out.replace('', '')
    out = out.replace('', '')
    return out
