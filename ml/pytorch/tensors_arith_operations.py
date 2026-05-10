import torch

tensor = torch.rand(4, 4)


# These 3 compute the matrix multiplication between two tensors. y1, y2, y3 will have the same value
y1 = tensor @ tensor.T

y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(tensor)
torch.matmul(tensor, tensor.T, out=y3)

# print(y1)
# print(y2)
# print(y3)


# This computes the element-wise product. z1, z2, z3 will have the same value
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)

# print(z1)
# print(z2)
# print(z3)


# Converting tensor with one element to python native datatype
agg = tensor.sum()
agg_item = agg.item()
# print(agg_item, type(agg_item))


#In place operations that store the result in the operand
print(tensor, "\n")
tensor.add_(5)
print(tensor)

