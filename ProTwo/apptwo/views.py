from django.shortcuts import render
from apptwo.models import User

def index(jellybelly):
    altu = User.objects.order_by('f_name')
    faltu = {'temptag': altu}
    return render(jellybelly,"html/index.html",context=faltu)


#def index(rocky):
#    webpage_list = AccessRecord.objects.order_by('date')
#    date_dict = {'access_record':webpage_list}
#    return render(rocky,'html/index.html',context=date_dict)
