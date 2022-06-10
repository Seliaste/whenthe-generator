from PIL import Image, ImageDraw, ImageFont, ImageSequence
import textwrap


def generate_text(text, gifsize):
    fnt = ImageFont.truetype("ressources/fceb.otf", 40)
    tmpimg = Image.new("RGB",gifsize, (255, 255, 255))
    tmpdraw = ImageDraw.Draw(tmpimg)
    text_size = tmpdraw.textsize(text, font=fnt)
    text_split = textwrap.wrap(text, width= len(text)//(text_size[0]/gifsize[0]))
    text_wrapped = "\n".join(text_split)
    height = 50*len(text_split)
    print(height)
    txtimg = Image.new("RGB",(gifsize[0],height), (255, 255, 255))
    draw = ImageDraw.Draw(txtimg)
    draw.multiline_text((gifsize[0]/2, height/2), text_wrapped,
              font=fnt, fill="black", anchor="mm", align="center")
    return txtimg


def generate_image(text):
    print("Generating gif...")
    gifsrc = Image.open("ressources/x-when-y-walks-in.gif")
    textimg = generate_text(text, gifsrc.size)

    output_array = []
    for frame in ImageSequence.Iterator(gifsrc):
        rendered_frame = Image.new('RGB', (gifsrc.width, gifsrc.height + textimg.height))
        rendered_frame.paste(textimg, (0, 0))
        rendered_frame.paste(frame, (0, textimg.height))
        output_array.append(rendered_frame)
    output_array[0].save("output/output.gif", save_all=True, append_images=output_array[1:], loop=0, optimize=True, duration=50)
    print("Gif generated. Find the output in the output directory")
