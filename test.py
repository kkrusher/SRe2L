import torch

print(torch.cuda.is_available())
print(torch.cuda.current_device())

for i in range(torch.cuda.device_count()):
    print(torch.cuda.get_device_name(i))
