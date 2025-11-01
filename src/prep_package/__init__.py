# if you import functions into __init__ you can import them directly with:
# from prep_package import hello
# Otherwise you have to import them from the module with 
# from prep_package.example_functions import hello
from .example_functions import hello, generate_random_phenotype

