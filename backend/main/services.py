import os.path

from main.models import MainModel


def get_or_create_short_url(url, front):
    last_url = MainModel.objects.all().last()
    last_id = last_url.id if last_url else 0
    hexed_id = hex(last_id + 1)[2:]
    obj, _ = MainModel.objects.get_or_create(base=url, defaults={'short': hexed_id})
    return os.path.join(front, obj.short)


def get_url_for_redirect(hexadecimal):
    data = MainModel.objects.filter(short=hexadecimal).first()
    if data:
        data.clicks += 1
        data.save()
        return data.base


def get_top_urls(length):
    top = MainModel.objects.order_by('-clicks')[:int(length)]
    return [{'id': i.id, 'base': i.base, 'clicks': i.clicks} for i in top]
