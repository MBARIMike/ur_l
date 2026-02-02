from django.shortcuts import redirect
from django.urls import path, re_path
from django.views.decorators.cache import never_cache
from rest_framework.documentation import include_docs_urls

from . import api_views, views
from .apps import ApiConfig as conf


def _redirect_to_url_api_list_view(_):
    return redirect("/" + conf.API_URL_PATH)


urlpatterns = [
    path("", _redirect_to_url_api_list_view, name="root"),
    re_path(conf.SHORT_URL_PATH, never_cache(views.short_url), name="url_short"),
    path(conf.API_URL_PATH, api_views.UrlList.as_view(), name="url_list"),
    re_path(conf.API_TOKEN_PATH, api_views.UrlDetail.as_view(), name="url_get"),
    path(conf.API_ROOT_PATH, _redirect_to_url_api_list_view, name="url_root"),

    # Comment out to avoid this exception when bringing up stoqs with the adamwojt/adamwojt:ur_l_production image built here:
    # stoqs-shortener  |   File "/app/api/urls.py", line 22, in <module>
    # stoqs-shortener  |     include_docs_urls(title=conf.API_DOCS_TITLE),
    # stoqs-shortener  |     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # stoqs-shortener  |   File "/opt/pysetup/.venv/lib/python3.14/site-packages/rest_framework/documentation.py", line 61, in include_docs_urls
    # stoqs-shortener  |     docs_view = get_docs_view(
    # stoqs-shortener  |         title=title,
    # stoqs-shortener  |     ...<8 lines>...
    # stoqs-shortener  |         permission_classes=permission_classes,
    # stoqs-shortener  |     )
    # stoqs-shortener  |   File "/opt/pysetup/.venv/lib/python3.14/site-packages/rest_framework/documentation.py", line 20, in get_docs_view
    # stoqs-shortener  |     return get_schema_view(
    # stoqs-shortener  |         title=title,
    # stoqs-shortener  |     ...<8 lines>...
    # stoqs-shortener  |         permission_classes=permission_classes,
    # stoqs-shortener  |     )
    # stoqs-shortener  |   File "/opt/pysetup/.venv/lib/python3.14/site-packages/rest_framework/schemas/__init__.py", line 45, in get_schema_view
    # stoqs-shortener  |     generator = generator_class(
    # stoqs-shortener  |         title=title, url=url, description=description,
    # stoqs-shortener  |         urlconf=urlconf, patterns=patterns, version=version
    # stoqs-shortener  |     )
    # stoqs-shortener  |   File "/opt/pysetup/.venv/lib/python3.14/site-packages/rest_framework/schemas/coreapi.py", line 120, in __init__
    # stoqs-shortener  |     assert coreapi, '`coreapi` must be installed for schema support.'
    # stoqs-shortener  |            ^^^^^^^
    # stoqs-shortener  | AssertionError: `coreapi` must be installed for schema support.
    ##path(
    ##    conf.API_DOCS_PATH,
    ##    include_docs_urls(title=conf.API_DOCS_TITLE),
    ##    name="url_docs",
    ##),
]
