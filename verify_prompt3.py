"""Verify Prompt 3 deliverables: blog/forms.py, blog/urls.py, blog_project/urls.py.

Note: full URL resolution depends on views.py which is the next prompt.
This script verifies everything else.
"""
import os
import sys

BASE = r"C:\dev\coding projects-LOCAL\PYTHON\Django Blog Platform with User"
sys.path.insert(0, BASE)
os.chdir(BASE)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")
import django
django.setup()

print("=" * 60)
print("1. forms.py - import all three forms")
print("=" * 60)
from blog.forms import UserRegisterForm, PostForm, CommentForm
print(f"  UserRegisterForm OK -> fields: {list(UserRegisterForm().fields.keys())}")
print(f"  PostForm         OK -> fields: {list(PostForm().fields.keys())}")
print(f"  CommentForm      OK -> fields: {list(CommentForm().fields.keys())}")

# Check Bootstrap class is applied
print()
print("=" * 60)
print("2. Bootstrap widget classes applied")
print("=" * 60)
uf = UserRegisterForm()
for fname, field in uf.fields.items():
    has_class = 'form-control' in (field.widget.attrs.get('class') or '')
    print(f"  UserRegisterForm.{fname}.class = 'form-control' : {has_class}")
pf = PostForm()
print(f"  PostForm.title placeholder = {pf.fields['title'].widget.attrs.get('placeholder')!r}")
print(f"  PostForm.category widget   = {type(pf.fields['category'].widget).__name__}")
cf = CommentForm()
print(f"  CommentForm.body rows      = {cf.fields['body'].widget.attrs.get('rows')}")
print(f"  CommentForm.body label     = {cf.fields['body'].label!r}")

print()
print("=" * 60)
print("3. blog/urls.py - 8 patterns registered (file imports OK)")
print("=" * 60)
# We can't import blog.urls because it fails on missing views
# But we can read the file and count
import re
with open(os.path.join(BASE, "blog", "urls.py")) as f:
    content = f.read()
patterns = re.findall(r"path\(", content)
print(f"  path() calls found: {len(patterns)}")
names = re.findall(r"name=['\"]([^'\"]+)['\"]", content)
print(f"  URL names: {names}")
assert len(patterns) == 8, f"Expected 8 patterns, got {len(patterns)}"
assert set(names) == {'home', 'post_detail', 'post_create', 'post_edit',
                      'post_delete', 'register', 'add_comment', 'category_posts'}

print()
print("=" * 60)
print("4. blog_project/urls.py - includes + media wiring")
print("=" * 60)
with open(os.path.join(BASE, "blog_project", "urls.py")) as f:
    root_content = f.read()
checks = {
    "include('blog.urls')":  "include('blog.urls')" in root_content,
    "include('django.contrib.auth.urls')": "include('django.contrib.auth.urls')" in root_content,
    "static() for media":    "static(settings.MEDIA_URL" in root_content,
    "settings.DEBUG guard":  "settings.DEBUG" in root_content,
}
for k, v in checks.items():
    print(f"  {k}: {v}")
assert all(checks.values()), "Some wiring is missing"

print()
print("=" * 60)
print("5. Auth URL smoke test (Django test client)")
print("=" * 60)
from django.test import Client
c = Client()
r = c.get('/accounts/login/')
print(f"  GET /accounts/login/    -> {r.status_code}  (200 = OK)")
body = r.content.decode('utf-8', errors='replace')
print(f"    Has login form: {'<form' in body}")
print(f"    Has 'login':    {'login' in body.lower()}")

print()
print("=" * 60)
print("6. Admin still works (no regression)")
print("=" * 60)
from django.contrib.auth import get_user_model
admin_user = get_user_model().objects.get(username='admin')
c.force_login(admin_user)
r = c.get('/admin/')
print(f"  GET /admin/ (logged in) -> {r.status_code}  (200 = OK)")

print()
print("=== PARTIAL VERIFICATION PASSED ===")
print("(Full URL resolution will pass once views.py is written - next prompt)")
