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
    out = out.replace('角度', 'Angular')
    out = out.replace('角', 'Angular')
    out = out.replace('\ x99t', '')
    out = out.replace('\ x99ll', '')
    out = out.replace('\ x99s', '')
    out = out.replace('\ xe2', '')
    out = out.replace('\ x80', '')
    out = out.replace('\ x98', '')
    out = out.replace('\ xa6', '')
    out = out.replace('\ x9d', '')
    out = out.replace('\ x9c', '')
    out = out.replace('\ x93', '')
    out = out.replace('\ x99', '')
    out = out.replace('', '')
    out = out.replace('', '')
    out = out.replace('', '')
    out = out.replace('', '')
    return out
