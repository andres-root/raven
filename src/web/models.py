from django.db import models
from django.utils.encoding import smart_unicode


class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(default=1, null=True, blank=True)
    bio = models.TextField()
    genres = models.TextField()
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True,
                                        auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    isbn = models.CharField(max_length=220, null=True, blank=True)
    description = models.TextField()
    genres = models.TextField()
    author = models.ForeignKey(Author)
    release_date = models.DateField(null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True,
                                        auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Genre(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True,
                                        auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Comment(models.Model):
    pass


class Moment(models.Model):
    pass


class Read(models.Model):
    pass
