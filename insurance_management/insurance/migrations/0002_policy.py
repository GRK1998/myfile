from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=200)),
                ('sum_assurance', models.PositiveIntegerField()),
                ('premium', models.PositiveIntegerField()),
                ('tenure', models.PositiveIntegerField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Category')),
            ],
        ),
    ]
