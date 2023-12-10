from django.contrib import admin
from apps.projects.models import Projects, ProjectsPhoto, Gallery, Partners, InisiativMiniProjects


class ProductImageInline(admin.TabularInline):
    model = ProjectsPhoto
    extra = 3


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ('title',)}
    save_on_top = True


class InisiativMiniProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}
    save_on_top = True


class ProjectsPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'image_tag']
    list_display_links = ('id', 'project', 'image_tag')
    list_filter = ['project', ]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag']
    list_display_links = ('id', 'image_tag')


class PartnersAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Partners, PartnersAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(InisiativMiniProjects, InisiativMiniProjectsAdmin)
admin.site.register(ProjectsPhoto, ProjectsPhotoAdmin)