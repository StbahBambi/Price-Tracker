# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time

# coordinates_to_capture = [
#     (100, 100, "screenshot1.png"),
#     (200, 200, "screenshot2.png"),
#     (300, 300, "screenshot3.png"),
# ]
# # Set up the Chrome driver (you can use other browser drivers as well)
# driver = webdriver.Chrome()

# # Maximize the browser window
# driver.maximize_window()


# # # Open the desired URL
# # url = "https://www.google.com"
# # driver.get(url)


# # Find the latest screenshot index
# screenshot_folder = "C:/Users/radia/OneDrive/Bureau/PyProjects/Price-Tracker/Screenshots/"
# # existing_screenshots = [filename for filename in os.listdir(screenshot_folder) if filename.startswith("screenshot")]
# # latest_idx = max([int(filename.split("screenshot")[1].split(".png")[0]) for filename in existing_screenshots], default=0)

# # Increment the index for the new screenshot
# # idx = latest_idx + 1

# # Take a screenshot
# # screenshot_path = f"{screenshot_folder}screenshot{idx}.png"

# # for x, y, screenshot_filename in coordinates_to_capture:
# #     driver.set_window_size(1920, 1080)  # Set the window size if necessary
# #     driver.execute_script(f"window.scrollTo({x}, {y});")
# #     driver.save_screenshot(screenshot_filename)

# #####################################################################################



# website_url = "https://www.ouedkniss.com/"
# driver.get(website_url)
# time.sleep(5)

# # Find the specific element you want to capture
# element_selector = "row"
# element = driver.find_elements(By.CLASS_NAME, element_selector)
# # element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, element_selector)))
# # Capture a screenshot of the specific element
# for i, e in enumerate(element):
#     driver.execute_script("arguments[0].scrollIntoView();", e)
#     # wait = WebDriverWait(driver, 10)
#     # wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
#     screenshot_filename = f"element_screenshot{i}.png"
#     time.sleep(3)
#     screenshot = e.screenshot(screenshot_filename)
#     # time.sleep(3)
    

# # Close the browser
# driver.quit()

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up the Chrome driver (you can use other browser drivers as well)
# driver = webdriver.Chrome()

# # Open the desired URL
# website_url = "https://www.ouedkniss.com/"
# driver.get(website_url)

# # Define the CSS selector of the elements you want to capture
# element_selector = "row"

# # Wait for elements to be present and visible
# max_wait_time = 30
# elements = WebDriverWait(driver, max_wait_time).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, element_selector))
# )

# # Loop through elements and capture screenshots
# for i, element in enumerate(elements):
#     # Scroll to the element to ensure it's in view
#     driver.execute_script("arguments[0].scrollIntoView();", element)
    
#     # Wait for the element to become fully visible
#     WebDriverWait(driver, max_wait_time).until(
#         EC.visibility_of(element)
#     )
    
#     # Capture a screenshot of the element
#     screenshot_filename = f"element_screenshot{i}.png"
#     element.screenshot(screenshot_filename)

# # Close the browser
# driver.quit()





#############################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver (you can use other browser drivers as well)
driver = webdriver.Chrome()

# Open the desired URL
website_url = "https://www.ouedkniss.com/"
driver.get(website_url)

# Define the CSS selector of the elements you want to capture
element_selector = ".row"

# Wait for the first batch of elements to be present
max_wait_time = 10
elements = WebDriverWait(driver, max_wait_time).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, element_selector))
)

# # Capture initial screenshots
# for i, element in enumerate(elements):
#     screenshot_filename = f"element_screenshot{i}.png"
#     element.screenshot(screenshot_filename)

# Simulate scrolling to load more content
scroll_pause_time = 5
scrolls = 3  # Number of times to scroll

for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    # Capture newly loaded elements
    elements = driver.find_elements(By.CSS_SELECTOR, element_selector)
    for i, element in enumerate(elements):
        time.sleep(3)
        screenshot_filename = f"element_screenshot_{i}.png"
        element.screenshot(screenshot_filename)
        time.sleep(3)


# Close the browser
driver.quit()
