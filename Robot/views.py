from django.shortcuts import render,redirect
import os
import threading
# Create your views here.

# def running():
#     print 'Coming!'
#     os.system('workon haoyidai')
#     print os.system('python')
#     os.system('exit()')
#
def satrt(request):
    return redirect('http://127.0.0.1:8000/media/Robot/qr/QR.png')
