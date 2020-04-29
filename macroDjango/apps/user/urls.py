from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from user.views import UserViewset , VerifyCodeViewSet
router = DefaultRouter()

# 用户
router.register(r'UserProfile', UserViewset, basename="UserProfile")
# 验证码
router.register(r'VerifyCode', VerifyCodeViewSet, basename="VerifyCode")

app_name = "user"
urlpatterns = [
    url(r"^", include(router.urls), name="user"),
]
