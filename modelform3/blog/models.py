# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Instagram(models.Model):
	nama_depan = models.CharField(max_length=50)
	nama_belakang = models.CharField(max_length=100)
	username = models.CharField(max_length=100)

	def __str__(self):
		return "{}. {}".format(self.id, self.username)
