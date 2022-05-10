from django.db import models
import uuid


type_choices = (
    ("BUG", "BUG"), 
    ("IDEA", "IDEA"),
    ("OTHER", "OTHER"),
)

class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=5, choices=type_choices)
    comment = models.TextField()
    screenshot = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "feedbacks"
