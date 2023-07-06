import requests
from bs4 import BeautifulSoup


def main():
    # set headers to send to amazon
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    # get html from amazon for the soup
    response = requests.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1', headers=headers)
    # print(response.text)

    # create the soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # log soup in txt file so you can see all of the html
    # with open('misc.txt', mode='w') as f:
    #     f.write(f"{soup}")

    # get the item price
    price_whole = soup.find(class_="a-offscreen").getText()
    price_without_currency = price_whole.split('$')[1]
    price = float(price_without_currency)
    # print(price)


    # check the price to see if it is under $100
    price_checker(price, soup)


def price_checker(price, soup):
    BUY_PRICE = 100

    if price < BUY_PRICE:
        print(f"yay! The price is the item is now {price}!")

        # for email
        # title = soup.find(id="productTitle").get_text().strip()
        # message = f"{title} is now {price}"

        # with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        #     connection.starttls()
        #     result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        #     connection.sendmail(
        #         from_addr=YOUR_EMAIL,
        #         to_addrs=YOUR_EMAIL,
        #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        #     )


if __name__ == "__main__":
    main()