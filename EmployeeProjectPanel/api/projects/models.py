from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'tbl_project'

    def __unicode__(self):
        return 'Project-(%s)' % (self.name)