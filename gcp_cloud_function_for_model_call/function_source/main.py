
from google.cloud import aiplatform


def stroke_predictor(request):
    req = request.get_json()
    project = req['projectid']
    location = "us-central1"
    instances = req['instance_dict']['instances']
    endpoint = req['endpoint_id']
    aiplatform.init(project=project, location=location)
    endpoint = aiplatform.Endpoint(endpoint)
    prediction = endpoint.predict(instances=instances)
    print(prediction)
    #return {'predictions':prediction.predictions,'deployed_model_id':prediction.deployed_model_id}
    return (str(int(prediction.predictions[0]['scores'][1]*100)))