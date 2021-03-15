# 模拟登入12306
from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains
from Cjy import Chaojiying_Client
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://kyfw.12306.cn/otn/login/init')
sleep(5)
bro.save_screenshot('main.png')    # 这个截图对图片格式有要求需要为.png

code_img_tag = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')

location = code_img_tag.location
size = code_img_tag.size
print(location, type(location))
print(size)
#裁剪的区域范围
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

print(rangle)
# 裁剪图
i = Image.open('./main.png')
frame = i.crop(rangle)
frame.save('code.png')


def get_text(imgPath,imgType):
    chaojiying = Chaojiying_Client('bobo328410948', 'bobo328410948', '899370')
    im = open(imgPath, 'rb').read()
    return chaojiying.PostPic(im, imgType)['pic_str']


#55,70|267,133 ==[[55,70],[33,66]]
result = get_text('./code.png',9004)
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)
# action = ActionChains(bro)
for a in all_list:
    x = a[0]
    y = a[1]
    ActionChains(bro).move_to_element_with_offset(code_img_tag,x,y).click().perform()
    sleep(1)

bro.find_element_by_id('username').send_keys('123456')
sleep(1)
bro.find_element_by_id('password').send_keys('67890000000')
sleep(1)
bro.find_element_by_id('loginSub').click()

sleep(5)
bro.quit()







