from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
import json
from models import Cards, Transactions


class IndexView(TemplateView):
    template_name = 'index.html'


    

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
# Create your views here.

def get_id(request):
    response = {}
    if request.session.get('card_id'):
        response['info'] = {
            'card_balance': request.usr.cards_balance,
            'card_num': request.usr.cards_num

        }
        return HttpResponse(json.dumps(response))
    return HttpResponse(json.dumps({'error': 'error'}))


def add_transaction(request):
    data = json.loads(request.GET.get('data'))
    card_num = request.session.get('card_id')
    if data.get('sum') == 'None':
        transaction = Cards.objects.filter(cards_num=card_num)
        if transaction:
            Transactions.objects.create(
                transactions_link = transaction[0],
                transactions_code = str(data.get('code')),
            )

            print 'ok'
    else:
        sum = int(data.get('sum'))
        transaction = Cards.objects.filter(cards_num=card_num)
        if transaction:
            transaction[0].cards_balance -= sum
            transaction[0].save()
            Transactions.objects.create(
                transactions_link = transaction[0],
                transactions_code = str(data.get('code')),
                transaction_sum = sum,
            )

            return HttpResponse(json.dumps({'ok':'ok'}))

def get_card(request):
    print json.loads(request.GET.get('data'))
    data = json.loads(request.GET.get('data'))
    response = {}
    cards_num = data.get('cards_num').split('-')
    cards_num = ''.join(cards_num)
    print "="*10,
    if data.get('cards_pin'):
        card = Cards.objects.get(cards_num=cards_num)
        print 'here', card.cards_pin == int(data.get('cards_pin'))
        if card.cards_pin == int(data.get('cards_pin')):
            request.session.set_expiry(600)
            #
            # print "="*20, request.usr.cards_balance
            request.session['card_id'] = int(cards_num)
            response['success'] = 'success'


        elif card.cards_success:
            card.decrement()
            response['error'] = 'invalid_pwd'
            response['count'] = card.cards_success
        else:
            response['error'] = 'block'

    else:
        card = Cards.objects.filter(cards_num=cards_num)
        if card:
            if card[0].cards_success:
                response['success'] = 'success'
            else:
                response['error'] = 'block'
        else:
            response['error'] = 'not_found'
        # print card.cards_success
    # context = self.get_context_data()

    return HttpResponse(json.dumps(response))

def logout(request):
    request.session.clear()
    return HttpResponse(json.dumps({'ok':'ok'}))
