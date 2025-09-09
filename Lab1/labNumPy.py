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
    identity_matrix = np.eye(5)
    print(identity_matrix)
    print("\n")
    random_matrix = np.random.randint(1,11,(3,3))
    print(random_matrix)
    if array_range is not None and array_linear is not None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        axes[0, 0].bar(range(len(array_range)), array_range, color='skyblue')
        axes[0, 0].set_title('Array Range (0 to 20)')
        axes[0, 0].set_xlabel('Index')
        axes[0, 0].set_ylabel('Value')
    if array_linear is not None:
        sine_wave = np.sin(array_linear)
        axes[0, 1].plot(array_linear, sine_wave, 'b-', linewidth=2)
        axes[0, 1].set_title('Sine Wave')
        axes[0, 1].set_xlabel('Radians')
        axes[0, 1].set_ylabel('sin(x)')
        axes[0, 1].grid(True)
    if identity_matrix is not None:
        im = axes[1, 0].imshow(identity_matrix, cmap='RdBu', vmin=0, vmax=1)
        axes[1, 0].set_title('5x5 Identity Matrix')
        plt.colorbar(im, ax=axes[1, 0])
    if random_matrix is not None:
        im = axes[1, 1].imshow(random_matrix, cmap='viridis')
        axes[1, 1].set_title('3x3 Random Matrix')
        for i in range(3):
            for j in range(3):
                axes[1, 1].text(j, i, f'{random_matrix[i, j]}',
                    ha='center', va='center', color='white')
        plt.colorbar(im, ax=axes[1, 1])
    plt.tight_layout()
    plt.show()
    
    return array_range, array_linear, identity_matrix, random_matrix

exercise_1_1()

def exercise_1_2():
    #Explore array attributes with different dimensional arrays.
    print("\n"+"="*50)
    print("Exercise 1.2: Array Attributes")
    print("="*50)
    
    arr_1d = np.array([1,2,3,4,5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    arrays = [
        ("1D Array", arr_1d),
        ("2D Array", arr_2d),
        ("3D Array", arr_3d)
    ]
    
    for name, arr in arrays:
        print(f"\n{name}")
        print(f" Array: {arr}")
        print(f" Shape: {arr.shape}")
        print(f" Dimensions: {arr.ndim}")
        print(f" Data Type: {arr.dtype}")
        print(f" Size : {arr.size}")
        print(f" Item Size: {arr.itemsize} bytes")
        print(f" Total Bytes: {arr.nbytes} bytes")
        
        return arr_1d, arr_2d, arr_3d
    
exercise_1_2()

def exercise_2_1():
    #Compare performance between NumPy arrays and Python lists.
    #Create visualizations showing the speed difference.
    
    print("\n"+"="*50)
    print("Exercise 2.1: The Great Performance Race!")
    print("="*50)
    
    sizes = [100,1000,10000,100000]
    python_times = []
    numpy_times = []
    
    for size in sizes:
        python_list = list(range(size))