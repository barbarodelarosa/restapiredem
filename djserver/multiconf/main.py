import os
from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
  cloud_name = os.getenv('CLOUD_NAME_CLOUDINARY'),
  api_key = os.getenv('API_KEY_CLOUDINARY'),
  api_secret = os.getenv('API_SECRET_CLOUDINARY')
)