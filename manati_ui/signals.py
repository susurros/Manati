from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
from manati_ui.models import *


@receiver(pre_save, sender=Weblog)
def check_id(sender, **kwargs):
    instance = kwargs.get('instance')
    if len(instance.id.split(':')) <= 1:
        instance.id = str(instance.analysis_session_id)+":"+str(instance.id)


@receiver(post_save, sender=Weblog)
def create_ioc(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        instance.create_IOCs()


@receiver(pre_delete, sender=Weblog)
def pre_delete_story(sender, instance, **kwargs):
    instance.ioc_set.clear()
