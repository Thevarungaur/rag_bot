# """
# This file downloads the LLM model required for the application's working, in GGUF format (which allows it to be run on CPU, instead of a dedicated GPU)
# """
# #
# import os
# import requests

# # Parameters that define where the model file is stored on the internet and where it needs to be downloaded locally
# MODEL_NAME = os.getenv("MODEL_NAME", "orca-mini")
# MODEL_SHA_DIGEST = os.getenv(
#     "MODEL_SHA_DIGEST", "66002b78c70a22ab25e16cc9a1736c6cc6335398c7312e3eb33db202350afe66")
# MODEL_URL = f"https://registry.ollama.ai/v2/library/" + \
#     f"{MODEL_NAME}/blobs/sha256:{MODEL_SHA_DIGEST}"
# MODEL_PATH = "./models/model.gguf"


# def download_model():
#     # Download the model file if it does not exist already
#     if not os.path.exists(MODEL_PATH):
#         print(f"Downloading the {MODEL_NAME} model from {MODEL_URL}...")
#         os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

#         try:
#             response = requests.get(MODEL_URL, stream=True)
#             response.raise_for_status()
#             with open(MODEL_PATH, 'wb') as f:
#                 for chunk in response.iter_content(chunk_size=8192):
#                     f.write(chunk)
#             print(f"Model downloaded successfully and saved to {MODEL_PATH}")
#         except requests.exceptions.RequestException as e:
#             print(f"Failed to download the model: {e}")
#         except IOError as e:
#             print(f"Failed to save the model to {MODEL_PATH}: {e}")
#     else:
#         print(f"{MODEL_PATH} already exists. Skipping re-downloading.")
