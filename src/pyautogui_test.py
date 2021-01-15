import gevent, random, pyautogui, os


def click(picture):
    while True:
        # 获取图片在屏幕中的左上角坐标,以及图片的宽高
        point = pyautogui.locateOnScreen(picture, confidence=0.8,grayscale=True)
        if point is not None:
            # 设置一些鼠标点击位置的随机位置,偏移量就是图片的宽高
            x = random.randint(point[0], point[0]+point[2])
            y = random.randint(point[1], point[1]+point[3])
            # 鼠标点击,duration是鼠标从当前位置移到指定位置需要的时间,单位秒
            pyautogui.click(x,y, duration=0.1)
        # 当前协程每执行一次都要休眠让行,不然会导致当前协程一直执行,休眠单位秒
        gevent.sleep(0.5)


if __name__ == '__main__':
    path = './images'
    gevents = []
    # 获取/images下所有文件名
    for filename in os.listdir(path):
        gevents.append(gevent.spawn(click, os.path.join(path, filename)))
    # 添加进协程池
    gevent.joinall(gevents)
