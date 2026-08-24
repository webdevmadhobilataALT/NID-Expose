from django.contrib import admin

# Register your models here.


from django.contrib import admin


from .models import NIDCheck


@admin.register(NIDCheck)
class NIDCheckAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nid_number",
        "visitor_ip",
        "created_at",
    )

    search_fields = (
        "nid_number",
        "visitor_ip",
    )

    list_filter = (
        "created_at",
    )

    readonly_fields = (
        "id",
        "created_at",
    )


