from random import choices

from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db.models import RESTRICT, ImageField, ForeignKey, CharField, EmailField, TextChoices, SlugField, Model, \
    ManyToManyField, DateTimeField, IntegerField, DateField
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField


class User(AbstractUser):
    class Gender(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        PENDING = 'pending', '------'


    email = EmailField(unique=True, blank=True)
    photo = ResizedImageField(size=[250, 250],crop=['middle', 'center'],upload_to='users', default='default.png')
    bio = CharField(max_length=70)
    gender = CharField(max_length=10, choices=Gender.choices, default=Gender.PENDING)
    phone_number = CharField(max_length=25, default='Mavjud emas', null=True)

    class Meta:
        verbose_name_plural = 'Foydalanuvchilar'
        verbose_name = 'Foydalanuvchi'


class Category(Model):
    name = CharField(max_length=100)
    image = ResizedImageField(size=[330, 85], crop=['middle', 'center'], upload_to='category')

    def sh_image(self):
        return mark_safe('<img style="border-radius: 10px" src="{}" height="70">'.format(self.image.url))

    sh_image.short_description = 'Image'
    sh_image.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Kategoriyalar'
        verbose_name = 'Kategoriya'


class Post(Model):
    class Status(TextChoices):
        PENDING = 'pending', 'Kutilmoqda'
        ACTIVE = 'active', 'Faol'
        CANCEL = 'cancel', 'Rad etilgan'

    category = ManyToManyField(Category)
    title = CharField(max_length=100)
    body = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    user = ForeignKey(User, on_delete=RESTRICT)
    is_publish = CharField(max_length=25, choices=Status.choices, default=Status.PENDING)
    image = ImageField(upload_to='post/%m')
    views_count = IntegerField(default=0)
    slug = SlugField(max_length=100, unique=True)

    def status_buttons(self):
        if self.is_publish == self.Status.PENDING:
            return format_html(
                f'<a style="padding: 5px;margin: 3px;" class="button" href="confirm/{self.pk}">Confirm</a>'
                f'<a style="padding: 5px;margin: 3px;" class="button" href="cancel/{self.pk}">Cancel</a>'
            )
        elif self.is_publish == self.Status.ACTIVE:
            return format_html(f'<a style="padding: 5px;margin: 3px;" class="button" href="cancel/{self.pk}">Cancel</a>')
        elif self.is_publish == self.Status.CANCEL:
            return format_html(
                f'<a style="padding: 5px;margin: 3px;" class="button" href="confirm/{self.pk}">Confirm</a>')
        else:
            return format_html('')

    def __str__(self):
        return str(self.id) + '. ' + self.title
    class Meta:
        verbose_name_plural = 'Postlar'


class Comment(Model):
    post = ForeignKey(Post, on_delete=RESTRICT)
    user = ForeignKey(User, on_delete=RESTRICT)
    text = CharField(max_length=1024)
    created_at = DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Izohlar'
        verbose_name = 'Izoh'


class About(Model):
    address = CharField(max_length=255)
    phone_number = CharField(max_length=255)
    email = EmailField(max_length=255)

    class Meta:
        verbose_name_plural = 'Ma\'lumot'
        verbose_name = 'Ma\'lumot'

