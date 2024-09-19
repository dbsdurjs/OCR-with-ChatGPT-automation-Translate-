import easyocr
import openai

openai.api_key = "your openai api key"

from_A = input('인식 및 번역할 언어 입력: ')
to_B = input('번역될 언어 입력: ')

reader = easyocr.Reader([from_A])
result = reader.readtext('../image/example.png')

translate_ = []
for detection in result:
    translate_.append(detection[1])

translate_ = ' '.join(translate_)   

completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": f"You're an AI for translation. When {from_A} comes in, translate it to {to_B}."
        },
        {
            "role": "user",
            "content": f'translate this {translate_} english to korea'
        }
    ]
)

print(completion.choices[0].message.content)
