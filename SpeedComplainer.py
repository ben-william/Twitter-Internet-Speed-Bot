from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PROMISED_UP = 50
PROMISED_DOWN = 200
USER = "<<Twitter Username Here>>"
PW = "<<Password Here>>"
TWITTER_URL = "https://twitter.com/i/flow/login"
SPEEDTEST_URL = "https://www.speedtest.net/"
chrome_driver_path = "<<Filepath to Chrome Driver>>"


class InternetSpeedTwitterBot:

    def __init__(self):

        s = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=s)

    def get_internet_speed(self):

        self.driver.get(url=SPEEDTEST_URL)

        try:
            self.go = WebDriverWait(self.driver, 30)\
                .until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button")))
            self.go.click()

            self.modal_button = WebDriverWait(self.driver, 90)\
                .until(EC.element_to_be_clickable((By.LINK_TEXT, "Back to test results")))
            self.modal_button.click()

            speed_link = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.result-data[data-result-id="true"] a')))\
                .get_attribute('href')

            down = float(self.driver.find_element(By.CSS_SELECTOR,
                                            'span[class="result-data-large number result-data-value download-speed"]').text)
            up = float(self.driver.find_element(By.CSS_SELECTOR,
                                            'span[class="result-data-large number result-data-value upload-speed"]').text)

        except TimeoutError:
            print('Timeout Error in SpeedTest')

        finally:
            print(down)
            print(up)
            if down < PROMISED_DOWN or up < PROMISED_UP:
                print('tweet')
                twitterbot = bot.tweet(down, up, speed_link)
            else:
                print('quit')
                twitterbot = bot.tweet(down, up, speed_link)
                self.driver.quit()

            return down, up, speed_link

    def tweet(self, down, up, speed_link):

        self.driver.get(url=TWITTER_URL)

        try:

            user_input = WebDriverWait(self.driver, 30)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="username"]')))

            user_input.click()
            user_input.send_keys(USER)

            next_button = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')))
            next_button.click()

            pw_input = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autocomplete="current-password"]')))
            pw_input.click()
            pw_input.send_keys(PW)
            pw_input.send_keys(Keys.ENTER)

            new_tweet_btn = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Tweet"]')))
            new_tweet_btn.click()

            tweet_input = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')))
            tweet_input.send_keys(f'This internet speed is not what I paid for! Download speed is {down} Mbps '
                                  f'with {up} Mbps upload!\nSource: {speed_link}')

            send_tweet_btn = WebDriverWait(self.driver, 10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="tweetButton"]')))
            send_tweet_btn.click()

        except TimeoutError:
            print('Timeout Error in Twitter')

        finally:
            self.driver.quit()


bot = InternetSpeedTwitterBot()
speedbot = bot.get_internet_speed()

