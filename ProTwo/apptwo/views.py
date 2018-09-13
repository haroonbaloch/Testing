from django.shortcuts import render

def index(jellybelly):
    faltu = {"temptag": "its my choice"}
    return render(jellybelly,"html/index.html",context=faltu)
