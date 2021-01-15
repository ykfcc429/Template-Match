# Template-Match
使用pyautogui进行图片定位,并点击,用协程的方式运行,占用资源低,效率中等,代码简易


##首先需要安装一些组件来支持:

* pip install gevent 
* pip install pyautogui 
* pip install opencv-python 

代码很短,注释很清晰,可以用来实现一些点点点游戏的挂机,比如说阴阳师

如果不想运行代码,只是执行默认程序的话可以下载windows直接运行的版本

默认情况下,在程序同目录新建一个images文件夹,里面放好所有需要匹配的
图片,程序开始运行后会不断的在屏幕中去寻找所有的图片,找到了就会点击一次该
图片所在的位置.