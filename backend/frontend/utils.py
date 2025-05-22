
import os
import json
from django.conf import settings


def get_vite_js_path() -> str:
    manifest_path = os.path.join(
        settings.BASE_DIR, 'static', 'frontend', '.vite', 'manifest.json'
    )
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    if "index.html" not in manifest:
        raise ValueError(f"index.html not found in manifest.json")
    return settings.STATIC_URL + 'frontend/' + manifest["index.html"]['file']


def get_vite_css_path() -> str:
    manifest_path = os.path.join(
        settings.BASE_DIR, 'static', 'frontend', '.vite', 'manifest.json'
    )
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    if "index.html" not in manifest:
        raise ValueError(f"index.html not found in manifest.json")
    return settings.STATIC_URL + 'frontend/' + manifest["index.html"]['css'][0]
