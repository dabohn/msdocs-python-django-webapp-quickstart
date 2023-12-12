from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')
    
import requests

def alpaca_sma_view(request):
    # Fetch files from the Alpaca-SMA repository
    url = "https://raw.githubusercontent.com/dbohn94/Alpaca-SMA/main/bot.py"  # Example URL
    response = requests.get(url)
    file_content = response.text

    # Process the file content as needed
    # ...

    # Render the template with the file content
    return render(request, 'alpaca_sma_page.html', {'file_content': file_content})
