from __future__ import unicode_literals

from django.db import models
import datetime

class Cards(models.Model):

    class Meta:
        ordering = ['cards_success']

    cards_num = models.CharField(max_length=16, verbose_name='Card id')
    cards_pin = models.PositiveSmallIntegerField(verbose_name='Card pin')
    cards_success = models.PositiveSmallIntegerField( default=4,
                                                verbose_name='Card success')
    cards_balance = models.IntegerField(default=0, verbose_name='Card balance')


    def decrement(self):
        if self.cards_success:
            self.cards_success -= 1
            super(Cards, self).save()


    def __unicode__(self):
        return "%s"%self.cards_num


class Transactions(models.Model):


    class Meta:
        ordering = ['-transaction_timestamp']

    CHECK_BALANCE = 'CB'
    GET_MONEY = 'GM'
    SUCCESS = 'SS'

    CODES = (
        (CHECK_BALANCE, 'Check balance'),
        (GET_MONEY, 'Trye gets money'),
        (SUCCESS, 'Success operation'),
    )

    transactions_link = models.ForeignKey(Cards, related_name='card', verbose_name='Card')
    transactions_code = models.CharField(max_length=2, choices=CODES)
    transaction_timestamp = models.DateTimeField(auto_now_add=True)
    transaction_sum = models.CharField(max_length=255, verbose_name='Transaction sum', default='0')


    def __unicode__(self):
        return '%s'% self.transactions_link