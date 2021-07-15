import torch 
 
x  = torch.randn((3,5), requires_grad= True)
print(x)
y = torch.randn((3,1), requires_grad= True)
z = torch.multiply(torch.square(x), y) 
print(z)
print("calling backward on z = x**2 * y :")
try:
    z.backward()
except Exception as e:
    print(e)
z = torch.mean(z)
z.backward()
print(x.grad)
print(y.grad)