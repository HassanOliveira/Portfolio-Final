from django.contrib import admin

from base.models import Projects, Category, TimelineItem, CV
class ListingProjects(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle", "published")
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("published",)
    list_per_page = 10

admin.site.register(Projects, ListingProjects)
admin.site.register(Category)
admin.site.register(TimelineItem)
admin.site.register(CV)
