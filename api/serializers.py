from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer


from shoeapp.models import ShoeColor, ShoeType, Shoe, Manufacturer


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name', 'website')


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('shoe_colors',)


class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'

        )
