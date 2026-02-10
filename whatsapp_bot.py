from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# ====== Start Browser ======
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com/")
print("Scan QR Code...")
time.sleep(20)  # Time to scan QR

# ====== Chat Name (Change this) ======
contact_name = "Friend Name"

while True:
    try:
        # Search contact
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        # Get last message
        messages = driver.find_elements(By.XPATH, '//div[contains(@class,"message-in")]')
        last_message = messages[-1].text

        print("Received:", last_message)

        # Simple AI logic
        if "hi" in last_message.lower():
            reply = "Hello 😎 I am your AI Bot!"
        elif "how are you" in last_message.lower():
            reply = "I am always powerful 💪"
        else:
            reply = "Interesting 🤔 Tell me more!"

        # Send reply
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(reply)
        message_box.send_keys(Keys.ENTER)

        time.sleep(10)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
