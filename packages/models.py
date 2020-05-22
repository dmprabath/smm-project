from django.db import models


class Packages(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    socialMedia = models.TextField()
    psotNo = models.IntegerField()
    videoNo = models.IntegerField()
    reportType = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    costomCompany = models.TextField()
    target = models.TextField()
    otherAd = models.TextField()
    gurant = models.CharField(max_length=255)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.title
