from tortoise import fields, models


class Records(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=True)
    val_1 = fields.BooleanField(default=False)
    val_2 = fields.BooleanField(default=False)
    val_3 = fields.BooleanField(default=False)
    val_4 = fields.BooleanField(default=False)
    val_5 = fields.BooleanField(default=False)


#class Notes(models.Model):
#    id = fields.IntField(pk=True)
#    title = fields.CharField(max_length=225)
#    content = fields.TextField()
#    author = fields.ForeignKeyField("models.Users", related_name="note")
#    created_at = fields.DatetimeField(auto_now_add=True)
#    modified_at = fields.DatetimeField(auto_now=True)
#
#    def __str__(self):
#        return f"{self.title}, {self.author_id} on {self.created_at}"
