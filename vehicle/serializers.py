from rest_framework import serializers

from vehicle.models import Car, Milage, Moto


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage')
    milage = MilageSerializer(many=True)

    class Meta:
        model = Car
        fields = "__all__"


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = "__all__"

    def create(self, validated_data):
        milage_data = validated_data.pop('milage')
        moto = Moto.objects.create(**validated_data)
        for milage in milage_data:
            Milage.objects.create(moto=moto, **milage)
        return moto


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = "__all__"

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')
