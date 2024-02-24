# Receipt Processor

## Exercise details

The task is to build a webservice that fulfils the documented API.Formal definition is provided in the .yml file.

Endpoint: Process Receipts
- Path: /receipts/process
- Method: POST
- Payload: Receipt JSON
- Response: JSON containing an id for the receipt.

Endpoint: Get Points
- Path: /receipts/{id}/points
- Method: GET
- Response: A JSON object containing the number of points awarded.

## Execution details 

### Setting up 
- Python | Flask | Docker

- Build details:

          git clone https://github.com/pritigumaste/fetch-assessment.git
          cd fetch-assessment/
          Ensure that docker is running in your system.
          docker compose up --build       
          Navigate to localhost:5001\<api-endpoint> endpoints to perform POST and GET. (You can also use Postman for this).

### API Calls
  
- POST Request

For executing the POST request, we can use Postman and make a call to the endpoint http://localhost:5001/receipts/process. We have it hosted on our localhost with the endpoint that is given. Our request body will contain the following data:  

        {
          "retailer": "M&M Corner Market",
          "purchaseDate": "2022-03-20",
          "purchaseTime": "14:33",
          "items": [
            {
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            },{
              "shortDescription": "Gatorade",
              "price": "2.25"
            }
          ],
          "total": "9.00"
        }

Response to our POST request
  
  ![Image]()

- GET Request

As a response you will get a <receipt_id> which you will pass in the second request which will be a GET request like the following http://localhost:5001/receipts/<receipt_id>/points. 

Response to our GET request

  ![Image]()
