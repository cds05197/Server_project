from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Board(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  file_upload = models.FileField(upload_to='board/data/%Y/%m/%d/', blank=True)
  #file_upload는 장고에서 제공하는 파일 업로드 클래스 model field
  #url은 파일 경로->다운로드에 사용, Filename이 저장된다.
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return f'[PK:{self.pk}]-{self.title} :: {self.author}'
  
  def get_FileName(self):
    return os.path.basename(self.file_upload.name)
  # 파일의 경로명이 아닌 첨부파일명만 표시하기 위해서 사용
  def get_absolute_url(self):
    return f'/Board/{self.pk}'

