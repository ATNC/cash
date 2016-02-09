from django.contrib import admin
from models import Transactions, Cards

class TransactionsAdmin(admin.ModelAdmin):
    fields = ('transactions_link', 'transactions_code',
               'transaction_sum','transaction_timestamp',)
    readonly_fields = ('transaction_timestamp'),

admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Cards)
# Register your models here.
