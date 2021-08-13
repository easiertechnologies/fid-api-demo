import requests


# make get request to get the data
# r = requests.get('https://api.github.com/users/mattdavis0351/repos')

# print the response body
# print(r.text)


# # use iex trade api to get current price of a stock
# def get_price(ticker):
#     url = 'https://api.iextrading.com/1.0/tops/last?symbols=' + ticker
#     response = requests.get(url)
#     return response.json()


# twitter = get_price('aapl')

# print(twitter)


# get user data from github api
# def get_user_data(username):
#     url = 'https://api.github.com/users/' + username
#     response = requests.get(url)
#     return response.json()


# u = get_user_data('mattdavis0351')
# print(u)
``

# get random joke from icanhazdadjoke api


def get_joke():
    url = 'https://icanhazdadjoke.com/'
    # add application/json to the header
    headers = {'Accept': 'application/json',
               "User-Agent": "my-joke-bot, https://github.com/mattdavis0351/my-joke-bot"}
    response = requests.get(url, headers=headers)
    return response


j = get_joke()
print(j.text['joke'])
