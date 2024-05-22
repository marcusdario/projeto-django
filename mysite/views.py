from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Agora é %s. Qualquer coisa que eu escrever.</body></html>" % now
    return HttpResponse(html)

def lorna_list(request):
    html = f"<html><body> Cliqui para ver musicas </body></html>"
    return HttpResponse(html)