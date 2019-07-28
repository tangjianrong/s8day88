# Generated by Django 2.0 on 2019-03-12 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('telephone', models.BigIntegerField()),
                ('addr', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('publishDate', models.DateField()),
                ('read_num', models.IntegerField(default=0)),
                ('comment_num', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('authors', models.ManyToManyField(to='app01.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Publish'),
        ),
        migrations.AddField(
            model_name='author',
            name='authorDetail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
    ]
