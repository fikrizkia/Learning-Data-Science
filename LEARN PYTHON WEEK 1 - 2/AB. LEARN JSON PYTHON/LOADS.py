import json

response_api = '{"email_id": "EM102", "is_spam": true, "confidence_score": 0.98, "sender": null}'


data_baca = json.loads (response_api)

print ("---DATA API---")
print ("Data Email",data_baca["email_id"])
print ("SPAM :", data_baca["is_spam"])
print ("Confidence_score", data_baca ["confidence_score"])
print ("Sender : ", data_baca ["sender"])