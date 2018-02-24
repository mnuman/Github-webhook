import json
def lambda_handler(event, context):
    # Just print the event as a first tracer bullet
    print(json.dumps(event, indent=2))
    response_body =  { "message": 'Howdy from Lambda!'}
    
    return {
      "isBase64Encoded": "false",
      "statusCode": 200,
      "headers": {},
      "body": json.dumps(response_body)
    }