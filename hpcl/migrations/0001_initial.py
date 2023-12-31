# Generated by Django 4.2.4 on 2023-08-25 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractemployee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('quali', models.CharField(blank=True, choices=[('skilled', 'Skilled'), ('unskilled', 'Unskilled'), ('semiskilled', 'Semi Skilled'), ('highly_skilled', 'Highly Skilled')], max_length=20, null=True)),
                ('org_name', models.CharField(blank=True, max_length=100, null=True)),
                ('desg', models.CharField(blank=True, max_length=50, null=True)),
                ('ven_code', models.CharField(blank=True, max_length=20, null=True)),
                ('basic', models.CharField(blank=True, max_length=20, null=True)),
                ('doj', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10, null=True)),
                ('add1', models.CharField(blank=True, max_length=100, null=True)),
                ('add2', models.CharField(blank=True, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, max_length=100, null=True)),
                ('mob', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('esic_enrolled', models.CharField(blank=True, max_length=20, null=True)),
                ('esic_location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Contractemployee',
                'managed': False,
            },
        ),
    ]
