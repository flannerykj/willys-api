from django.contrib import admin
from .models import *
from nested_admin import NestedStackedInline, NestedModelAdmin

class LineInline(NestedStackedInline):
    model = Line
    extra = 1
    fk_name = 'scene'

class SceneInline(NestedStackedInline):
    model = Scene
    extra = 1
    fk_name = 'act'
    inlines = [LineInline]

class ActInline(NestedStackedInline):
    model = Act
    extra = 1
    fk_name = 'play'
    inlines = [SceneInline]

class PlayAdmin(NestedModelAdmin):
    model = Play
    inlines = [ActInline]

admin.site.register(Play, PlayAdmin)

class RelationshipTypeAdmin(NestedModelAdmin):
    model = RelationshipType

admin.site.register(RelationshipType, RelationshipTypeAdmin)

class CharacterRelationship(NestedStackedInline):
    model = CharacterRelationship
    extra = 1
    fk_name = 'character'

class CharacterAdmin(NestedModelAdmin):
    model = Character
    inlines = [CharacterRelationship]

admin.site.register(Character, CharacterAdmin)
