from google.cloud import bigquery
client= bigquery.client()


def conn_to_bigquery(request):

    request_json = request.get_json()
    res= process_req(request_json)
    r= make_response(res)
    return r

def process_req(request_json)

    result= request_json.get("queryResult")
    user_says= result.get("queryText")
    parameters= result.get("parameters")
    location= parameters.get("geo-city")
    budget= parameters.get("budget")

    query= """ SELECT Name FORM chatbotdata.listofpgs
    WHERE Location = {location} AND  Budget <= {budget}
    """
    queryjob= client.query(query)

    fulfillmentText=""
    for row in queryjob
    fulfillmentText+= row[0] +'\n'

    return {
        "fulfillmentText": fulfillmentText
    }