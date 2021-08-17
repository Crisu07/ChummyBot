import requests

#letters of the dictionary to add to url
links = ['/a','/b','/c','/d','/f','/g','/h','/j','/k','/l','/m','/n','/p','/q','/r','/s','/t','/u','/v','/w']
curse = []

exception = ['damn', 'flamer', 'goddamn', 'goddamnit', 'hell', 'humping', 'jap', 'junglebunny', 'jungle bunny', 'lesbian', 'pissed off', 'spook', 'smeg', 'snatch']

#returns list of swear/bad words
def get_curse():
  for i in links:
    response = requests.get("https://www.noswearing.com/dictionary" + i)
    lines = response.text.split(">")
    for i in lines:
      if "<a name=" in i:
        joke= i.split("a name=", 1)[1]
        if joke.strip(' "') == "top":
          continue
        curse.append( joke.strip(' "'))
  
  for i in exception:
      curse.remove(i)

  return curse