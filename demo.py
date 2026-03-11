import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

print("Cargando modelo")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

pipe = pipe.to("cpu")

print("Modelo cargado")

def generar_imagen(prompt):

    print("Generando imagen")

    image = pipe(
        prompt,
        num_inference_steps=15
    ).images[0]

    image.save("imagen_generada.png")

    print("Imagen guardada como imagen_generada.png")

prompt = input("Escribe el prompt para generar la imagen: ")

generar_imagen(prompt)