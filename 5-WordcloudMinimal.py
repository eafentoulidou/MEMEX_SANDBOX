
from wordcloud import WordCloud
import matplotlib.pyplot as plt

RappWiener2019a = {
        "arranz": 0.07890095663321488,
        "bereits": 0.055601958621490116,
        "bl": 0.0787890309911564,
        "bnf": 0.06977663507664524,
        "byzantinischen": 0.11301272969132051,
        "claudia": 0.11963248675665712,
        "codex": 0.05347463352490345,
        "drei": 0.06440920160921099,
        "elisabeth": 0.10049128887559197,
        "euchologion": 0.21979552204967004,
        "finden": 0.07531276101176781,
        "folgenden": 0.06177995402387791,
        "gebet": 0.29545775473847374,
        "geburt": 0.053746701015500144,
        "goar": 0.0958083044831895,
        "gott": 0.0879182092735771,
        "handschrift": 0.06440920160921099,
        "handschriften": 0.1044028735123728,
        "hrsg": 0.08689933962896286,
        "immer": 0.05793289308597523,
        "jahrhundert": 0.11945723562635677,
        "kaiser": 0.1287695576405936,
        "kaiserlichen": 0.06569041235227795,
        "kal": 0.17705608039985254,
        "kirche": 0.07765547640133819,
        "kontext": 0.05072204354992386,
        "lasst": 0.055601958621490116,
        "liturgie": 0.061215228582798605,
        "liturgischen": 0.14827188965730698,
        "patmos": 0.06301291827441527,
        "patriarch": 0.05833311331972278,
        "patriarchen": 0.06687250062853077,
        "praxis": 0.07104823340663034,
        "quellen": 0.051797501108521896,
        "rapp": 0.11301272969132051,
        "schiffer": 0.12355990804775582,
        "seit": 0.06372618239457277,
        "siehe": 0.21435170441810839,
        "sowie": 0.10502153045735878,
        "tag": 0.054355820221251766,
        "texte": 0.08488437299642151,
        "texten": 0.06372618239457277,
        "tov": 0.06747391408587408,
        "traditionen": 0.055601958621490116,
        "verschiedene": 0.05213960377737772,
        "verwendung": 0.054948880795985686,
        "vgl": 0.16680587586447038,
        "vita": 0.06325679445550694,
        "weitere": 0.05971855668388905,
        "wurde": 0.13324565409774305,
        "wurden": 0.21498680406200057,
        "zeit": 0.05121287014425167
    }

savePath = "RappWiener2019a"

def createWordCloud(savePath, tfIdfDic):
    wc = WordCloud(width=1000, height=600, background_color="white", random_state=2, relative_scaling=0.5, colormap="gray") 

    wc.generate_from_frequencies(tfIdfDic)
    # plotting
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    #plt.show() # this line will show the plot
    plt.savefig(savePath, dpi=200, bbox_inches='tight')

createWordCloud(savePath, RappWiener2019a)