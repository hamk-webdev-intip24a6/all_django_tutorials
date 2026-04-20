from django.contrib import admin
from django.db.models import Avg
from .models import Topic, Feedback


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'avg_rating')
    search_fields = ['name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(average_rating=Avg('feedback__rating'))

    def avg_rating(self, obj):
        avg = getattr(obj, 'average_rating', None)
        if avg is None:
            return '-'
        return f"{avg:.2f}"
    avg_rating.short_description = 'Avg rating'
    avg_rating.admin_order_field = 'average_rating'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('topic', 'rating', 'good', 'bad', 'date')
    list_filter = ['topic', 'date']
    search_fields = ['good', 'bad']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Feedback, FeedbackAdmin)
