from django.db import models
from django.utils.encoding import smart_unicode


class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    date_birth = models.DateField(null=False, blank=False)
    genre = models.CharField(max_length=2, null=True, blank=True)
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
        return smart_unicode(self.title)


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


class BookMedia(models.Model):

    def image_path(self, filename):
        path = 'books/%s/%s' % (self.book.title.replace(" ", "-"), str(filename))
        return path

    book = models.ForeignKey(Book)
    media_type = models.CharField(max_length=200,
                                  null=False, blank=False, default='img')
    url = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=image_path)
    name = models.CharField(max_length=200, null=False, blank=False)
    order = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    main = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True,
                                        auto_now_add=False, auto_now=False)
