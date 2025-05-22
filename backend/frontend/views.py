
from .utils import get_vite_css_path, get_vite_js_path
from django.shortcuts import render



from django.contrib.auth.decorators import login_required


@login_required
def react_index(request):
    js_path = get_vite_js_path()
    css_path = get_vite_css_path()
    return render(request, 'frontend/index.html', { 'js_path': js_path, 'css_path': css_path })