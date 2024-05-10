from django.db import models


class Information(models.Model):
    logo = models.ImageField(upload_to="logo")
    name = models.CharField(max_length=100)
    video = models.URLField(null=True, blank=True)
    email_one = models.EmailField()
    email_two = models.EmailField()
    facebook = models.URLField()
    address = models.CharField(max_length=100)
    phone_number_one = models.CharField(max_length=20)
    phone_number_two = models.CharField(max_length=20)
    instagram = models.URLField()
    telegram = models.URLField()
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField()

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyHome(models.Model):
    title = models.CharField(max_length=50)
    position = models.ManyToManyField(Position)
    photo = models.ImageField(upload_to='my_photo')


class Services(models.Model):
    icon = models.ImageField(upload_to='services_icon')
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_img')
    name = models.CharField(max_length=75)
    service = models.CharField(max_length=75)
    banner = models.ImageField(upload_to='portfolio_banner')
    client = models.CharField(max_length=100)
    project_type = models.CharField(max_length=75)
    date = models.DateField()
    about = models.TextField()
    github_link = models.URLField(null=True, blank=True)
    figma_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    photo = models.ImageField(upload_to='about_me_img')
    title = models.CharField(max_length=100)
    bio = models.TextField()
    position = models.CharField(max_length=100)


class Biography(models.Model):
    full_name = models.CharField(max_length=75)
    age = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Skills(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Resume(models.Model):
    biography = models.ForeignKey(Biography, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    education = models.ManyToManyField(Education)


class News(models.Model):
    image = models.ImageField(upload_to='news_img')
    title = models.CharField(max_length=255)
    date = models.DateField()


class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
