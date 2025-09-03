from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "location", "amount", "renewal_at", "next_renewal_at", "createdby")
    search_fields = ("location", "createdby", "renewalby")
    list_filter = ("renewal_at", "next_renewal_at")
