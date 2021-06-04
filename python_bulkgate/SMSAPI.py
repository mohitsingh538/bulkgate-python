import urllib
import requests
import json


BULK_GATE_APP_ID = ""
BULK_GATE_APP_TOKEN = ""


def send_transactional(sms_data):
    BULK_GATE_TRN_URL = ""
    trn_sms_url = "https://portal.bulkgate.com/{}".format(BULK_GATE_TRN_URL)
    api_headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}
    sms_data['application_id'] = BULK_GATE_APP_ID
    sms_data['application_token'] = BULK_GATE_APP_TOKEN
    sms_data['unicode'] = True
    sms_data['country'] = 'IN'
    response = requests.post(trn_sms_url, data=json.dumps(sms_data), headers=api_headers)
    return response


def send_otp(phone):
    body = {"application_id": BULK_GATE_APP_ID,
            "application_token": BULK_GATE_APP_TOKEN,
            "number": f"{phone}",
            "country": "in",
            "language": "en",
            "code_type": "int",
            "code_length": 5,
            "request_quota_number": 1,
            "request_quota_identification": "127.0.0.1",
            "channel": {
                "sms": {
                    "unicode": True
                }
            }
    }
    response_url = "https://{}/{}".format(BULK_GATE_HOST, BULK_GATE_API_URL)

    req = urllib.request.Request(response_url)
    req.add_header('Content-Type', 'application/json')
    json_data = json.dumps(body)
    json_data_asBytes = json_data.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(json_data_asBytes))
    response = urllib.request.urlopen(req, json_data_asBytes)
    otp_id = json.loads(response.read().decode('utf-8'))
    val_otp = otp_id['data']['id'] if "data" in otp_id else otp_id["error"]
    return val_otp


def verify_otp(id, user_otp):
    OTP_VERIFY_URL = '/api/1.0/otp/verify'
    body = {
        "application_id": BULK_GATE_APP_ID,
        "application_token": BULK_GATE_APP_TOKEN,
        "id": id,
        "code": user_otp
    }

    response_url = "https://{}/{}".format(BULK_GATE_HOST, OTP_VERIFY_URL)

    req = urllib.request.Request(response_url)
    req.add_header('Content-Type', 'application/json')
    json_data = json.dumps(body)
    json_data_asBytes = json_data.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(json_data_asBytes))
    response = urllib.request.urlopen(req, json_data_asBytes)
    otp_id = json.loads(response.read().decode('utf-8'))
    val_otp = otp_id['data']['verified'] if "data" in otp_id else otp_id["error"]
    if isinstance(val_otp, bool):
        return True if val_otp else False
    else:
        return val_otp
