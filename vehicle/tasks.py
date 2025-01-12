from celery import shared_task

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    instance = None
    if model == "Car":
        instance = Car.objects.filter(pk=pk).first()
    elif model == "Moto":
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = None
        for m in instance.milage.all():
            if prev_milage is None:
                prev_milage = m.milage
            elif prev_milage < m.milage:
                print("Неверный пробег")
                break
            prev_milage = m.milage
    else:
        print(f"Экземпляр с pk={pk} не найден для модели {model}.")


def check_filter():

    filter_amount = {"amount__lte": 500}
    if Car.objects.filter(**filter_amount).exists():
        print("Отчет по фильтру")
