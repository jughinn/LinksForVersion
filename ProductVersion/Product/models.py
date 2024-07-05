from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField('ProductName', max_length=50)
    description = models.TextField('Description', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    version = models.CharField('Version', max_length=50, default=0)
    lin_port_link = models.CharField('Linux_Version_Portable', max_length=50, default=0)
    lin_rpm_link = models.CharField('Linux_Version_RPM', max_length=50, default=0)
    win_exe_link = models.CharField('Windows_Version_Exe', max_length=50, default=0)
    win_msi_link = models.CharField('Windows_Version_MSI', max_length=50, default=0)
    mac_os_link = models.CharField('MacOs_Version', max_length=50, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продуктов'
