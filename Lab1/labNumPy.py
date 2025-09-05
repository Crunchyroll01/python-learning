import numpy as np
import matplotlib.pyplot as plt
import time
plt.style.use('seaborn-v0_8-darkgrid')
np.random.seed(42)
print("\nLab environment ready!\n")
print(f"NumPy version: {np.__version__}")

def exercise_1_1():
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)
    print("\n")

    array_range = np.arange(0,20)
    print(array_range)
    print("\n")
    array_linear = np.linspace(0, 2*np.pi)
    print(array_linear)
    print("\n")
    identity_5x5=np.eye(5)
    print(identity_5x5)
    print("\n")
    random_matrix = np.random.randint(1,11,(3,3))
    print(random_matrix)
    if array_range is not None and array_linear is not None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes[0, 0].bar(range(len(array_range)), array_range, color='skyblue')
    axes[0, 0].set_title('Array Range (0 to 20)')
    axes[0, 0].set_xlabel('Index')
    axes[0, 0].set_ylabel('Value')
    plt.show()
exercise_1_1()