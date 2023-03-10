# Generated by Django 4.1.4 on 2023-01-29 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('is_public', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='pet.petcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='pet',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.petcategory'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
