from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Version, Product


class VersionSerializer(ModelSerializer):
    product = StringRelatedField(read_only=True)

    class Meta:
        model = Version
        fields = ['product', 'version', 'linux_portable_link', 'linux_rpm_link',
                  'windows_exe_link', 'windows_msi_link', 'mac_os_link']


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
#         fields = ['product', 'version', 'linux_portable_link', 'linux_rpm_link',
#                   'windows_exe_link', 'windows_msi_link', 'mac_os_link']
