from flask import Flask, jsonify, request
from flask_expects_json import expects_json
import math, uuid

app = Flask(__name__)

receipts = {}

schema = {
    'type': 'object',
    'properties': {
        'retailer': {'type': 'string'},
        'purchaseDate': {'type': 'string'},
        'purchaseTime': {'type': 'string'},
        'total': {'type': 'string'},
        'items': {'type': 'array'}
    },
    'required': ['retailer', 'purchaseDate', 'purchaseTime', 'total', 'items']
}


@app.route("/receipts/process", methods=["POST"])
@expects_json(schema) 
def process_receipt():

    data = request.json
    items = data['items']

    if len(items) == 0:
        return 'items is required', 400
    for item in items:
        if not 'shortDescription' in item or not 'price' in item:
            return 'item is incorrect', 400

    
    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = calculatePoints(data)

    return receipt_id, 200

@app.route("/receipts/<id>/points", methods=["GET"])
def get_points(id):
    if id in receipts:
        return jsonify({"points" : receipts[id]}), 200 
    else:
        return 'No receipt found', 404
    
def get_retailerPoints(retailer):
    points = 0
    for name in retailer:
        if name.isalnum():
            points +=1
    return points

def getValuePoints(total):
    points =0
    countCents = total[-2:]
    if countCents == '00':
        points += 50
    
    if int(countCents) % 25 ==0:
        points +=25

    return points


def get_itemPoints(items):
    points =0
    countItems = len(items)
    points += (countItems//2) * 5

    for i in items:
        desc , price = i['shortDescription'], float(i['price'])
        if len(desc.strip()) % 3 ==0:
            points += math.ceil(price * 0.2)
    
    return points


def get_purchasePoints(purchase_date):
    points = 0
    datesDight = purchase_date[-1]
    if int(datesDight) % 2 ==1:
        points+=6
    
    return points

def get_purchaseTimePoints(purchase_time):
    points =0
    purchaseHour, purchaseMinute = purchase_time[0:2], purchase_time[3:5]
    if (purchaseHour == '14' and purchaseMinute != '00') or purchaseHour == '15':
        points += 10
    return points

def calculatePoints(data):
    points = 0
    retailer = data['retailer']
    purchaseData = data['purchaseDate']
    puchaseTime = data['purchaseTime']
    total = data['total']
    items = data['items']


    points += get_retailerPoints(retailer)
    points += getValuePoints(total)
    points += get_itemPoints(items)
    points += get_purchasePoints(purchaseData)
    points += get_purchaseTimePoints(puchaseTime)

    return points

if __name__ == "__main__":
    app.run(debug = True, host ="0.0.0.0", port = 5001)