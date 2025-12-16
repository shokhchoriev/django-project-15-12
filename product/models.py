from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE,blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        print("salom")
        super().save(*args, **kwargs)