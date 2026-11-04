"""Pretraživanje po značenju nad opisima listića (poglavlje 26), lokalno.

Isti kôd kao u Colabu, bez prvog retka (!pip). Paket instalirajte u
virtualno okruženje: pip install -r requirements-pretrazivanje.txt
Datoteka: jedan materijal u retku, "naslov | opis", UTF-8. Kôd otvara
listici_izmisljeni.txt iz ove mape; za svoju datoteku promijenite DATOTEKA.
Model se pri prvom pokretanju preuzme (oko 1,2 GB); poslije sve računa
vaše računalo.
"""
from sentence_transformers import SentenceTransformer

# POSTAVKE: za usporedbu upišite "BAAI/bge-m3"
MODEL = "Qwen/Qwen3-Embedding-0.6B"
DATOTEKA = "listici_izmisljeni.txt"   # vlastita: npr. "listici.txt"
retci = open(DATOTEKA, encoding="utf-8").read().splitlines()
listici = [r for r in retci if r.strip()]

model = SentenceTransformer(MODEL)
vektori = model.encode_document(listici)   # svaki redak: 1024 broja

def trazi(upit, koliko=5):
    v = model.encode_query(upit)
    slicnost = model.similarity(v, vektori)[0]   # sa svim retcima
    for i in slicnost.argsort(descending=True)[:koliko]:
        print(f"{slicnost[i]:.2f}  {listici[i].split('|')[0]}")

trazi("razlomci")
