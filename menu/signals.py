from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from menu.models import Menu


@receiver(post_save, sender=Menu)
def menu_create(sender, instance, **kwargs):
    """
    Этот сигнал срабатывает после создания меню.
    """
    if instance.group and instance.group != 'null':
        menus = Menu.objects.filter(group=instance.group)
        menu_count = menus.count()
        if menu_count > 1:
            menus.update(has_category=True)

        elif menu_count == 1:
            menus.update(has_category=False)


@receiver(pre_save, sender=Menu)
def menu_update(sender, instance, **kwargs):
    """
    Этот сигнал также срабатывает перед обновлением или созданием меню.
    instance.id недоступен, пока не будет создано меню
    """
    if instance.id:
        instance_old_group = Menu.objects.get(id=instance.id).group
        menus = Menu.objects.filter(group=instance_old_group).exclude(id=instance.id)
        if menus.count() == 1:
            menus.update(has_category=False)


@receiver(pre_delete, sender=Menu)
def menu_delete(sender, instance, **kwargs):
    """
    Этот сигнал выполняется перед удалением меню.
    """
    menus = Menu.objects.filter(group=instance.group).exclude(id=instance.id)
    if menus.count() == 1:
        menus.update(has_category=False)
