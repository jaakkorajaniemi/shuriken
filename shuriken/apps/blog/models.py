from django.db import models

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published at', null=False)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Modified at', null=False)
    accessed = models.IntegerField(default=0, null=False)
    title = models.CharField(default='', max_length=256, null=False)
    content = models.TextField(default='', null=False)
    slug = models.CharField(default='', max_length=128, null=False)

    # Short description of the post (not always displayed, depending on the case)
    description = models.TextField(default='', null=False)

    # Language in 2-character standard country code
    language = models.CharField(max_length=2, default='en', null=False)

    # Visible to the public (the link is not visible, but content is accessible)
    visible = models.BooleanField(default=True, null=False)

    # Disabled from public access (the link might be visible, but content is inaccessible)
    disabled = models.BooleanField(default=True, null=False)

    # Static page (author/timestamp hidden) or blog post (author/timestamp visible)
    static = models.BooleanField(default=False, null=False)

    # Extended=True objects are hidden, and intended to be extended by other apps.
    extended = models.BooleanField(default=False, null=False)

    # Generate PDF
    def convert(self):
        pass

    def __str__(self):
        return self.title

class File(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published at', null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modified at', null=False)
    accessed_at = models.DateTimeField(auto_now=True, verbose_name='Accessed at', null=False)
    accessed = models.IntegerField(default=0, null=False)
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=False)

    # File size in bytes
    filesize = models.IntegerField(default=0, null=False)

    # Directories are defined as File objects whose filetype is Null
    filetype = models.CharField(max_length=4, null=True)

    # Local file identifier in the filesystem
    identifier = models.CharField(max_length=32, null=False)

    # Parent directory (File object with filetype=Null) in the filesystem
    location = models.ForeignKey('File', on_delete=models.CASCADE, null=True, default=None)

    # Password protected files cannot be accessed without password
    password = models.CharField(max_length=128, null=True)

    # Encrypted files cannot be opened unless decrypted at download time
    encrypted = models.BooleanField(default=False, null=False)

    # Extended=True objects are hidden, and intended to be extended by other apps.
    extended = models.BooleanField(default=False, null=False)
