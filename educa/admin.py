from django.contrib import admin
from .models import Subject, Course, Section, Lesson

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    search_fields = ('title',)
    ordering = ('title', )
    prepopulated_fields = {'slug': ('title',)}


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'collaborator','subject', 'language', 'framework')
    list_filter = ('title', 'created')
    search_fields = ('collaborator__username', 'framework__name', 'language__name')
    raw_id_fields = ('collaborator', 'framework', 'language', 'subject')
    ordering = ('-created', )
    prepopulated_fields = {'slug': ('title',)}

class SectionAdmin(admin.ModelAdmin):
    list_display = ('course', 'title',)
    list_filter = ('title', 'course')
    search_fields = ('course__title', 'title')
    raw_id_fields = ('course',)
    ordering = ('course', )
    prepopulated_fields = {'slug': ('title',)}

class LessonAdmin(admin.ModelAdmin):
    list_display = ('section', 'section', 'title',)
    list_filter = ('title', 'section')
    search_fields = ('section__section__title',)
    raw_id_fields = ('section',)
    ordering = ('section',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lesson, LessonAdmin)
