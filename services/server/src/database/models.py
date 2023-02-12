from tortoise import fields, models
from enum import IntEnum, unique

@unique
class Acess(IntEnum):
    ALLOW = 0
    DENY = 1

@unique
class AgeLimit(IntEnum):
    NULL = 0
    SIX = 1
    TWELVE = 2
    SIXTEEN = 3
    XXX = 4

@unique
class TheamRestriction(IntEnum):
    BUSINESS = 0
    MALICIOUS_SITE = 1
    FOR_CHILD = 2
    FILE_DOWNLOAD = 3
    HEALTH = 4
    GAME_ENTERTAINMENT = 5
    CULTURE = 6
    MULTIMEDIA = 7
    SCIENCE_AND_TECHNOLOGY = 8
    PROFANITY = 9
    NEWS_AND_MEDIA = 10
    EDUCATION = 11
    SOCIETY_AND_POLITICS = 12
    SEARCH_ENGINES = 13
    USER_CONTENT = 14
    PROXIES_AND_ANONYMIZERS = 15
    ILLEGAL_WEBSITES = 16
    ADVERTISING_AND_MARKETING = 17
    SOCIAL_NETWORKS = 18
    SPORTS_AND_HOBBIES = 19
    BACKGROUND_INFORMATION  = 20
    NON_THEAM = 21

@unique
class ColumnsId(IntEnum):
    BLOCKED_ACESS = 0
    AGE_LIMIT = 1
    THEAM_RESTRICTION = 2


class Records(models.Model):
    id = fields.IntField(pk=True)
    blocked_acess = fields.IntEnumField(Acess, default=0)
    age_limit = fields.IntEnumField(AgeLimit, default=0)
    theam_restriction = fields.IntEnumField(TheamRestriction, default=21)

    class Meta:
        # Define the default ordering
        #  the pydantic serialiser will use this to order the results
        ordering = ["id"]
