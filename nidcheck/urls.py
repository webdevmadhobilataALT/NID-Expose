

"""
URL Configuration file
fot the app-level directory
"""



from django.urls import path

from .views import NIDCheckView, NIDResultView


urlpatterns = [
    path(
        "",
        NIDCheckView.as_view(),
        name="nid_check",
    ),

    path(
        "result/<uuid:pk>/",
        NIDResultView.as_view(),
        name="nid_result",
    ),
]

