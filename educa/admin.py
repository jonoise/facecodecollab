from django.contrib import admin
from .models import Subject, Course, Section, Lesson

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    search_fields = ('collaborator', 'title')
    raw_fields = ('collaborator',)
    ordering = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    paginator = 10

class CourseAdmin(admin.ModelAdmin):
    list_display = ('collaborator','subject', 'title', 'language', 'framework')
    list_filter = ('title', 'created')
    search_fields = ('collaborator', 'title')
    raw_fields = ('collaborator',)
    ordering = ('-created', )
    prepopulated_fields = {'slug': ('title',)}
    paginator = 10

class SectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'title',)
    list_filter = ('title', 'course')
    search_fields = ('course', 'title')
    raw_fields = ('course',)
    ordering = ('course', )
    prepopulated_fields = {'slug': ('title',)}
    paginator = 10

class LessonAdmin(admin.ModelAdmin):
    list_display = ('section', 'section.course', 'title',)
    list_filter = ('title', 'section')
    search_fields = ('collaborator', 'title')
    raw_fields = ('collaborator',)
    ordering = ('section', 'section.course')
    prepopulated_fields = {'slug': ('title',)}
    paginator = 10



admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lesson, LessonAdmin)
