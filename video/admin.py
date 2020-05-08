from django.contrib import admin
from video.models import Video
from django.contrib.admin.utils import flatten_fieldsets
from django.utils.safestring import mark_safe



# Register your models here.
@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('category',)
    list_display = ('title', 'category','action')
    list_per_page = 20
    list_max_show_all = 20

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if self.fieldsets:
                return flatten_fieldsets(self.fieldsets)
            else:
                return list(set(
                    [field.name for field in self.opts.local_fields] +
                    [field.name for field in self.opts.local_many_to_many]
                ))
        return super().get_readonly_fields(request, obj)

    def action(self,obj):
        return mark_safe('<a target="_blank" href="{url}"><img src="{gif_url}" height="100" width="200"></a>'.format(url=obj.url,gif_url=obj.gif_url))

    action.short_description = '播放'

