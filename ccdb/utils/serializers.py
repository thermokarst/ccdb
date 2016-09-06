from rest_framework import serializers

from .models import AdminSection, AdminEntry


class AdminSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSection
        fields = ('id', 'name', 'sort')


class AdminEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminEntry
        fields = ('id', 'admin_url', 'package', 'model', 'section', 'sort')

    admin_url = serializers.SerializerMethodField()

    def get_admin_url(self, obj):
        return obj.admin_url(self.context.get('request'))
