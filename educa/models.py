from django.db import models
from languages.models import Language, Framework
from users.models import UserModel
# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=60, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    slug = models.SlugField(max_length=60, verbose_name='slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:subject_detail', args=[
                                self.slug
                                ])


class Course(models.Model):
    collaborator = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='courses')
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name='courses', blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=60, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    slug = models.SlugField(max_length=60, verbose_name='slug')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[
                                self.slug
                                ])

class Section(models.Model):
    course = models.ForeignKey(Course, verbose_name='section', on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=60, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    slug = models.SlugField(max_length=60, verbose_name='slug')

    def __str__(self):
        return self.title

class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=60, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    video = models.URLField(verbose_name='video link')
    slug = models.SlugField(max_length=60, verbose_name='slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:subject_detail', args=[
                                self.slug
                                ])