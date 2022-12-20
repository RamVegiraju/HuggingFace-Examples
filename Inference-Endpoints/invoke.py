import requests
import time

headers = {
    'Authorization': 'Bearer PYVevWdShZXpmWWixcYZtxsZRzCDNVaLillyyxeclCIlvNxCnyYhDwNQGtfmyQfciOhYpXRxcEFyiRppXAurMLafbPLroPrGUCmLsqAauOVhvMVbukAqJQYtKBrltUix',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'inputs': 'I like you. I love you',
}

def invoke_ep(headers, json_data):
    response = requests.post('https://wuiun4dp26z8vjqv.us-east-1.aws.endpoints.huggingface.cloud', headers=headers, json=json_data)
    return response.text

request_duration = 100
end_time = time.time() + request_duration
print(f"test will run for {request_duration} seconds")
while time.time() < end_time:
    invoke_ep(headers, json_data)