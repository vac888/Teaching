from django.db import models
    
class myquadric(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    x1 = models.TextField()
    x2 = models.TextField()
    x_answer_1 = models.TextField()
    x_answer_2 = models.TextField()
    status_answer = models.TextField()

    def __str__(self):
        return self.a
