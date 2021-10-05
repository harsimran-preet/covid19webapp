from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "33a56f1985msh9d028b4c99359dbp10252fjsncf20217a19c2",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def helloworldview(request):
    list1 = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        list1.append(response['response'][x]['country'])
        list1.sort()
    if request.method == 'POST':
        
        selectedcountry = request.POST['selectedcountry']
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry,'list1':list1,'new' : new, "active":active, 'critical':critical, 'recovered':recovered, 'deaths':deaths, 'total': total}
        return render(request,'index.html' , context)   
    noofresults = int(response['results'])
    
    for i in range(0, noofresults):
        
        list1.append(response['response'][i]['country'])
    context = {'list1':list1}
    return render(request,'index.html' , context)
