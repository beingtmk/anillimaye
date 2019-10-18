from django.urls import path

from anillimaye.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    contact,
    news_letter
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("contact/", contact, name="contact"),
    path("news_letter/", news_letter, name="news_letter"),

]
