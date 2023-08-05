from django.db import models

STATUS_CHOICES=(
    ('todo','to do'),
    ('doing','Doing'),
    ('done','DONE')
)


class Task (models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    status = models.CharField(max_length=30,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
