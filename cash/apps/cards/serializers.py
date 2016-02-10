from rest_framework import serializers

from models import Cards

class CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        lookup_field = 'cards_num'
        extra_kwargs = {
            'url': {'lookup_field': 'cards_num'}
        }
        # fields = ('cards_num', 'cards_success', 'cards_')
        # def update(self, instance, validated_data):
        #     instance.decrement()
        #     print instance.cards_success, "+"*20
        #     return instance


class CardsAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
