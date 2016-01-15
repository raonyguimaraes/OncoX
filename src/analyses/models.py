from __future__ import unicode_literals
from authtools.models import User
from django.core.urlresolvers import reverse


from django.db import models

from files.models import File
# Create your models here.
class Analysis(models.Model):
    analysis_types = (
        ('xhmm', 'XHMM'),
        ('oncotator', 'Oncotator'),
        ('mendelmd', 'Mendel,MD'),
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    
    # user = models.ForeignKey(User, null=True)

    
    files = models.ManyToManyField(File,null=True, blank=True)
    type = models.CharField(max_length=50, choices=analysis_types, null=True, blank=True, default='xhmm')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('analysis-detail', kwargs={'pk': self.pk})
    