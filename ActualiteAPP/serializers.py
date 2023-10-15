from rest_framework import serializers

from ActualiteAPP.models import Actualite


class ActualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields=('ActualiteId','ActualiteTitle','ActualiteDescription','ActualiteDate','ActualiteTag','ActualiteImage')

class ImageSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Actualite
        fields = ('ActualiteImage')

    def get_image_url(self, obj):
        return obj.image.url