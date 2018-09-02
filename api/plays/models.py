from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

GENRE_CHOICES = (
    ('T', 'Tragedy'),
    ('C', 'Comedy'),
    ('H', 'History')
)
RELATIONSHIP_TYPES = (
    ('FA', 'Father'),
    ('MO', 'Mother'),
    ('BR', 'Brother'),
    ('SI', 'Sister'),
    ('FR', 'Friend'),
    ('SO', 'Son'),
    ('DA', 'Daughter'),
    ('MA', 'Master'),
    ('SE', 'Servant'),
    ('EN', 'Enemy'),
    ('CO', 'Cousin'),
    ('NI', 'Niece'),
    ('NE', 'Nephew'),
    ('AU', 'Aunt'),
    ('UN', 'Uncle')
)

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
        return self.play.name + ", Act " + self.number

class Scene(models.Model):
    setting_text = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    number = models.IntegerField()
    def __str__(self):
        return self.act.play.name + ", Act " + self.play.act + ", Scene " + self.number

class Line(models.Model):
    play_index = models.IntegerField()
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    line_text = models.TextField()
    stage_direction = models.TextField()
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_index = models.IntegerField()
    def __str__(self):
        return self.scene.act.play.name + ", Index: ", + self.play_index

class CharacterRelationship(models.Model):
    subject_charater = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='subject_character')
    relationship_type = models.CharField(max_length=2, choices=RELATIONSHIP_TYPES)
    object_character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='object_character')
