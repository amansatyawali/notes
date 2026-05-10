import torch

tensor = torch.zeros([3, 3], dtype=torch.float)
print(tensor)


src=torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)

idx = torch.tensor([[0, 2, 2], [1, 2, 0]])


tensor = tensor.scatter_(1, index=idx, src=src)

print(tensor)