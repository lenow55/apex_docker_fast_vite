from tortoise import fields, models


class Records(models.Model):
    id = fields.IntField(pk=True)
    blocked_acess = fields.IntField(default=0)
    age_limit = fields.IntField()
    theam_restriction = fields.IntField()

    class Meta:
        # Define the default ordering
        #  the pydantic serialiser will use this to order the results
        ordering = ["id"]
