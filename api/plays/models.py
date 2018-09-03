from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

GENRE_CHOICES = (
    ('T', 'Tragedy'),
    ('C', 'Comedy'),
    ('H', 'History')
)

class RelationshipType(models.Model):
    relation = models.CharField(max_length=200)
    masculine = models.CharField(max_length=200, null=True, blank=True)
    feminine = models.CharField(max_length=200, null=True, blank=True)
    counterpart = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.relation
    def save(self, *args, **kwargs):
        if not self.masculine:
            self.masculine = self.relation
        if not self.feminine:
           self.feminine = self.relation
        # if self.counterpart:
            # self.counterpart.counterpart = self
        super(RelationshipType, self).save(*args, **kwargs)

TITLE_CHOICES = (
    ('KI', 'King'),
    ('QU', 'Queen'),
    ('DU', 'Duke'),
    ('CO', 'Count'),
)

class Play(models.Model):
    name = models.CharField(max_length=200)
    year_published = models.IntegerField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=200)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES, null=True, blank=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Act(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    number = models.IntegerField()
    def __str__(self):
        return "Act " + str(self.number)

class Scene(models.Model):
    setting_text = models.TextField(blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    number = models.IntegerField()
    def __str__(self):
        return "Act " + str(self.act.number) + ", Scene " + str(self.number)

class Line(models.Model):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    line_text = models.TextField()
    stage_direction = models.TextField()
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_index = models.IntegerField()
    def __str__(self):
        return self.scene.act.play.name + ", Index: ", + self.play_index

class CharacterRelationship(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character')
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    of_character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='of_character')

    class Meta:
        unique_together = ('character', 'of_character',)

    def save(self, create_related=True, *args, **kwargs):
        if create_related:
            result = super(CharacterRelationship, self).save(*args, **kwargs)
            try:
                # find existing, update relationship_type
                counterpart = CharacterRelationship.objects.get(character=self.of_character, of_character=self.character)
                counterpart.relationship_type = self.relationship_type.counterpart
            except:
                # create new
                counterpart = CharacterRelationship(character=self.of_character, relationship_type=self.relationship_type.counterpart, of_character=self.character)
            counterpart.save(create_related=False)
        else:
            result = super(CharacterRelationship, self).save(*args, **kwargs)
        return result
