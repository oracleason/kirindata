# -*- coding:utf-8 -*-

import json
from collections import OrderedDict

def update_json(idempotencyKey, po1,bokkingid,containerId1,itemId1, po2,containerId2,itemId2):
    data = '{"header": {   "major_version": 1,   "type": "com.amazon.xbt.schema.nodeinstruction.NodeInstruction",   "minor_version": 0 },  "idempotencyKey": "96607521-7d0c-48d8-99e8-amztestqa001",  "creationTime": "2019-07-01T00:00:00.000Z", "node": {  "location": {     "code": "KUK2",     "codeType": "NODE_ID",      "locationType": "ORIGIN_CONSOLIDATION"   } },"consignment": {"cargo": {"containers": [{"clientProvidedReferences": [{"type": "PURCHASE_ORDER_NUMBER", "value": "QA000001"}, {             "type": "BOOKING_ID",              "value": "AMZTEST00011QA1"           }         ],         "volume": {          "unit": "CU_METER",           "value": 1.0          },        "deliveryDetail": {          "location": {            "address": {              "countryCode": "US",            "name": "ABE2"           }        }       },        "containerType": "VIRTUAL",         "weight": {      "unit": "KG",          "value": 89.4         },         "containerId": "2d3f75be-478e-49e4-ae7a-container001",         "items": [           {             "externalItemIdentifiers": [               {                 "externalItemIdType": "ASIN",                "externalItemIdValue": "B0757G1MYQ"              }            ],           "quantity": 36,           "tags": [             {                 "key": "LINE_ITEM_ID",                 "value": "SZ1L000116372"               }             ],           "itemId": "54ca347c-9781-4770-b146-itemsid00001"     }          ],  "contentSummary": {          "containerTypeToCountMappings": [           {              "containerType": "CARTON",                "count": 3             }           ]        }, "shippingRequestHierarchicalId": {"shippingRequestContainerId": "2d3f75be-478e-49e4-ae7a-8b12699aa10d",  "shippingRequestId": "100r-1cto-q96p-bnd0"         }       },       {       "clientProvidedReferences": [           {            "type": "PURCHASE_ORDER_NUMBER",             "value": "QA000002"          },           {            "type": "BOOKING_ID",             "value": "AMZTEST00011QA1"           }        ],         "volume": {           "unit": "CU_METER",            "value": 3.7        },         "deliveryDetail": {           "location": {             "address": {               "countryCode": "US",               "name": "ABE2"             }           }         },        "containerType": "VIRTUAL",         "weight": {           "unit": "KG",           "value": 61.6         },         "containerId": "2d3f75be-478e-49e4-ae7a-container002",         "items": [           {             "externalItemIdentifiers": [               {                "externalItemIdType": "ASIN",                "externalItemIdValue": "B06WVMKWBP"                }           ],            "quantity": 48,             "tags": [               {                "key": "LINE_ITEM_ID",                 "value": "SZ1L000116373"             }            ],             "itemId": "54ca347c-9781-4770-b146-itemsid00002"          }        ],        "contentSummary": {           "containerTypeToCountMappings": [            {                "containerType": "CARTON",              "count": 4             }           ]         },         "shippingRequestHierarchicalId": {          "shippingRequestContainerId": "61833bc9-96b1-441f-ae69-0797d3020533",            "shippingRequestId": "100r-1cto-q96p-bnd0"         }       }     ]   } },"logisticsServices": [   {     "consolidationCriteria": {       "consolidationGroup": "GROUP2"     },      "serviceProvider": {        "id": "CDS",      "type": "ORIGIN_CONSOLIDATOR"      },     "header": {       "major_version": 1,       "type": "com.amazon.xbt.schema.nodeinstruction.logisticsservice.Consolidation",       "minor_version": 0     }  } ], "id": "7211-jy25-m480-g6ra",  "version": 1}'
    json_data = json.loads(data, object_pairs_hook=OrderedDict);
    json_data["idempotencyKey"] = idempotencyKey
    json_data["consignment"]["cargo"]["containers"][0]["clientProvidedReferences"][0]["value"] = po1
    json_data["consignment"]["cargo"]["containers"][0]["clientProvidedReferences"][1]["value"] = bokkingid

    json_data["consignment"]["cargo"]["containers"][0]["containerId"] = containerId1
    json_data["consignment"]["cargo"]["containers"][0]["items"][0]["itemId"] = itemId1

    json_data["consignment"]["cargo"]["containers"][1]["clientProvidedReferences"][0]["value"] = po2
    json_data["consignment"]["cargo"]["containers"][1]["clientProvidedReferences"][1]["value"] = bokkingid

    json_data["consignment"]["cargo"]["containers"][1]["containerId"] = containerId2
    json_data["consignment"]["cargo"]["containers"][1]["items"][0]["itemId"] = itemId2

    file_out = open("../output/DA_QATest.json", "w")
    file_out.write(json.dumps(json_data, indent=2))
    file_out.close()







