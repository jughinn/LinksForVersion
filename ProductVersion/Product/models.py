from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField('ProductName', max_length=50)
    description = models.TextField('Description', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Version(models.Model):
    version = models.CharField('Version', max_length=50, default=0)
    linux_portable_link = models.CharField('Linux_Portable_Version', max_length=50, default=0)
    linux_rpm_link = models.CharField('Linux_RPM_Version', max_length=50, default=0)
    windows_exe_link = models.CharField('Windows_Exe_Version', max_length=50, default=0)
    windows_msi_link = models.CharField('Windows_MSI_Version', max_length=50, default=0)
    mac_os_link = models.CharField('Mac_Os_Version', max_length=50, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = 'Product Version'
        verbose_name_plural = 'Product Versions'
