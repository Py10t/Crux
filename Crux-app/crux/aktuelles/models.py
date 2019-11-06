from django.db import models

DEFAULT_CUSTOMER_ID = 1
class Aktuelles(models.Model):
    """Aktuelles"""
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
# #     # delivery_date = models.ForeignKey('bestellung.Order', to_field='delivery_date', on_delete=models.CASCADE)
# #     # NEWamount = models.ForeignKey('bestellung.Order', to_field='amount', on_delete=models.CASCADE)
# #     # NEWorder_status = models.ForeignKey('bestellung.Order', to_field='order_status', on_delete=models.CASCADE)
#     stock_amount = models.ManyToManyField(
#         Person,
#         through='stock.Article',
#         through_fields=('group', 'person'),
#     )
# #     # NEWcustomer = models.ForeignKey('stock.Customer', on_delete=models.CASCADE, default=DEFAULT_CUSTOMER_ID)
# #     #
#     def __str__(self):
#         return str(self.stock_amount.stock_amount)
