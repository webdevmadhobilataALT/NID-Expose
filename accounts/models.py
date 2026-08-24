from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    """
    class for the customized
    user model
    """


    # specify the visitor IP address and NID card Number fields
    nid_number = models.CharField(max_length=20)
    visitor_ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """
        additional method to
        return the class object
        in a human readable format
        """

        # return the visitor IP
        return self.visitor_ip




    