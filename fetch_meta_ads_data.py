import requests
import json

def fetch_meta_ads_data():
    access_token = 'EAAG41HIgnu8BOx8J897i2sE4HR5Ne0W36kjmuYeiDqcrSOddQH8gWI8CoEDB9g9gRpD37cJJxn1r7sVdemMwEZCKTDMHIRK3rEpsjw7Y2zpLJumUkxQFAoCGtsYJWo0oyiYclK93QZB7ekQQAd4iNKJrPLUWtEm1LvQKDezeGYF1NhnyFAptBKdjtcDlEVF81JO8L5'
    ad_account_id = '673961731459956'
    api_url = f'https://graph.facebook.com/v14.0/act_{ad_account_id}/insights'

    params = {
        'fields': 'campaign_name,impressions,clicks,spend',
        'level': 'campaign',
        'access_token': access_token
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    # Print the data (you can adjust this part to store data as needed)
    print(json.dumps(data, indent=4))
    return data
