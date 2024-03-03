from django.db import models

# Create your models here.

class Feature(models.Model): #định nghĩa 1 model của django đặt tên là Feature, nó kế thừa models.Model
    name = models.CharField(max_length=100) #đặt tên biến là name, Đây là một trường ký tự (CharField) với độ dài tối đa là 100 ký tự. Trường này thường được sử dụng để lưu trữ tên ngắn
    
    details = models.CharField(max_length=500)