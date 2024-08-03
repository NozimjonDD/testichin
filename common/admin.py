from django.contrib import admin

from common.models import Region, District, SubDistrict, InteractiveService, InnovationIdea, SpellingMistake, FileStore

admin.site.register(Region)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(InteractiveService)
admin.site.register(InnovationIdea)
admin.site.register(SpellingMistake)
admin.site.register(FileStore)
