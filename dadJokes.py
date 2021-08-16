import requests

def get_joke():
  response = requests.get("https://icanhazdadjoke.com/")
  lines = response.text.split("/>")
  for i in lines:
    if "property=\"og:description\"" in i:
      joke = i.split("content=", 1)[1]
      return ( joke.strip(' "'))