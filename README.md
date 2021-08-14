## How to run
1. Use pip to install selenium library
    ```
    pip install selenium
    ```
2. Download WebDriver(Default will use Microsoft Edge) and put it beside app.py. The WebDriver download link is as follows

    If want to use firefox, you need to download geckodriver, and then uncomment `browser = webdriver.Firefox(executable_path="geckodriver.exe")` and comment `browser = webdriver.Edge(executable_path=DRIVER)` in app.py

3. Run the app.py
    ```
    python app.py
    ```

## WebDriver

Microsoft Edge Driver
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

mozilla / geckodriver
https://github.com/mozilla/geckodriver/releases