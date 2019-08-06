from django.urls import path, re_path
from .views import OrderShippingProportionView
from .views import OrderMemberCohortView, OrderPopularItemView

urlpatterns = [
    path(
        r'shipping_proportion/',
        OrderShippingProportionView.as_view(),
        name="order_shipping_proportion"
        ),
    re_path(
        r'member_cohort/$',
        OrderMemberCohortView.as_view(),
        name="order_member_cohort"
        ),
    path(r'popular_item/',
         OrderPopularItemView.as_view(),
         name="order_popular_item"
         )
]
