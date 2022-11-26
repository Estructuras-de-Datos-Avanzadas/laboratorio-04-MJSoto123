

from PIL import Image
from color import Color
from octree_quantizer import OctreeQuantizer


def reduction_colors(img_name,cant_pixels):
    image = Image.open(str(img_name)+'.png')
    pixels = image.load()
    width, height = image.size

    octree = OctreeQuantizer()

    # add colors to the octree
    for j in range(height):
        for i in range(width):
            octree.add_color(Color(*pixels[i, j]))

    # 256 colors for 8 bits per pixel output image
    palette = octree.make_palette(cant_pixels*cant_pixels)
    

    # create palette for 256 color max and save to file
    palette_image = Image.new('RGB', (cant_pixels, cant_pixels))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        palette_pixels[i % cant_pixels, i / cant_pixels] = (int(color.red), int(color.green), int(color.blue))
    name_palette = str(cant_pixels*cant_pixels) + str(img_name) +'_palette.png'
    palette_image.save(name_palette)

    # save output image
    out_image = Image.new('RGB', (width, height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (int(color.red), int(color.green), int(color.blue))
    name_out = str(cant_pixels*cant_pixels) + str(img_name) +'_out.png'
    out_image.save(name_out)

def main():
    reduction_colors('ramas',16)
    reduction_colors('ramas',8)

if __name__ == '__main__':
    main()
