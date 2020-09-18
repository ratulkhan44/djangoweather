from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    if request.method=="POST":
        zipcode=request.POST.get('zipcode')
        api_request=requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=2020-09-18&distance=25&API_KEY=3BA78D50-E7F9-457A-8AB4-29435F9021FC")

        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error..."   

        if api[0]['Category']['Name']=='Good':
            category_description="(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color='good'
        elif api[0]['Category']['Name']=='Moderate':
            category_description="(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color='moderate'
        elif api[0]['Category']['Name']=='Unhealthy for Sensitive Groups':
            category_description="(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color='usg'
        elif api[0]['Category']['Name']=='Unhealthy':
            category_description="(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color='unhealthy'
        elif api[0]['Category']['Name']=='Very Unhealthy':
            category_description="(201 to 250) Health alert: The risk of health effects is increased for everyone."
            category_color='very-unhealthy'
        elif api[0]['Category']['Name']=='Hazardous':
            category_description="(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color='hazardous'
        return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})
    else:
        api_request=requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-09-18&distance=25&API_KEY=3BA78D50-E7F9-457A-8AB4-29435F9021FC")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="Error..."   

        if api[0]['Category']['Name']=='Good':
            category_description="(0 to 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color='good'
        elif api[0]['Category']['Name']=='Moderate':
            category_description="(51 to 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color='moderate'
        elif api[0]['Category']['Name']=='Unhealthy for Sensitive Groups':
            category_description="(101 to 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color='usg'
        elif api[0]['Category']['Name']=='Unhealthy':
            category_description="(151 to 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color='unhealthy'
        elif api[0]['Category']['Name']=='Very Unhealthy':
            category_description="(201 to 250) Health alert: The risk of health effects is increased for everyone."
            category_color='very-unhealthy'
        elif api[0]['Category']['Name']=='Hazardous':
            category_description="(301 and higher) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color='hazardous'
        return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})    

def about(request):
    return render(request,'about.html',{})    
