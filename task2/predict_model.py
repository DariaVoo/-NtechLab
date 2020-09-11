import torch
import torch.nn as nn
import torch.optim as optim


PATH = 'gdrive/My Drive/NtechLab_test/task2/modelext.pth'
model = torch.load(PATH)
print(model.eval())