# Generated by Django 2.0.7 on 2020-12-13 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsBrowser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='浏览时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '用户浏览记录',
                'verbose_name_plural': '用户浏览记录',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('ctitle', models.CharField(max_length=20, verbose_name='商品名称')),
                ('cusername', models.CharField(max_length=20, verbose_name='买家昵称')),
                ('cusername1', models.CharField(max_length=20, verbose_name='卖家昵称')),
                ('ccontent_chart', tinymce.models.HTMLField(max_length=200, verbose_name='消息内容')),
                ('ccheck', models.BooleanField(default=False, verbose_name='消息是否已读')),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='tuihuoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=20, verbose_name='商品名称')),
                ('username', models.CharField(max_length=20, verbose_name='收件人姓名')),
                ('username1', models.CharField(max_length=20, verbose_name='寄件人姓名')),
                ('person_number', models.CharField(max_length=20, verbose_name='身份证号码')),
                ('order_number', models.CharField(max_length=20, verbose_name='订单号')),
                ('kuaidi', models.CharField(max_length=20, verbose_name='快递类型')),
                ('kuaidi_number', models.CharField(max_length=20, verbose_name='快递单号')),
                ('address', models.CharField(default=None, max_length=50, verbose_name='收货地址')),
                ('address1', models.CharField(default=None, max_length=50, verbose_name='发货地址')),
                ('text', tinymce.models.HTMLField(default=None, max_length=200, verbose_name='退货理由')),
                ('passOrdefault', models.BooleanField(default=False, verbose_name='同意退款')),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
            ],
            options={
                'verbose_name': '退款订单',
                'verbose_name_plural': '退款订单',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('usex', models.CharField(default='', max_length=10, verbose_name='性别')),
                ('uage', models.CharField(default='', max_length=10, verbose_name='年龄')),
                ('upersonInf', models.CharField(default='', max_length=200, verbose_name='个人简介')),
                ('ulogo', models.FileField(default='default.jpg', upload_to='images', verbose_name='用户头像')),
                ('upwd', models.CharField(max_length=40, verbose_name='用户密码')),
                ('uemail', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('urealname', models.CharField(default='', max_length=20, verbose_name='真实姓名')),
                ('uzhengjian_type', models.CharField(default='', max_length=20, verbose_name='证件类型')),
                ('uzhengjian_tel', models.CharField(default='', max_length=18, verbose_name='证件号码')),
                ('uzhengjian_img', models.FileField(default='', upload_to='images/zhengjian_img', verbose_name='证件图片')),
                ('ucheck_passOrfail', models.BooleanField(default=False, verbose_name='认证审批')),
                ('ushou', models.CharField(default='', max_length=20, verbose_name='收货名称')),
                ('uaddress', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('uyoubian', models.CharField(default='', max_length=6, verbose_name='邮编')),
                ('uphone', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('uname_passOrfail', models.BooleanField(default=True, verbose_name='允许登录')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='information',
            name='cinformation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='消息'),
        ),
        migrations.AddField(
            model_name='goodsbrowser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo', verbose_name='用户ID'),
        ),
    ]