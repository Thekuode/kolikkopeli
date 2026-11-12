Idean kolikkopelissä on yksinkertainen ns slottipeli, mutta pienellä twistillä. Tuntuu että ensimmäisellä peli kerralla voittaa paremmin, rahat vähissä niin yhtäkkiä antaa toivoa, ja muita twistejä. Kiinnostus tekemään tätä tuli kun halusin alkaa oppimaan miten slottien rtp toimii ja miten niitä pystyy muokkaamaan ja mitä vaikutusta näitä muuttamalla on.

## Käynnistys (backend)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
