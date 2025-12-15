import requests

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

if __name__ == "__main__":
    result = get_data()
    print("Result:", result)
