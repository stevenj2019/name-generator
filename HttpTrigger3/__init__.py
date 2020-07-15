import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    output = list()
    for i in range(1, 5):
        output.append(random.choice(string.ascii_lowercase))
    return "".join(output)
