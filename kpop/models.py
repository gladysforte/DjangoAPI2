from django.db import models

# Create your models here.


class GroupCat(models.Model):
    group_category = models.CharField(max_length=100)

    def __str__(self):
        return self.group_category


class KpopGroups(models.Model):
    group_name = models.CharField(max_length=150)
    year_established = models.PositiveIntegerField()
    origin = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    alias = models.CharField(max_length=10)
    group_category = models.ForeignKey(GroupCat, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class Members(models.Model):
    fullname = models.CharField(max_length=100)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20)
    birthplace = models.CharField(max_length=50)
    group_name = models.ForeignKey(KpopGroups, on_delete=models.CASCADE)


class Songs(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    group_name = models.ForeignKey(KpopGroups, on_delete=models.CASCADE)

# class Role(models.Model):
#     role = models.CharField(max_length=100)

#     def __str__(self):
#         return self.role  #to result the actual data