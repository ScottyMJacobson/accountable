from django.contrib import admin
from accounts.models import User
from commitments.models import CommitmentProfile

class CommitmentProfileInline(admin.StackedInline):
    model = CommitmentProfile

class UserAdmin(admin.ModelAdmin):
    inlines = (CommitmentProfileInline,)
    fields = ('email', 'username', 'is_active',
        'is_admin', 'is_staff')

admin.site.register(User, UserAdmin)
