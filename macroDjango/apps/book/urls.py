from django.urls import include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

import goods
from .views import GoodsListViewSet , CategoryViewset , BannerViewset , IndexCategoryViewset , HotSearchsViewset

router = DefaultRouter()

# 电商的商品列表
router.register(r'goods', GoodsListViewSet, basename="goodList")

# CategoryList
router.register(r'Category', CategoryViewset, basename="CategoryList")

# 轮播图
router.register(r'banners', BannerViewset, basename="banners")

# 首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")

# 查询热点内容
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")


app_name = "goods"
urlpatterns = [
    url(r"^", include(router.urls), name="good"),
]