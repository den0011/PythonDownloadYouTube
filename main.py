from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

# URL видео на YouTube
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"  # Путь

# Создание объекта ChromeOptions и настройка параметров
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без отображения окна браузера
chrome_options.add_argument("--no-sandbox")  # Отключение использования песочницы (sandbox)
chrome_options.add_argument("--disable-dev-shm-usage")  # Отключение использования /dev/shm

# Путь к исполняемому файлу ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)
chrome_driver_path = "/путь/к/chromedriver"

# Создание объекта WebDriver для браузера Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Открытие страницы YouTube
driver.get(video_url)

# Пауза для загрузки страницы и воспроизведения видео
time.sleep(5)

# Поиск элемента с видео и получение URL видео
video_element = driver.find_element_by_tag_name("video")
video_url = video_element.get_attribute("src")

# Скачивание видео
response = requests.get(video_url)
with open("video.mp4", "wb") as f:
    f.write(response.content)

# Закрытие браузера
driver.quit()