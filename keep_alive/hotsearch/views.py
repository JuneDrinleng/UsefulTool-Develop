from django.shortcuts import render
from .utils.log_utils import get_log_path

def home(request):
    with open(get_log_path(), "r", encoding="utf-8") as f:
        log_content = f.read()
    return render(request, "index.html", {"log": log_content})