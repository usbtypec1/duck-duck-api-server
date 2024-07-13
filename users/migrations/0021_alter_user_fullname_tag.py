# Generated by Django 4.2.7 on 2024-04-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_country_nationality_user_gender_user_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='Anonymous', max_length=64),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=32)),
                ('weight', models.PositiveSmallIntegerField(choices=[(1, 'Gold'), (2, 'Silver'), (3, 'Bronze')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('of_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='given_tag', to='users.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_tag', to='users.user')),
            ],
        ),
    ]