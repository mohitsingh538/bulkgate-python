
if __name__ == '__main__':

    import urllib
    import urllib.request
    import json

    BULK_GATE_URL = "https://portal.bulkgate.com/{}"


    def send_transactional(app_id, app_token, sms_data):
        BULK_GATE_TRN_URL = "/api/1.0/advanced/transactional"
        country = sms_data['country'] if 'country' in sms_data else "in"
        text = sms_data['text'] if 'text' in sms_data else "Blank Text"
        sender_id = sms_data['sender_id'] if 'sender_id' in sms_data else "gSystem"
        sender_id_value = sms_data['sender_id_value'] if 'sender_id_value' in sms_data else 'null'

        body = {
                    "application_id": app_id,
                    "application_token": app_token,
                    "admin": sms_data['admin_id'],
                    "number": f"{sms_data['number']}",
                    "unicode": True,
                    "flash": False,
                    "text": text,
                    "sender_id": sender_id,
                    "sender_id_value": sender_id_value,
                    "country": country,
        }

        response_url = BULK_GATE_URL.format(BULK_GATE_TRN_URL)
        req = urllib.request.Request(response_url)
        req.add_header('Content-Type', 'application/json')
        json_data = json.dumps(body)
        json_data_asBytes = json_data.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(json_data_asBytes))
        response = urllib.request.urlopen(req, json_data_asBytes)
        otp_id = json.loads(response.read().decode('utf-8'))
        if "data" in otp_id:
            return {"status": otp_id['data']['status'], "sms_id": otp_id['data']['sms_id']}

        else:
            return {"status": "failure", "error_code": otp_id['code'], "reason": otp_id['error']}


    def send_otp(app_id, app_token, sms_data):
        OTP_SEND_URL = "/api/1.0/otp/send"
        country = sms_data['country'] if 'country' in sms_data else "in"
        language = sms_data['language'] if 'language' in sms_data else "en"
        code_type = sms_data['code_type'] if 'code_type' in sms_data else "int"
        length = sms_data['code_length'] if 'code_length' in sms_data else 4
        limit = sms_data['limit'] if 'limit' in sms_data else 1
        identifier = sms_data['identifier'] if 'identifier' in sms_data else '127.0.0.1'

        body = {"application_id": app_id,
                "application_token": app_token,
                "number": str(sms_data['number']),
                "country": country,
                "language": language,
                "code_type": code_type,
                "code_length": length,
                "request_quota_number": limit,
                "request_quota_identification": identifier,
                "channel": {
                        "sms": {
                            "unicode": True
                        }
                    }
                }
        response_url = BULK_GATE_URL.format(OTP_SEND_URL)

        req = urllib.request.Request(response_url)
        req.add_header('Content-Type', 'application/json')
        json_data = json.dumps(body)
        json_data_asBytes = json_data.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(json_data_asBytes))
        response = urllib.request.urlopen(req, json_data_asBytes)
        otp_id = json.loads(response.read().decode('utf-8'))
        if "data" in otp_id:
            return {"status": "success", "otp_id": otp_id['data']['id']}

        else:
            return {"status": "failure", "error_code": otp_id['code'], "reason": otp_id['error']}


    def verify_otp(app_id, app_token, otp_id, user_otp):
        OTP_VERIFY_URL = '/api/1.0/otp/verify'
        body = {
            "application_id": app_id,
            "application_token": app_token,
            "id": otp_id,
            "code": str(user_otp)
        }

        response_url = BULK_GATE_URL.format(OTP_VERIFY_URL)

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
            return {"status": "failure", "code": otp_id["code"], "reason": otp_id["error"]}


    def resend_otp(app_id, app_token, otp_id):
        OTP_RESEND_URL = '/api/1.0/otp/resend'
        body = {
            "application_id": app_id,
            "application_token": app_token,
            "id": otp_id
        }

        response_url = BULK_GATE_URL.format(OTP_RESEND_URL)

        req = urllib.request.Request(response_url)
        req.add_header('Content-Type', 'application/json')
        json_data = json.dumps(body)
        json_data_asBytes = json_data.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', len(json_data_asBytes))
        response = urllib.request.urlopen(req, json_data_asBytes)
        otp_id = json.loads(response.read().decode('utf-8'))
        if 'data' in otp_id:
            return {"status": "success", "otp-id": otp_id['data']['id']}

        else:
            return {"status": "failure", "code": otp_id["code"], "reason": otp_id["error"]}
