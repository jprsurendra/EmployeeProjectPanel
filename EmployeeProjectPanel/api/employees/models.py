from django.db import models



class Employee(models.Model):
    employee_id  = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    desgination = models.CharField(max_length=100)
    supervisor = models.ForeignKey('Employee', null=True, blank=True)
    class Meta:
        db_table = 'tbl_employee'

    def __unicode__(self):
        return '%s (%s)' % (self.full_name, self.employee_id)