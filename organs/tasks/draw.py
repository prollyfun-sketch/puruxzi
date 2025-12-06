from PIL import Image, ImageDraw

def draw_square(size: int = 100) -> str:
    """
    Draws a black square on white background of the given size.

    Args:
        size (int): The side length of the square.

    Returns:
        str: Path to the saved image.
    """
    img_size = (size + 20, size + 20)  # margin
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # draw square with 10px margin
    top_left = (10, 10)
    bottom_right = (10 + size, 10 + size)
    draw.rectangle([top_left, bottom_right], outline="black", width=3)

    path = f"square_{size}px.png"
    img.save(path)
    return f"[draw_square] Saved to {path}"
