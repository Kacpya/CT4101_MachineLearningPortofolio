CT4101 Machine Learning | Kacper Konopka | 22357246 | Milestone 2: Data and Baseline Checkpoint

**Repository:** 
https://github.com/Kacpya/CT4101_MachineLearningPortofolio

**Research question:**
By only using information available on a games store page at launch can we predict whether the game will be well received by players?

**Dataset:** 
 - Steam games dataset (about 125,000 rows) - https://huggingface.co/datasets/FronkonGames/steam-games-dataset
 - Data is not stored in the repository. download_data.py downloads it into data/games.csv

**Target:**
well_received = 1 if positive / (postive + negative) >= 0.80, only for games with atleast 50 reviews.

**Repository contents:** 
milestone2_notebook.ipynb:      Data audit, cleaning, evaluation design, leakage register, preprocessing pipeline and baseline results.
download_data.py:               Downloads games.csv from Hugging Face into data/
requirements.txt:               Python packages
data/: 	                        Created by download_data.py; ignored by git

**Setup and run:**
Tested with Python 3.14.7 (pandas 3.1.0, numpy 2.5.4, scikit-learn 1.9.1). The notebook prints the versions it runs with.

*Windows Powershell commands from repository folder:*

python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python download_data.py

**Running notebook in vs code:**
1. Open milestone2_notebook.ipynb.
2. Click Select Kernel and choose the .venv environment.
3. Click Restart, then Run All.

**Milestone 2: Data Audit**

*Notebook responsibilities:*
 - Data audit: shows data shape, variable types, missing values, duplicates, target distribution and outliers.
 - Preprocessing: pipeline: cleaning,feature pipeline on training data.
 - Split Design testing
 - Leakage checks
 - Baseline model results: majority class and logistic regression on price and genre

*Design Evaluation:*
 - **Time-based split by release date:** oldest 70% train, next 15% validation, newest 15% test. No cross-validation at this stage because a random k-fold would mix older and newer games.
 - **Primary metric:** PR-AUC for the minority class in the training data. Also F1 and recall for that class, ROC-AUC, Brier score and calibration error (ECE). Accuracy is for context only.
 - **Leakage control:** post-release columns (review counts except for building the label, tags, owners, playtime, scores) are never used as features. All learned preprocessing and the model are fitted on the training data only. The decision threshold is chosen on the validation set and the test set is scored once.

*Baseline results (test set) - Full results and plots are in the notebook*

Model:      Majority class
PR-AUC:     0.316
ROC-AUC:    0.500
F1:         0.000
Recall:     0.000
Accuracy:   0.684

Model:      Logistic Regression (price + genre)
PR-AUC:     0.415
ROC-AUC:    0.597
F1:         0.484
Recall:     0.750
Accuracy:   0.494

*Reproducibility*
 - Random seed is fixed (SEED = 42)
 - Raw file never edited, every step is done in the code
 - Package versions are in requirements.txt and printed at the top of the notebook

**AI Assistance**
- Github copilot was used for assisting with code, fixing bugs and writing comments on the code.
- Claude was used to assist me with the structure of the data audit and what steps I should take.