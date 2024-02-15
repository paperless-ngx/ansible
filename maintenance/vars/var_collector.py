import os
import re
from urllib.request import urlopen
from pathlib import Path

def get_pngx_docs_configuration_vars(pattern: str, version: str = 'latest') -> list:
    if version == 'latest':
        url = "https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/configuration.md"
    else:
        url = f"https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/v{version}/docs/configuration.md"
    content = urlopen(url).read().decode('utf-8')
    return re.findall(pattern, content, re.MULTILINE)

def get_role_readme_configuration_vars(pattern: str) -> list:
    file_path = os.path.dirname(__file__) + '/../../README.md'
    content = Path(file_path).read_text()
    return re.findall(pattern, content)

def get_role_defaults_vars(pattern: str) -> list:
    file_path = os.path.dirname(__file__) + '/../../defaults/main.yml'
    content = Path(file_path).read_text()
    return re.findall(pattern, content, re.MULTILINE)

def get_role_vars_vars(pattern: str) -> list:
    file_path = os.path.dirname(__file__) + '/../../vars/main.yml'
    content = Path(file_path).read_text()
    return re.findall(pattern, content, re.MULTILINE)

def get_role_configuration_tasks_file_vars(pattern: str) -> list:
    file_path = os.path.dirname(__file__) + '/../../tasks/paperless_ngx/configuration.yml'
    content = Path(file_path).read_text()
    return re.findall(pattern, content)