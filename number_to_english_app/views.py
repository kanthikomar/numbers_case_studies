from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

INVALID_JSON_FORMAT = "Invalid JSON format"
INVALID_NUMBER_FORMAT = "Invalid number format"
INVALID_REQUEST_METHOD = "Invalid request method"
INVALID_NUMBER_RANGE = "Number out of range"

@csrf_exempt
def num_to_english(request):
    # Define the function outside to load configuration only once
    def load_config():
        with open('config.json') as config_file:
            return json.load(config_file)

    def convert_under_20(num, config):
        return config['units'][num]

    def convert_tens(num, config):
        return config['tens'][num // 10] + " " + convert_under_20(num % 10, config) if num % 10 else config['tens'][num // 10]

    def convert(num, config):
        if num < 20:
            return convert_under_20(num, config)
        elif num < 100:
            return convert_tens(num, config)
        elif num < 1000:
            suffix = ""
            if num % 100:
                suffix = " " + convert(num % 100, config)
            return convert(num // 100, config) + " " + config['hundred'] + suffix
        else:
            for i, magnitude in enumerate(config['magnitudes']):
                if num < 1000 ** (i + 1):
                    suffix = ""
                    if num % 1000 ** i:
                        suffix = " " + convert(num % 1000 ** i, config)
                    return convert(num // 1000 ** i, config) + " " + magnitude + suffix

    def convert_decimal(decimal_part, config):
        result = ""
        for digit in decimal_part:
            result += " " + config['units'][int(digit)]
        return result.strip()

    def convert_to_english(decimal_number, config):
        whole_number = int(float(decimal_number))
        whole_number_text = convert(abs(whole_number), config)
        decimal_text = config['units'][0]
        if '.' in decimal_number: 
            decimal_text = convert_decimal(decimal_number.split(".")[1], config)  # Remove "0." from decimal

        result = whole_number_text
        if decimal_text != config['units'][0]:
            result += " point " + decimal_text

        if whole_number < 0:
            result = "Minus " + result

        return result.capitalize()

    if request.method == 'GET':
        number = request.GET.get('number')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            number = data.get('number')
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": INVALID_JSON_FORMAT})
    else:
        return JsonResponse({"status": "error", "message": INVALID_REQUEST_METHOD})

    if number is None:
        return JsonResponse({"status": "error", "message": INVALID_NUMBER_FORMAT})
    
    try:
        config = load_config()
        if float(number) > config['max_number'] or float(number) < config['min_number']:
            return JsonResponse({"status": "error", "message": INVALID_NUMBER_RANGE + ", valid range is (" + str(config['min_number']) + "," + str(config['max_number']) + ")"})   
        english_text = convert_to_english(number, config)
        return JsonResponse({"status": "ok", "num_in_english": english_text})
    except ValueError:
        return JsonResponse({"status": "error", "message": INVALID_NUMBER_FORMAT})
