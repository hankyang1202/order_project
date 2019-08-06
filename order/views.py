
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from io import BytesIO
from utils.base_view import BaseTemplateView
from .models import Order, OrderItem
import base64
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import pandas as pd


# Create your views here.
class OrderShippingProportionView(BaseTemplateView):

    template_name = 'order_proportion.html'

    def get(self, request, **kwargs):
        try:
            orders = Order.objects.all().filter(
                customer_id=request.user.id
            )
            shipping_fee_orders = orders.filter(shipping__gte=0)
            none_shipping_fee_orders = orders.filter(shipping=0)
            plt.figure(figsize=(6, 3))
            labels = ["shipping fee", "free shipping"]
            size = [
                shipping_fee_orders.count(),
                none_shipping_fee_orders.count()
                ]
            plt.pie(size,                         # 數值
                    labels=labels,                # 標籤
                    autopct="%1.1f%%",            # 將數值百分比並留到小數點一位
                    pctdistance=0.6,              # 數字距圓心的距離
                    textprops={"fontsize": 12}
                    )
            plt.axis('equal')
            plt.title("Shipping Proportion Plot")
            plt.legend(loc="best")
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            graphic = base64.b64encode(image_png)
            graphic = graphic.decode('utf-8')
            context = {'orders': orders, 'graphic': graphic}
        except Exception as e:
            raise e
        else:
            return self.render_to_response(context=context)


class OrderMemberCohortView(BaseTemplateView):

    template_name = 'order_member_cohort.html'

    def post(self, request, **kwargs):

        try:
            member_id = request.POST.get("member_id", None)
            orders = Order.objects.filter(
                customer_id=member_id
            ).extra({"date_created": "date(created_at)"})
            print(orders)
            if orders.count() > 0:
                date_order_count_list = orders.values(
                    'date_created').annotate(created_count=Count("order_id"))
                df = pd.DataFrame(date_order_count_list)

                df["date_created"] = pd.to_datetime(df.date_created)
                dates = df.set_index(
                    "date_created"
                ).resample("D").asfreq().index
                df = df.set_index(
                    "date_created"
                ).reindex(dates).fillna(0).reset_index()
                df["created_count"] = df["created_count"].astype(int)
                register_matplotlib_converters()
                plt.figure(figsize=(12, 4))
                plt.title('Member Order Cohort')
                plt.plot(df["date_created"], df["created_count"])
                plt.legend(loc="best")
                plt.gcf().autofmt_xdate()

                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()
                graphic = base64.b64encode(image_png)
                graphic = graphic.decode('utf-8')
                context = {'graphic': graphic}
            else:
                context = {"error_message": "此用戶無訂單"}

        except Exception as e:
            raise e
        else:
            return self.get(request=request, context=context)

    def get(self, request, **kwargs):
        try:
            users = User.objects.all()
            context = {'users': users}
            if 'context' in kwargs.keys():
                context.update(kwargs.get('context'))

        except Exception as e:
            raise e
        else:
            return self.render_to_response(context=context)


class OrderPopularItemView(BaseTemplateView):

    template_name = 'order_popular_item.html'

    def get(self, request, **kwargs):
        try:
            order_items = OrderItem.objects.all()
            order_sell_data = order_items.values(
                "product__product_name").annotate(
                    Sum("qty")).order_by("-qty__sum")
            context = {"order_sll_data": order_sell_data}
        except Exception as e:
            raise e
        else:
            return self.render_to_response(context=context)
