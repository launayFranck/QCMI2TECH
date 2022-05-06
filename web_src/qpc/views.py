from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.today()
    datas = {"date": date}
    return render(request=request,
                  template_name="qpc/index.html",
                  context=datas)