from google import genai

client = genai.Client(api_key="AIzaSyDNZXJ0xRA4_BTvCWbBrBdCwAGuof_kzJA")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)
