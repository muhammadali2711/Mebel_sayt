# Generated by Django 4.1.5 on 2023-01-31 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0002_subcategory_category_parent_product_maqsad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ctg',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_ctg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sayt.subcategory'),
            preserve_default=False,
        ),
    ]
