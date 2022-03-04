# -*- coding: utf-8 -*-

"""
@Time    : 2022/3/3 1:32 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from dotenv import load_dotenv

# Load environment variables
# needs to happen before anything else (to properly instantiate constants)
load_dotenv(verbose=True, override=True)

import os

mailchimp_api_key = os.environ.get("MAILCHIMP_API_KEY", "")

mailchimp_list = os.environ.get("MAILCHIMP_LIST", "")

gdrive_credentials = os.environ.get("GDRIVE_CREDENTIALS", "")

algolia_app_id = os.environ.get("ALGOLIA_APP_ID", "")

algolia_search_key = os.environ.get("ALGOLIA_SEARCH_KEY", "")

algolia_docs_index = os.environ.get("ALGOLIA_DOCS_INDEX", "")

rasa_x_host = os.environ.get("RASA_X_HOST", "rasa-x:5002")

rasa_x_password = os.environ.get("RASA_X_PASSWORD", "")

rasa_x_username = os.environ.get("RASA_X_USERNAME", "me")

rasa_x_host_schema = os.environ.get("RASA_X_HOST_SCHEMA", "http")