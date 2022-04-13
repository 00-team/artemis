from django.http import HttpRequest, JsonResponse

# exception
from utils.api import E

# random
from random import choice

# decorators
from django.views.decorators.http import require_GET

# models
from Collection.models import Owner, FAQ, Asset

# utils
from utils.api import get_data
from utils.api.exception import OWNER_NOT_FOUND


@require_GET
def get_owners(request: HttpRequest):
    try:
        owners = Owner.objects.all()

        def GO(o: Owner):
            try:
                a = choice(Asset.objects.filter(owner=o))

                return {
                    'username': o.username,
                    'picture': o.picture.url,
                    'description': o.description,
                    'image': a.image.url
                }
            except:
                return {}

        owners = filter(lambda o: o, map(GO, owners))

        return JsonResponse({'owners': list(owners)})
    except E as e:
        return e.response


@require_GET
def get_owner(request: HttpRequest):
    try:
        data = get_data(request)
        username = data.get('username')

        owner = Owner.objects.get(username=username)
        assets = Asset.objects.filter(owner=owner)

        def GA(a: Asset):
            try:
                return {
                    'image': a.image.url,
                    'title': a.title,
                    'description': a.description
                }
            except:
                return {}

        response = {
            'username': owner.username,
            'picture': owner.picture.url,
            'banner': owner.banner.url,
            'wallet': owner.wallet,
            'description': owner.description,
            'floor_price': owner.floor_price,
            'ceil_price': owner.ceil_price,
            'rarible': owner.rarible,
            'twitter': owner.twitter,
            'instagram': owner.instagram,
            'assets': list(filter(lambda a: a, map(GA, assets)))
        }

        return JsonResponse(response)

    except E as e:
        return e.response

    except Owner.DoesNotExist:
        return OWNER_NOT_FOUND.response


@require_GET
def get_faqs(request: HttpRequest):
    try:
        owners = Owner.objects.all()

        def GF(faq: FAQ):
            return {
                'question': faq.question,
                'answer': faq.answer,
            }

        def GOF(o: Owner):
            faqs = FAQ.objects.filter(owner=o)
            return {'owner': o.username, 'faqs': list(map(GF, faqs))}

        return JsonResponse({'owners': list(map(GOF, owners))})

    except E as e:
        return e.response

    except Owner.DoesNotExist:
        return OWNER_NOT_FOUND.response
