import numpy as np

def hello(name: str) -> str:
    return f"Hello, {name}!"

def generate_random_phenotype(
        num_samples=100,  
        num_independent_vars=2, 
        weights = None, 
        bias = None, 
        noise_level=0.1, 
        noise_type='gaussian', 
        random_seed=42):
    np.random.seed(random_seed)
    # Generate independent variables
    X = np.random.uniform(0, 10, (num_samples, num_independent_vars))
    # Define the phenotype as a function of the independent variables
    if weights is None:
        # Sample from poisson distribution if no weights are provided
        weights = np.random.poisson(1, num_independent_vars + 1)
    else: # check if weights length matches num_independent_vars
        if len(weights) != num_independent_vars:
            raise ValueError("Length of weights must match num_independent_vars")
    print(f"Using weights: {weights}")
    phenotype = np.zeros(num_samples)
    for i in range(num_independent_vars):
        phenotype += weights[i] * X[:, i]
    if bias is None:
        bias = np.random.poisson(1)
    print(f"Using bias: {bias}")
    phenotype += bias

    # Add noise
    if noise_type == 'gaussian' or noise_type == 'normal':
        phenotype = np.random.normal(phenotype, noise_level, num_samples)
    elif noise_type == 'poisson':
        phenotype = np.log(np.exp(phenotype)+1)  # Poisson requires positive values
        phenotype = np.random.poisson(phenotype)
    elif noise_type == 'exponential':
        phenotype += np.random.exponential(noise_level, num_samples)
    elif noise_type == 'uniform':
        phenotype *= np.random.uniform(-noise_level, noise_level, num_samples)
    else:
        raise ValueError("Invalid noise type. Choose 'gaussian' or 'uniform'.")

    return X, phenotype

