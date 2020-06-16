from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    # return render(request, 'index.html',params)
    return render(request, 'index2.html')


def func1(request):
    # return HttpResponse("Dial #9028219403")
    data = request.POST.get('content', 'default')
    rmv_pnc = request.POST.get('rmv_pnc', 'off')
    cnv_upcs = request.POST.get('cnv_upcs', 'off')
    rmv_spc = request.POST.get('rmv_spc', 'off')
    cnt_chr=request.POST.get('cnt_chr','off')

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    param={'raw':data}

    if rmv_pnc=='on':
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char
        data=analyzed

    if cnv_upcs=='on':
        data=data.upper()

    if rmv_spc=='on':
        analyzed=""
        data=data.replace("  ","")
        
    if cnt_chr=='on':
        length=len(data)
        param.update(cnt_line="The length of i/p string is : "+str(length)+" characters.")

    param.update(value=data)
    print(param)
    return render(request, 'anlyzer.html', param)
