from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from datetime import datetime 

# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User)
  name = models.CharField(max_length = 1000)
  locale = models.CharField(max_length = 1000)
  age = models.CharField(max_length = 1000)
  picture = models.CharField(max_length = 1000)
  bio = models.CharField(max_length = 1000)
  location = models.CharField(max_length = 1000)
  address = models.CharField(max_length = 1000)

class Wpost(models.Model):
  id = models.AutoField('#', primary_key=True)
  date = models.DateTimeField(default = datetime.now())
  wallpost = models.CharField(max_length = 1000)
  hascomments = models.BooleanField(default = False)
  numcomments = models.IntegerField(default = 0)
  likes = models.IntegerField(default = 0)
  user = models.ForeignKey(User)

  def for_json(self):
      return {"id": self.id, "likes": self.likes, "numcomments": self.numcomments}

  def timeremoved(self):
      return timesince(self.date).split(', ')[0]

class Ppost(models.Model):
  id = models.AutoField('#', primary_key=True)
  date = models.DateTimeField(default = datetime.now())
  profilepost = models.CharField(max_length = 1000)
  user1 = models.ForeignKey(User, related_name='user1')
  user2 = models.ForeignKey(User, related_name='user2')
  hascomments = models.BooleanField(default = False)
  numcomments = models.IntegerField(default = 0)
  clicked = models.BooleanField(default=False)
  likes = models.IntegerField(default = 0)

  def for_json(self):
      return {"id": self.id, "likes": self.likes, "numcomments": self.numcomments}

  def timeremoved(self):
      return timesince(self.date).split(', ')[0]

class Wcomment(models.Model):
  id = models.AutoField('#', primary_key=True)
  date = models.DateTimeField(default = datetime.now())
  wallcomment = models.CharField(max_length = 500)
  wall = models.ForeignKey(Wpost)
  user = models.ForeignKey(User)

  def for_json(self):
      return {"usercomment": self.user.username, "wallcomment": self.wallcomment, "date": timesince(self.date).split(', ')[0]}

class Pcomment(models.Model):
  id = models.AutoField('#', primary_key=True)
  date = models.DateTimeField(default = datetime.now())
  profilecomment = models.CharField(max_length = 500)
  profile = models.ForeignKey(Ppost)
  user = models.ForeignKey(User)

  def for_json(self):
      return {"usercomment": self.user.username, "profilecomment": self.profilecomment, "date": timesince(self.date).split(', ')[0]}

  def timeremoved(self):
      return timesince(self.date).split(', ')[0]

class Wlike(models.Model):
  id = models.AutoField('#', primary_key=True)
  wall = models.ForeignKey(Wpost)
  user = models.ForeignKey(User)
  color = models.IntegerField(default=0)

  def for_json(self):
      return {"wallid": self.wall.id, "color": self.color}

class Wdislike(models.Model):
  id = models.AutoField('#', primary_key=True)
  wall = models.ForeignKey(Wpost)
  user = models.ForeignKey(User)
  color = models.IntegerField(default=10)

  def for_json(self):
      return {"wallid": self.wall.id, "color": self.color}

class Plike(models.Model):
  id = models.AutoField('#', primary_key=True)
  profile = models.ForeignKey(Ppost)
  user = models.ForeignKey(User)
  color = models.IntegerField(default=0)

  def for_json(self):
      return {"profileid": self.profile.id, "color": self.color}

class Pdislike(models.Model):
  id = models.AutoField('#', primary_key=True)
  profile = models.ForeignKey(Ppost)
  user = models.ForeignKey(User)
  color = models.IntegerField(default=10)

  def for_json(self):
      return {"profileid": self.profile.id, "color": self.color}
