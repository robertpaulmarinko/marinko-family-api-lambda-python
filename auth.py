import json

class LoginResponse:
    success = False
    token = ""

def attempt_login(request):
    print("attemp_login: " + request)
    requestJson = json.loads(request);
    response = LoginResponse()
    if requestJson.get("password") == "password":
        response.success = True
        response.token = "123"
    else:
        response.success = False
        response.token = ""
    
    return json.dumps(response.__dict__)
