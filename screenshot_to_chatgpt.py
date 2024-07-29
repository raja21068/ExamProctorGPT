import pyautogui
from PIL import Image
import pytesseract
import openai

# Capture a screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Open the screenshot
img = Image.open("screenshot.png")

# Use Tesseract to extract text
text = pytesseract.image_to_string(img)
print("Extracted Text:", text)

# Set OpenAI API key
openai.api_key = 'your-api-key'

# Send text to ChatGPT API
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  max_tokens=150
)

# Extract and print the answer
answer = response.choices[0].text.strip()
print("ChatGPT Answer:", answer)
