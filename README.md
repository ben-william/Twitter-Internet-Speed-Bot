# Twitter Internet Speed Bot

Tweets a complaint if internet speed is below promised levels

```
Note: I am aware this project could use considerable refactoring to make it more robust, implement OOP, etc. 
This was a training exercise uploaded as-is.
I am currently focused on exploring new concepts rather than perfecting what currently exists. 
```

## How to Use
Here's a short guide on how to get this running.

### Internet Speed Thresholds
Update the PROMISED_UP and PROMISED_DOWN variables to your quoted speeds (in Mbps)

### Twitter Credentials
Update the USER and PW variables to an active Twitter account so Selenium can log in

### Selenium / Chrome
This project runs a Chrome browser with Selenium. To execute the script:

* Download an appropriate driver
  * Chrome Drivers can be downloaded here: https://chromedriver.chromium.org/downloads
* Update chrome_driver_path variable
