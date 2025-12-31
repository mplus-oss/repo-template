import os

import yaml

ANSWERS_FILE = ".copier-answers.yml"

def load_answers():
    if not os.path.exists(ANSWERS_FILE):
        return {}
    with open(ANSWERS_FILE) as f:
        return yaml.safe_load(f)
