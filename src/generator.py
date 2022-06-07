from PIL import Image, ImageDraw, ImageFont, ImageSequence
import textwrap


def generate_text(text, gifsize):
    txtimg = Image.new("RGB", gifsize, (255, 255, 255))
    fnt = ImageFont.truetype("ressources/fceb.otf", 40)
    draw = ImageDraw.Draw(txtimg)
    text_size = draw.textsize(text, font=fnt)
    text_wrapped = "\n".join(textwrap.wrap(text, width= len(text)//(text_size[0]/gifsize[0])))
    draw.multiline_text((gifsize[0]/2, gifsize[1]/2), text_wrapped,
              font=fnt, fill="black", anchor="mm", align="center")
    return txtimg


def generate_image(text):
    gifsrc = Image.open("ressources/buzz-lightyear-factory.gif")
    textimg = generate_text(text, gifsrc.size)

    output_array = []
    for frame in ImageSequence.Iterator(gifsrc):
        rendered_frame = Image.new('RGB', (gifsrc.width, gifsrc.height + textimg.height))
        rendered_frame.paste(textimg, (0, 0))
        rendered_frame.paste(frame, (0, textimg.height))
        output_array.append(rendered_frame)
    output_array[0].save("output/output.gif", save_all=True, append_images=output_array, loop=0)
