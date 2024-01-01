# Generated by Django 4.1.6 on 2023-05-05 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام برند')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productbrand', verbose_name=' برند'),
        ),
    ]