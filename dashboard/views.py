from django.shortcuts import render, HttpResponse
import os
from groq import AsyncGroq
# API KEY = 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

client = AsyncGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def index(request):
    return render(request, "dashboard/index.html")

async def groq_main_search(request):
    if request.method == "POST":
        user_message = request.POST.get('chatInput')
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": f"{user_message}",
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        context = { "message": chat_completion.choices[0].message.content}
        return render(request, "dashboard/index.html", context)

# def groq_image_search(request):
#     completion = client.chat.completions.create(
#         model="llama-3.2-11b-vision-preview",
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "What's in this image?"
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": "https://media.microchip.com/silicon-devices/large/pic10f322-b3x.png"
#                         }
#                     }
#                 ]
#             }
#         ],
#         temperature=1,
#         max_completion_tokens=1024,
#         top_p=1,
#         stream=False,
#         stop=None,
#     )
#
#     context = { "message": completion.choices[0].message.content }
#     print(context)
#     return render(request, "dashboard/image.html", context)