import logging
import sys

from playwright.sync_api import sync_playwright

# 创建一个日志器logger并设置其日志级别为DEBUG
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# 创建一个流处理器handler并设置其日志级别为DEBUG
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# 创建一个格式器formatter并将其添加到处理器handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 为日志器logger添加上面创建的处理器handler
logger.addHandler(handler)


def usage_01():

    player = sync_playwright().start()

    # slow_mo 表示每个动作之间的间隔时间
    browser = player.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    browser.close()
    player.stop()


def main():
    usage_01()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.fatal(e)
