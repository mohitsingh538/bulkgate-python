# BulkGate SMS - Python Integration

<br>
<br>
<img src="https://portal.bulkgate.com//images/white-label/bulkgate/logo/logo.svg" width="60%"><small>&nbsp;&nbsp;&nbsp;<b>(Unofficial)</b></small>



# Introduction

This is a simplistic integration of BulkGate SMS API and Python. It uses BulkGate's default <b>Advanced API</b>, so you
need to create API from BG's dashboard. <br>

To create API:
- Login to <a href="https://portal.bulkgate.com/">BulkGate</a>
- Go to Modules & API > Advanced API > Create API

# Requirements
- `python 3.x`
- `BulkGate App ID`
- `BulkGate App Token`

# Install
```bash
git clone https://github.com/ohlc-ai/bulkgate-python.git
```
<br>

For sending `Transactional SMS`:
```bash
from python_bulkgate import send_transactional

app_id = 'YOUR APP ID'
app_token = 'YOUR APP TOKEN'

sms_data = {'number': 9999999999, 
            'text': f"Hello {first_name}! This is a test msg.",
            "admin_id": 123   # Your admin ID
           }   # See Parameters below for adding custom params

send_transactional(app_id, app_token, sms_data)
```

<h4>Response to this command would be:</h4>
<br>
In case of success:
```bash
{"status": "accepted", "sms_id": "tmpde1bcd4b1d1"}
```
In case of failure:
```bash
{"status": "failure", "error_code": 400, "reason": "Invalid phone number"}
```
<h5>Parameters for sms_data dictionary:</h5>
<table class="tableizer-table">
<thead><tr class="tableizer-firstrow"><th>PARAMETER</th><th>VALUE</th><th>MANDATORY</th><th>DEFAULT</th></tr></thead><tbody>
 <tr><td>number</td><td>Recipient number</td><td>Yes</td><td>-</td></tr>
 <tr><td>admin</td><td>Number of BulkGate administrator receiving notification.</td><td>Yes</td><td>-</td></tr>
 <tr><td>text</td><td>Text of the SMS message (max. 612 characters, or 268 characters, if Unicode is activated), UTF-8 encoding. It is possible to add variables to the template from the variables array (another parameter) Hello <first_name> <last_name> ....</td><td>Yes</td><td>Blank SMS</td></tr>
 <tr><td>sender_id</td><td>Sender ID, see Sender ID type</td><td>No</td><td>gSystem</td></tr>
 <tr><td>sender_id_value</td><td>Sender value gOwn , gText , gMobile , or gPush (if gMobile , or gPush used, please supply mobile connect key as sender_id_value )</td><td>No</td><td>null</td></tr>
 <tr><td>country</td><td>Provide recipient numbers in international format (with prefix, for e.g 44 ), or add country code ( 7820125799 + GB = 447820125799 ). See the example of a country requirement. If the value is null, your set time zone will be used to fill in the information</td><td>No</td><td>in</td></tr>
</tbody></table>
<br>
<br>

For `sending` OTP:
```bash
from python_bulkgate import send_otp

app_id = 'YOUR APP ID'
app_token = 'YOUR APP TOKEN'

sms_data = {'number': 9999999999}   # See Parameters below for adding custom params

send_otp(app_id, app_token, sms_data)
```

<h4>Response to this command would be:</h4>
<br>
In case of success:
```bash
{"status": "success", "otp_id": "opt-609d984a32c336.12662723"}
```
In case of failure:
```bash
{"status": "failure", "error_code": 400, "reason": "Unknown identity"}
```

<h5>Parameters for sms_data dictionary:</h5>
<table class="tableizer-table">
<thead><tr class="tableizer-firstrow"><th>PARAMETER</th><th>VALUE</th><th>MANDATORY</th><th>DEFAULT</th></tr></thead><tbody>
 <tr><td>number</td><td>Phone number to which send the verification code</td><td>Yes</td><td>-</td></tr>
 <tr><td>country</td><td>Country code of phone number</td><td>No</td><td>in</td></tr>
 <tr><td>language</td><td>Language of send otp message</td><td>No</td><td>en</td></tr>
 <tr><td>code_type</td><td>Type of code. ( string , int , or combined )</td><td>No</td><td>int</td></tr>
 <tr><td>length</td><td>Length of verification code (4-20).</td><td>No</td><td>4</td></tr>
 <tr><td>limit</td><td>The number of requests per minute for request_quota_identification</td><td>No</td><td>1</td></tr>
 <tr><td>identifier</td><td>Identification of the "OTP user / requester" to whom the request_quota_number quota per minute will apply. We recommend using an IP address for this identification.</td><td>Yes</td><td>127.0.0.1</td></tr>
</tbody></table>
<br>
<br>

For `verifying` OTP:

```bash
from python_bulkgate import verify_otp

app_id = 'YOUR APP ID'
app_token = 'YOUR APP TOKEN'

send_otp(app_id, app_token, otp_id, user_otp)
```

<h4>Response to this command would be:</h4>
<br>
In case of success:
```bash
True  # if OTP is Verified
False   # if OTP is incorrect or expired
```
In case of failure:
```bash
{"status": "failure", "code": 400, "reason": "Unknown identity"}
```
<br>
<br>

For `resending` OTP:

```bash
from python_bulkgate import resend_otp

app_id = 'YOUR APP ID'
app_token = 'YOUR APP TOKEN'

resend_otp(app_id, app_token, otp_id)   #OTP ID of recently sent OTP to user
```

<h4>Response to this command would be:</h4>
<br>
In case of success:
```bash
{"status": "success", "otp-id": "opt-609d984a32c336.12662723"}
```
In case of failure:
```bash
{"status": "failure", "code": 400, "reason": "Unknown identity"}
```

### Contact

**Issues should be raised directly in the repository.** For additional questions or comments please email me at mohit@terrebrown.com
