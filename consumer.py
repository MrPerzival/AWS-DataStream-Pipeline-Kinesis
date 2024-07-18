import json
import base64

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            # Decode the Kinesis data
            data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            
            # Verify that the data is not empty
            if not data:
                print("Empty data received.")
                continue
            
            payload = json.loads(data)
            filename = payload.get('filename', 'Unknown')
            filetype = payload.get('filetype', 'Unknown')
            
            print(f"The provided file is {filename}/{filetype}")
            
        return {
            'statusCode': 200,
            'body': json.dumps('File type logged successfully')
        }
        
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"JSONDecodeError: {e}")
        }
    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"KeyError: {e}")
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Exception: {e}")
        }
