from PIL import Image, ImageDraw, ImageFont
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
    gifsrc = Image.open("ressources/buzz-lightyear-factory.gif").convert("RGB")

    textimg = generate_text(text, gifsrc.size)

    output = Image.new('RGB', (gifsrc.width, gifsrc.height + textimg.height))
    output.paste(textimg, (0, 0))
    output.paste(gifsrc, (0, textimg.height))
    output.show()
