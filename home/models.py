from django.db import models

class book_table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_time = models.DateTimeField()
    num_people = (
        (1,'1 People'),
        (2,'2 People'),
        (3,'3 People'),
    )
    num_people_field = models.IntegerField(choices=num_people,default=1)
    special_req = models.TextField()

