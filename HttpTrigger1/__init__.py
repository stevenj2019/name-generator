import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nums = list(requests.get(''))
    alph = list(requests.get(''))
    name = zip(nums, alph)
