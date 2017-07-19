
class Demography(models.Model):

    # Enums
    GENDER_CHOICES = (
        ('0', 'Male'),
        ('1', 'Female'),
        ('2', 'Unknow'),
    )

    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    state_code = models.CharField(max_length=10, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    alternate_address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    alternate_phone = models.CharField(max_length=30, null=True, blank=True)
    race = models.CharField(max_length=30, null=True, blank=True)
    ethnicity = models.CharField(max_length=30, null=True, blank=True)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )