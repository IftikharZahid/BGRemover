pip install rembg
pip install IPython

from rembg import remove
from PIL import Image
input_path = 'dimond.jpg'
output_path = 'output_dimond.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)


from IPython.display import display
display(output)
