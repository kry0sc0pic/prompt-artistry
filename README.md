# Prompt Artistry
Prompt engineering game where the player tries to replicate the reference image. Image similarity is compared using differential hashing. The player with the lowest difference score wins.

I built this challenge for the annual techfest event as part of my institution's GDSC.

### tech stack
- streamlit
- replicate
- stable diffusion (Kandinsky 2.2)

### setup
```bash
git clone https://github.com/kry0sc0pic/prompt-artistry.git
cd prompt-artistry
pip install -r requirements.txt
```

### replicate api
get an api key from [replicate](https://replicate.com) and set it in the `.env` file.

### run
```bash
streamlit run main.py
```

### improvements
- add a leaderboard
- daily challenge

*feel free to make a pull request for any improvements*

