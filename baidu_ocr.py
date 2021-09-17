from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '23634406'
API_KEY = 'IC3gl61doGfaM6cHzidaSax9'
SECRET_KEY = 'vXTt1BWq9a7GGzkAuEsA7IkXkDEfh2iK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
filePath = "C:\\Users\\admin\\Desktop\\test.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        image = fp.read()
        return image


image = get_file_content(filePath)
""" 调用通用文字识别（高精度版） """
client.basicAccurate(image)
""" 如果有可选参数 """
# options = {}
# options["detect_direction"] = "true"
# options["probability"] = "true"
""" 带参数调用通用文字识别（高精度版） """
res = client.basicAccurate(image)
print(res)
