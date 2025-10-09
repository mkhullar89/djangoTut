from django.contrib import admin
from .models import Chaivariety,ChaiReview,Store,ChaiCertificate
# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','choices','date')
    # search_fields=('name','choices')
    # list_filter=('choices','date')
    inlines=[ChaiReviewInline]
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_variety',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')
admin.site.register(Chaivariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
# admin.site.register(ChaiReview)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)