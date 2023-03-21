from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   # 생성일
    updated_at = models.DateTimeField(auto_now=True)   # 업데이트일 ( 수정일 )
    image = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.id}번째 글 - {self.title}'