import requests

def send(question, url, webhook_url):
    json = {
        "content": f"Question: {question} \n URL: {url}"
    }
    response = requests.post(webhook_url, json=json)

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1308426087331663953/Ylj_p9qaEVBSq_Cfifkl31KsWhjyCU4A2d3NTcRp_hlX4WR6K9-gi1Nux4iSfIMJFOde"

    send(
        "The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying Eureka? Because this sum gives the same number",
        "https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python",
        webhook_url
    )
