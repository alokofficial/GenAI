import requests

# def extract_text_from_image(image_path, api_key):
#     url = "https://api.ocr.space/parse/image"
#     payload = {
#         "apikey": api_key,
#         "language": "eng",  # Change this if your image contains text in a different language
#     }
#     with open(image_path, "rb") as image_file:
#         files = {"file": image_file}
#         response = requests.post(url, files=files, data=payload)
#         result = response.json()
#         if "ParsedResults" in result:
#             extracted_text = result["ParsedResults"][0]["ParsedText"]
#             return extracted_text
#         else:
#             return None

def extract_text_from_image(image, api_key):
    url = "https://api.ocr.space/parse/image"
    payload = {
        "apikey": api_key,
        "language": "eng",  # Change this if your image contains text in a different language
    }
    response = requests.post(url, files={"file": image}, data=payload)
    result = response.json()
    if "ParsedResults" in result:
        extracted_text = result["ParsedResults"][0]["ParsedText"]
        return extracted_text
    else:
        return None

# Replace 'YOUR_API_KEY' with your actual OCR.space API key
api_key = "K81405423488957"

# Path to the image file you want to extract text from
image_path = "unnamed.png"

extracted_text = extract_text_from_image(image_path, api_key)
print(extracted_text)
