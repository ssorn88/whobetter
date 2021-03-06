

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('election', models.CharField(max_length=10, null=True)),
                ('party', models.CharField(max_length=20, null=True)),
                ('slogan', models.CharField(max_length=20, null=True)),
                ('keyword', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corona', models.CharField(max_length=20, null=True)),
                ('realty', models.CharField(max_length=20, null=True)),
                ('military', models.CharField(max_length=20, null=True)),
                ('politics', models.CharField(max_length=20, null=True)),
                ('economy', models.CharField(max_length=20, null=True)),
                ('construction', models.CharField(max_length=20, null=True)),
                ('environ', models.CharField(max_length=20, null=True)),
                ('science', models.CharField(max_length=20, null=True)),
                ('culture', models.CharField(max_length=20, null=True)),
                ('edu', models.CharField(max_length=20, null=True)),
                ('candi_dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promiseapp.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='DepartCon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coronaCon', models.TextField(null=True)),
                ('realtyCon', models.TextField(null=True)),
                ('militaryCon', models.TextField(null=True)),
                ('politicsCon', models.TextField(null=True)),
                ('economyCon', models.TextField(null=True)),
                ('constructionCon', models.TextField(null=True)),
                ('environCon', models.TextField(null=True)),
                ('scienceCon', models.TextField(null=True)),
                ('cultureCon', models.TextField(null=True)),
                ('eduCon', models.TextField(null=True)),
                ('candi_con', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promiseapp.depart')),
            ],
        ),
    ]
