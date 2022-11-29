import os.path

from main.models import MainModel


def get_or_create_short_url(url, front):
    obj, _ = MainModel.objects.get_or_create(base=url)
    hex_id = hex(obj.id)[2:]
    return os.path.join(front, hex_id)


def get_url_for_redirect(hexadecimal):
    data = MainModel.objects.filter(id=int(hexadecimal, 16)).first()
    if data:
        data.clicks += 1
        data.save()
        return data.base


def get_top_urls(length):
    top = MainModel.objects.order_by('-clicks')[:int(length)]
    return [{'id': i.id, 'base': i.base, 'clicks': i.clicks} for i in top]
