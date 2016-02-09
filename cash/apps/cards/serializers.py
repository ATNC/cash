from rest_framework import serializers

from models import Cards

class CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        lookup_field = 'cards_num'
        extra_kwargs = {
            'url': {'lookup_field': 'cards_num'}
        }
        fields = ('cards_num', 'cards_success',)


class CardsAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
