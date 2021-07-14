import graphviz as gv
import matplotlib.pyplot as plt

def draw(alfabeto, estados, inicio, trans, final):
    g = gv.Digraph(format='png')
    g.graph_attr['rankdir'] = 'LR'
    g.graph_attr['center'] = 'true'
    g.graph_attr['size'] = "5,5"
    g.node('ini', shape="point")
    for e in estados:
        if e in final:
            g.node(e, shape="box")
        else:
            g.node(e,shape='box')
        if e in inicio:
            g.edge('ini',e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))
    g.render(format='png')


# Ejemplo de uso

if __name__ == '__main__':
    alf = [0,1]
    estados = ["A","B","C","D","E","F"]
    trans = [("A","B", 0),
            ("B","C",0),
            ("A","E",0),
            ("A","A",0),
            ("A","D",0),
            ("F","F",0),
            ("D","C",0),
            ("B","A",0), 
            ("E","C",0),
            ("F","D",0),
            ("C","A",0),
            ("B","B", 0),
            ("B","C",0),]
    inicial = ("A")
    terminal = ("C")

    draw(alf, estados, inicial, trans, terminal)

import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"


def main():
    image = text_image('content.txt')
    image.show()
    image.save('content.png')


def text_image(text_path, font_path=None):

    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


if __name__ == '__main__':
    main()


lines = ['~ Q1 Q2 Q3', '0 Q1 ~~ ~~']
with open('content.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


matriz=[]
matriz=[['aaa', 'v', 's'], ['g', 'f', 'd'], [], ['hg', 'fd', 'ds'], [], ['a', 'v', 's'], [], ['hg', 'fd', 'ds']]

i=10
print(matriz)
if ['aaa', 'v', 's'] not in matriz:
    i=i+10
    print('si')

print(i)

for i in matriz:
    if i ==[]:
        matriz.pop(i)
print(matriz)

