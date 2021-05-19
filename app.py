from flask import Flask
import random, jsonify

app = Flask(__name__)

sites = """
xVideos
PornHub
xHamster
XNXX
YouPorn
HClips
Porn
TnaFlix
Tube8
Spankbang
DrTuber
Nuvid
IXXX
SunPorno
PornHD
Porn300
PornOne
SexVid
Thumbzilla
ZbPorn
Fuq
XXXBunker
HDHole
3Movs
CumLouder
PornDoe
Xbabe
VipWank
PornDroids
AlohaTube
MatureTube
TubeV
4Tube
BestFreeTube
Shameless
MegaTube
PornTube
PornDig
PornBurst
BigPorn
Fapster
Porn.biz
FapVidHD
MelonsTube
TastyBlacks
LobsterTube
Bobs-Tube
PornRox
PornMaki
Pornid
Sex-XXX
Slutload
ProPorn
Pornhost
TheMaturePorn
XXXVideos247
Its.Porn
HandjobHub
DansMovies
Porn7
ForHerTube
PornHeed
Orgasm
PornRabbit
Tiava
Fux
H2porn
MetaPorn
Here.XXX
PornerBros
""".splitlines()

@app.route("/porn")
def pornsite():
    return random.choice(sites)


if __name__ == "__main__" :
    print(random.choice(sites))
    app.run()