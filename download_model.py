import os
import urllib.request

MODEL_URL = "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"
MODEL_DIR = "models"
MODEL_NAME = "ggml-gpt4all-j-v1.3-groovy.bin"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

def download_model():
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    if os.path.exists(MODEL_PATH):
        print(f"Model already exists at {MODEL_PATH}")
        return
    print(f"Downloading GPT4All model (~4GB). This will take several minutes...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print(f"Model downloaded successfully to {MODEL_PATH}")

if __name__ == "__main__":
    download_model()
