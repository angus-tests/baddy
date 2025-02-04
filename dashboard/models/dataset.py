from django.db import models


class Dataset(models.Model):
    """
    A model to store information about a dataset.
    """
    dataset_id = models.CharField(max_length=255, unique=True)
    filename = models.CharField(max_length=255)
    period = models.DateField()
    survey_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dataset_id
