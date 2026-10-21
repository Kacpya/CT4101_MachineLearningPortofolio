from huggingface_hub import hf_hub_download

hf_hub_download(
    "FronkonGames/steam-games-dataset",
   "games.csv",
    repo_type="dataset",
   local_dir="data",
)