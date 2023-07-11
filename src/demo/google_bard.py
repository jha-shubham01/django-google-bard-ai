from bardapi import Bard, ChatBard

from django.conf import settings


def get_response(prompt):

    bard = Bard(token=settings.BARD_API_KEY)

    response = bard.get_answer(str(prompt))
    print(response)
    return response['content']


# bard = ChatBard(token=settings.BARD_API_KEY, language="english")

# def chat(prompt):

#     response = bard.start()
#     return response
