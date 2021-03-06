from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE


class Event(SafeDeleteModel):
    """Event Model

    Description: Stores a single event

    If an Event is deleted it is just masked so that it can still be accessed from the QuizTaker Model.

    Fields
    - name = `CharField`
    - active =  `BooleanField`
    - date = `DateField(auto_now=False, auto_now_add=False)`
    """
    # Added this because the important quiz_taker model uses
    _safedelete_policy = HARD_DELETE_NOCASCADE

    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    child_mode = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ["active"]
        verbose_name_plural = "events"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
