from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.functional import lazy
from django.utils.translation import gettext, gettext_lazy as _

gettext_lazy = lazy(gettext, str)

from .models import Person, Address, Status, Course, Performance, CoursePerformance

admin.site.register(Address)
admin.site.register(Status)
admin.site.register(Course)
admin.site.register(Performance)
admin.site.register(CoursePerformance)


class CourseInlineAdmin(admin.TabularInline):
    model = Person.courses.through


@admin.register(Person)
class AdvNewUserAdmin(UserAdmin):
    save_on_top = True
    filter_horizontal = ('groups', 'user_permissions', 'status')
    inlines = [CourseInlineAdmin]
    # 'status', 'courses'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone',
                                         'address', 'avatar', 'status')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
