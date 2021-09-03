import chaojiying
# 对超级鹰网进行登录
from selenium import webdriver
import time
from PIL import Image

def login(username,password):
	# 定义为全局变量，否则可能闪退
	global driver
	driver = webdriver.Chrome()
	# 浏览器全屏方便截图
	driver.maximize_window()
	driver.get(url)
	# 等待界面加载
	time.sleep(1)
	driver.find_element_by_name("user").send_keys(username)
	driver.find_element_by_name("pass").send_keys(password)
	# 全屏截图
	driver.save_screenshot(img_path)
	# 获取页面中图片信息，为切割获取验证码做准备
	element = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img')    #找到验证码图片
	# 获取验证码图片的定位信息
	left = element.location['x']
	top = element.location['y']
	right = element.location['x'] + element.size['width']
	bottom = element.location['y'] + element.size['height']
	# 图片处理切割出验证码图片
	im = Image.open(img_path)
	im = im.crop((left, top, right, bottom))
	im.save(img_path)
	# 读取图片，发送给超级鹰获取验证码
	image = open(img_path, 'rb').read()
	code = chaojiying.digital_check_code(image, 1902)
	driver.find_element_by_name("imgtxt").send_keys(code)
	time.sleep(1)
	# 点击登陆按钮，触发登陆事件
	driver.find_element_by_class_name("login_form_input_submit").submit()

def main():
	global img_path,url
	url = 'https://www.chaojiying.com/user/login/' # url链接
	img_path = "code.png"    # 验证码保存地址
	username = "***" # 超级鹰账号
	password = "***" # 超级鹰账号密码
	login(username,password)

if __name__ == "__main__":
	main()