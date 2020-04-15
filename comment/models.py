from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    # 作为一个外键关联进来
    user = models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)

    root= models.ForeignKey('self',related_name='root_comment',null=True,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',related_name='parent_comment',null=True,on_delete=models.CASCADE)
    reply_to=models.ForeignKey(User,related_name='replies',null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

    class Meta:
        # 倒序
        ordering = ['comment_time']