from django.db import models

# Create your models here.


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    heading0 = models.CharField(max_length=500, default="")
    cheading0 = models.CharField(max_length=5000, default="")
    heading1 = models.CharField(max_length=500, default="")
    cheading1 = models.CharField(max_length=5000, default="")
    heading2 = models.CharField(max_length=500, default="")
    cheading2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    author = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title
