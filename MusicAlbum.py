musicPlayList = []
while True:
    x = str(input())
    if x == 'exit': break
    musicPlayList.append(x)
if len(musicPlayList) == 0:
    print("There is no song in the album")
else:
  try:
      curr = int(input())
      if curr <= 0 or curr > len(musicPlayList): raise Exception
      else: print(f"Currently playing: {musicPlayList[curr-1]}")
  except:
      print("The MP3 Player has an Error")
