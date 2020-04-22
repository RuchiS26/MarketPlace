from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'defaults/avatar.png', upload_to = "profile_pics/")
	contact  = models.CharField(max_length = 13)

	def __str__(self):
		return str(self.user)

