import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nums = list(requests.get(''))
    alph = list(requests.get(''))
    db.session.add(usernames(zip(name=zip(nums, alph))))
    db.session.commit()