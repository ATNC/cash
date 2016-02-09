from rest_framework import generics, permissions
from rest_framework.views import APIView
from serializers import CardsSerializer, CardsAuthSerializer
from models import Cards
from rest_framework.response import Response

class CardList(generics.ListCreateAPIView):
    model = Cards
    serializer_class = CardsSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Cards.objects.all()

class CardDetail(generics.RetrieveAPIView):
    model = Cards
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'cards_num'
    # def get_queryset(self):
    #     queryset = super(CardDetail,self).get_queryset()
    #     return queryset.filter(cards_num=self.kwargs.get('card_id'))
    # queryset = Cards.objects.all()

class Auth(APIView):
    model = Cards
    queryset = Cards.objects.all()

    serializer_class = CardsAuthSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, format=None):
        num = request.query_params.get('cards_num')
        pwd = request.query_params.get('cards_pin')
        card = Cards.objects.get(cards_num=num)
        print dir(card)
        response = {}
        if card.cards_pin == pwd:
            pass
        else:
            card.cards_success -= 1
            card.save()
            response['success'] = card.cards_success


        print card, 'qqqqq'

        return Response(response)