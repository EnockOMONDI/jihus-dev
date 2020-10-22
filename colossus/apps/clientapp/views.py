from django.conf import settings as django_settings
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import requests
import json
from .forms import SendMessageForm



def get_acess_token(request):
    url = "https://dsvc.safaricom.com:9480/api/auth/login"

    payload = {'username' :'TISA_API', 'password' : 'TISA_API@ps7331'}
    
    headers = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    print(response.json())
    result=response.json()
    acess_token=result['token']
    print(acess_token)
    return acess_token
        
   


def send_bulk_sms(request):
    url = "https://dsvc.safaricom.com:9480/api/public/CMS/bulksms"
    access_token = get_acess_token(request)
    payload = "{\n\"timeStamp\": \"1556873649895\",\n\"dataSet\": [\n{\n\"userName\": \"tisa\",\n\"channel\": \"sms\",\n\"packageId\": \"5025\",\n\"oa\": \"JIHUSISHE\",\n\"msisdn\": \"254728826517,722877107\",\n\"message\": \"This is the bulk sms send\",\n\"uniqueId\": \"2500688298721\",\n\"actionResponseURL\": \"https://posthere.io/c59f-4786-86ac\"\n}\n]\n}"

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SendMessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = form.cleaned_data['message']
            recepients = form.cleaned_data['recepients']
         
           
        payload1={
        "timeStamp": "1556873649895",
        "dataSet": [
        {
        "userName": "tisa",
        "channel": "sms",
        "packageId": "5025",
        "oa": "jihusishe",
        "msisdn": recepients,
        "message": message,
        "uniqueId": "2500688298721",
        "actionResponseURL": "https://posthere.io/c59f-4786-86ac"
        }
        ]
        }
        headers = {
        'Content-Type': 'application/json',
        'X-Authorization': 'Bearer %s' % access_token}
        print(access_token)

        response = requests.request("POST", url, headers=headers,  data = json.dumps(payload1))
        result=response.json()
        print(result)
        # message=result["message"]
    
        return HttpResponse(message)
        
    else:
        form = SendMessageForm()

        return render(request, 'pages/sendbulk.html', 
        {
          'form': form,
          'local_css_urls' : django_settings.SB_ADMIN_CLIENT_CSS_LIBRARY_URLS,
          'local_js_urls' : django_settings.SB_ADMIN_CLIENT_JS_LIBRARY_URLS
   })


    
    
    
def send_ondemand_sms(request):
    access_token = get_acess_token(request)
    url = "https://dsvc.safaricom.com:9480/api/public/SDP/sendSMSRequest"

    payload = "{\n\"requestId\": 17,\n\"channel\": \"APIGW\",\n\"operation\": \"SendSMS\",\n\"requestParam\": {\n\"data\": [\n{\n\"name\": \"LinkId\",\n\"value\": \"\"\n},\n{\n\"name\": \"Msisdn\",\n\"value\": \"254728826517\"\n},\n{\n\"name\": \"Content\",\n\"value\": \"Thank You for Ondemand Subscription SAFRI TEST TUN Subscption test Send sms\"\n},\n{\n\"name\": \"OfferCode\",\n\"value\": \"001009700850\"\n},\n{\n\"name\": \"CpId\",\n\"value\": \"97\"\n}\n]\n}\n}"
    headers = {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Authorization': 'Bearer %s' % access_token
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
