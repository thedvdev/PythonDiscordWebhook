import requests

# Replace the URL below with your Discord Webhook URL
url = 'https://discord.com/api/v8/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN'

# Set the message text
message = 'Hello, Discord!'

# Construct the JSON payload
payload = {
    'content': message
}

# Send the HTTP request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 204:
    print('Message sent successfully!')
else:
    print('Failed to send message. Status code:', response.status_code)