from django.db import models

# Create your models here.

# NULLABLE FIELDS ARE ATTRS WITH NO RELEVANT USE (FOR NOW) MIGHT AS WELL DEFAULT TO 0 OR "0"
# FOR FUTURE USAGE

default_string_value = "N/A"

class Title(models.Model):
    
    # japanese title
    japanese = models.CharField(default=default_string_value ,max_length=100)
    
    # compact version of english title
    pretty = models.CharField(default=default_string_value,max_length=100)

    # eng ver
    english = models.CharField(default=default_string_value,max_length=100)

    # consider puting this field if willing to sacrifice DB space for simplicity.
    # if commented : serializer must include Book ID so API calls on this backend
    #                could show the related book when given a title
    # if uncommented: no need to do the above since Foreign Key is part of the model.
    
    #book_id = models.OneToOneField(Book, on_delete=models.CASCADE)

# model for avoiding redundancy on tag_type
class Tag_Type(models.Model):
    tag_name = models.CharField(primary_key=True, unique=True,max_length=100)

class Tag(models.Model):
    
    # tag url usually of form /<type>/<name>/
    url = models.CharField(default=default_string_value,max_length=100)

    # number of books with this tag on
    count = models.IntegerField(default=0)

    # if tag type remove, remove tag
    tag_type = models.OneToOneField(Tag_Type, on_delete=models.CASCADE)

    tag_id = models.IntegerField(unique=True, primary_key=True)

    name = models.CharField(default=default_string_value,max_length=100)

class Book(models.Model):
    
    # nhentai api returns upload date as integer for some reason. Might as well keep it unchanged
    upload_date = models.IntegerField(null=True,blank=True,default=0)
    
    # book id or simply "id" field from the api response. couldnt be id due to django convention
    book_id = models.IntegerField(primary_key=True, unique=True)
    
    # used for querying jpg images
    media_id = models.CharField(null=True,blank=True,default="0",max_length=100)

    # number of favorites
    num_favorites = models.IntegerField(null=True, blank=True, default=0)

    num_pages = models.IntegerField(default=0)

    # make this foreign key to a scantalator model (pay respects to the TLs man T_T)
    scanlator = models.CharField(null=True,blank=True,default="N/A",max_length=100)
    
    # not including this for now, since api just returns the image dimensions
    # images
    
    # MANY TAGS
    tags = models.ManyToManyField(Tag)

    # OneToOnefield for title model
    title = models.OneToOneField(Title, null=True, on_delete=models.SET_NULL)




