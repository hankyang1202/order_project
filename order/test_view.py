
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client, TestCase
from .models import Order, OrderItem
from product.models import Product


class OrderShippingProportionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            "test1", "testuser1@test.com", "12345")

    def test_order_shipping_proportion_view(self):
        response = self.client.get(
            reverse(
                'order_shipping_proportion',
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order_proportion.html")
        self.assertContains(response, "訂單免運比例圓餅圖")
        self.assertContains(response, "系統目前無訂單")

    # TODO 測試圖片是否正確


class OrderMemberCohortViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            "test1", "testuser1@test.com", "12345")

    def test_order_member_cohort_view(self):
        response = self.client.get(
            reverse(
                'order_member_cohort',
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order_member_cohort.html")
        self.assertContains(response, "訂單用戶同類群組分析表")

    # TODO 測試圖片是否正確


class OrderPopularItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            "test1", "testuser1@test.com", "12345")

    def test_order_popular_item_view(self):
        response = self.client.get(
            reverse(
                'order_popular_item',
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order_popular_item.html")
        self.assertContains(response, "最受歡迎商品")

    # TODO 測試資料是否正確
