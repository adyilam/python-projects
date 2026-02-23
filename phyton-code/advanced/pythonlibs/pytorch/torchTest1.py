import torch

x = torch.rand(5, 3)
print(x)

input_tensor = torch.randn(4)
print(input_tensor)
output_tensor = torch.sqrt(input_tensor)
print(">>> ", output_tensor)
