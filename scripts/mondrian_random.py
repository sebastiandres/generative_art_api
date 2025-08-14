"""
Script to create an image similar to the paintings of Piet Mondrian artwork of Composition in White, Blue and Black.
"""
import base64
try:
    from scripts.mondrian_lib import MondrianObject, paint_artwork
except ImportError:
    from mondrian_lib import MondrianObject, paint_artwork
import random

def generate_random_mondrian(seed=None, N=7, N_trys=10):
    # Configure all the required parameters
    if seed is None:
        seed = random.randint(0, 1000000)
        random.seed(seed)
    else:
        random.seed(seed)
    # Pack them into a dictionary
    params = {
        "seed": seed,
        "N": N,
        "N_trys": N_trys
    }


    # Create a list of N objects. Try N_trys times to find a non-intersecting object, otherwise give up.
    objects = [MondrianObject("square")] # Start with a square to make sure we have at least one interesting object
    for i in range(params["N"]*params["N_trys"]):
        object_type = random.choices(["row", "column", "square"], weights=[1, 1, 1])[0]
        object = MondrianObject(object_type)
        if not object.intersects_with_all(objects):
            objects.append(object)
        if len(objects) == params["N"]:
            break

    filepath = f"aux_{params['seed']}.png"
    paint_artwork(objects, filepath)
    # Get the image as a base64 string
    with open(filepath, "rb") as image_file:
        image_b64 = base64.b64encode(image_file.read()).decode('utf-8')
    # Pack the parameters and the image into a dictionary
    params["image"] = image_b64
    return params

if __name__ == "__main__":
    print(generate_random_mondrian())