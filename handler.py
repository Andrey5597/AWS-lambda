import json
import requests
import ast


def load_timer(event, context):
    """
        example of request body: ["http://google.com", "http://facebook.com", "any fake url"]
        response : {
            statusCode: 200
            "body": {
            'url': 'load_time',
            ...
            }
        }
    """
    try:
        list_of_urls = ast.literal_eval(event.get('body'))
    except Exception:   
        return {"statusCode": 400, "body": json.dumps({"statusCode": 400})}
    body = {}
    for url in list_of_urls:
        try:
            time = requests.get(url).elapsed.total_seconds()
            body[url] = time
        except Exception:
            body[url] = 'URL is invalid'
    return {"statusCode": 200, "body": json.dumps(body)}
