from django.db import models
from apps.localUsers.models import LocalUser

# Create your models here.
class Post(models.Model):
  title = models.CharField('제목', max_length=24)
  content = models.CharField('내용', max_length=24)
  region = models.CharField('지역', max_length=24)
  # 작성자
  user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, verbose_name='작성자', null=True)
  price = models.IntegerField('가격', default=1000)
  # 이미지
  photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')

  # 생성 시각, 수정 시각
  created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
  updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)