from aip import AipSpeech

APP_ID = '123176612'
API_KEY = 'V6FbxHYABg1Pxaza2APly5en'
SECRET_KEY = 'GFqk5ZfGvTNJkci5lfrsD0zIZFhqVF9X'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

text = "你好，我的第一个百度AI项目跑通了，感觉真棒！"

result = client.synthesis(text, 'zh', 1, {'vol': 5, 'spd': 5, 'pit': 5, 'per': 0})

if not isinstance(result, dict):
    with open('output.mp3', 'wb') as f:
        f.write(result)
    print("成功！音频文件已保存为 output.mp3")
else:
    print("出错了：", result)
