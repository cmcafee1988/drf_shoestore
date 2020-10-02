from django.db import models

# While growing up on the African Savanah, Joe spent many days running with herds of grazing
# antelopes while wearing his favorite violet colored sneakers


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()


class ShoeType(models.Model):
    Sneaker = 'S'
    Boot = 'B'
    Sandal = 'SL'
    Dress = 'D'
    Other = 'O'

    SHOE_TYPE_CHOICES = [
        (Sneaker, 'sneaker'),
        (Boot, 'boot'),
        (Sandal, 'sandal'),
        (Dress, 'dress'),
        (Other, 'other')

    ]
    style = models.CharField(
        max_length=20,
        choices=SHOE_TYPE_CHOICES
    )


class ShoeColor(models.Model):
    Red = 'R'
    Orange = 'O'
    Yellow = 'Y'
    Green = 'G'
    Blue = 'B'
    Indigo = 'I'
    Violet = 'V'
    White = 'W'
    Black = 'BLK'

    SHOE_COLOR_CHOICES = [
        (Red, 'Red'),
        (Orange, 'Orange'),
        (Yellow, 'Yellow'),
        (Green, 'Green'),
        (Blue, 'Blue'),
        (Indigo, 'Indigo'),
        (Violet, 'Violet'),
        (White, 'White'),
        (Black, 'Black'),
    ]

    shoe_colors = models.CharField(
        max_length=10,
        choices=SHOE_COLOR_CHOICES
    )

class Shoe (models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=200)
    shoe_type = models.ForeignKey(ShoeType, models.CASCADE)
    fasten_type = models.CharField(max_length=120)
