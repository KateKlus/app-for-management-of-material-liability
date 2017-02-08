from django.shortcuts import get_object_or_404, render


def index(request):
    template_name = 'knastu/index.html'

    return render(request, template_name)






