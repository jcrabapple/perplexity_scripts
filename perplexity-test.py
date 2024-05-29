import requests
import json

url = "https://api.perplexity.ai/chat/completions"

# Open the prompt txt file in read mode
with open('/home/jason/Documents/prompt.txt', 'r') as file:
    # Read the contents of the file into a variable
    file_contents = file.read()

payload = {
    "model": "llama-3-sonar-large-32k-online",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": file_contents
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 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"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

# Parse the JSON response
response_json = response.json()

# Extract the content item
content = response_json['choices'][0]['message']['content']

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; }}
    </style>
</head>
<body>
    <h1>Daily Report</h1>
    <pre>{}</pre>
</body>
</html>
""".format(content)

# Write the Markdown content to a file
# with open('/home/jason/Documents/daily_report.md', 'w') as markdown_file:
#    markdown_file.write(markdown_content)

# print("Markdown file created successfully.")

# Write the HTML content to a file
with open('/home/jason/Documents/daily_report.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file created successfully.")