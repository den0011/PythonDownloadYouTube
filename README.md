# PythonDownloadYouTube
Download YouTube video using Python

Распакуйте скачанный архив с [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
Укажите путь к исполняемому файлу ChromeDriver в переменной chrome_driver_path в вашем скрипте. Например, если вы распаковали архив и получили файл chromedriver.exe в папке **C:\path\to\chromedriver**, то путь будет **chrome_driver_path** = "**C:\path\to\chromedriver\chromedriver.exe**".
Обратите внимание, что путь к исполняемому файлу **ChromeDriver** должен быть абсолютным путем (полным путем к файлу). Убедитесь, что вы указываете правильный путь к исполняемому файлу **ChromeDriver** в вашем коде.

Если вы используете операционную систему **Mac или Linux**, файл **ChromeDriver** может иметь другое имя, например, chromedriver без расширения **.exe**. В этом случае укажите правильное имя файла в переменной **chrome_driver_path**.

Убедитесь, что версия ChromeDriver соответствует установленной версии браузера **Chrome**, и что вы установили все необходимые зависимости, включая Selenium **(pip install selenium)**.