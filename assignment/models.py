from django.db import models

class Entry(models.Model):
	url = models.URLField(max_length=300)
	status = models.BooleanField(default=False)
	def __unicode__(self):
		return self.url
