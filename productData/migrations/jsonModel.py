from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_price', models.CharField(blank=True, null=True)),
                ('product_category', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
