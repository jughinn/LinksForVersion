from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from Product.models import Version, Product


class VersionSerializer(ModelSerializer):
    product = StringRelatedField(read_only=True)

    class Meta:
        model = Version
        fields = ['product', 'version', 'lin_port_link', 'lin_rpm_link',
                  'win_exe_link', 'win_msi_link', 'mac_os_link']


class ProductSerializer(ModelSerializer):
    versions = VersionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'versions']


# class ProductSerializer(ModelSerializer):
#     versions = StringRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ['title', 'description', 'versions']
#
#
# class VersionSerializer(ModelSerializer):
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = Version
#         fields = ['product', 'version', 'lin_port_link', 'lin_rpm_link',
#                   'win_exe_link', 'win_msi_link', 'mac_os_link']
