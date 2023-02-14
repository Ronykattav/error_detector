from django.shortcuts import render
from .forms import UploadForm
# Create your views here.
from .models import UserInput


def save_info(request):
    if request.method == 'POST':
        user_input = UploadForm(request.POST)
        if user_input.is_valid():
            msg = calc_response(request.POST)
            temp = request.POST.get
            final_input = UserInput(userId=temp.get('userId'), problem=temp.get('problem'),
                                    serialNum=temp.get('serialNum'), onLights=temp.get('onLights'),
                                    offLights=temp.get('offLights'), blinkingLights=temp.get('blinkingLights'), msg=msg)
            final_input.save()
            return render(request, 'detector/msgInfo.html', {'msg': msg})
    else:
        user_input = UploadForm
    return render(request, 'detector/mainform.html', {'user_input': user_input})


def calc_response(user_input):
    serial_num = user_input.get('serialNum')
    on_lights = user_input.get('onLights')
    off_lights = user_input.get('offLights')
    blinking_lights = user_input.get('blinkingLights')
    serial_start = serial_num[:4]

    if serial_num.isdigit():
        return "Bad serial number"
    elif serial_start == '24-x':
        return "please upgrade your device"
    elif serial_start == '36-x':
        if int(off_lights) == 3:
            return "turn on the device"
        elif int(blinking_lights) >= 2:
            return "Please wait"
        elif int(on_lights) == 3:
            return "ALL is ok"
        else:
            return "Unknown issue"
    elif serial_start == '51-b':
        if int(off_lights) == 3:
            return "turn on your device"
        elif int(blinking_lights) >= 1:
            return "Please wait"
        elif int(on_lights) > 1:
            return "ALL is ok"
        else:
            return "Unknown issue"
    else:
        return "Unknown issue"



