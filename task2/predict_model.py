import pickle
import torch
import numpy as np
from skimage import io

from tqdm import tqdm, tqdm_notebook
from pathlib import Path

from multiprocessing.pool import ThreadPool
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

from pathlib import Path
import pandas as pd
from GenderDataset import GenderDataset



def predict(model, test_loader):
    with torch.no_grad():
        logits = []
    
        for inputs in test_loader:
            inputs = inputs.to(DEVICE)
            model.eval()
            outputs = model(inputs).cpu()
            logits.append(outputs)
            
    probs = nn.functional.softmax(torch.cat(logits), dim=-1).numpy()
    return probs


# Будем предсказывать на GPU
train_on_gpu = torch.cuda.is_available()
if not train_on_gpu:
    print('CUDA is not available.  Training on CPU ...')
else:
    print('CUDA is available!  Training on GPU ...')
DEVICE = torch.device("cuda")

# ВАЖНО!!! Укажите путь до модели
PATH = 'gdrive/My Drive/NtechLab_test/modelext.pth'
model = torch.load(PATH)

# PATH_DATA = Path(input())
PATH_DATA = Path('gdrive/My Drive/NtechLab_test/task2/testset')
data_files = list(PATH_DATA.rglob('*.jpg'))[:50]

# Получаем предсказания с набора
dataset = GenderDataset(data_files, mode="test")
loader = DataLoader(dataset, shuffle=False, batch_size=64)
probs = predict(model, loader)

# Переводим вероятности классов в названия классов
label_encoder = LabelEncoder()
label_encoder.fit(["male", "female"])

# label_encoder = pickle.load(open("label_encoder.pkl", 'rb'))
preds = label_encoder.inverse_transform(np.argmax(probs, axis=1))
filenames = [path.name for path in dataset.files]

# Запись предсказаний в файл .json
df = pd.DataFrame()
df['Id'] = filenames
df['Expected'] = preds

df.set_index('Id')['Expected'].to_json('preds.json')

print("Done")