from PIL import Image, ImageChops, ImageDraw, ImageFont
kol = (8 , 5)
def create_white_square(id, kol):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #квадраты 20х20
    #расстояние между квадратами 10 пикселей
    img = Image.open('C:/Users/HP/PycharmProjects/TAS/create_sample/square.png', 'r')
    img_w, img_h = img.size
    #
    font_size = 20
    fnt = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    font_size2 = 15
    fnt2 = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    fnt_little = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', 15)
    background = Image.new('RGBA', ((kol[0] * 30) + 20, (kol[1] * 30) + 36), (255, 255, 255, 255))
    print(kol[0] * 35, kol[1] * 40)

    bg_w, bg_h = background.size
    draw_text = ImageDraw.Draw(background)
    # print(background.size)
    q, w = 25, 20
    # q, w = background.size[0] // kol[0] ,background.size[1] // kol[1]
    # x = background.size[0] // kol[0]
    # y = background.size[1] // kol[1]
    x, y = 25, 20
    # print(x, y, 'x y')
    # x, y = 20, 10
    xx, yy = 12, 10
    ya = 1
    for i in range(kol[1]):
        if i == 0:
            for k in range(1, kol[0] + 1):
                if k > 9:
                    draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt_little)
                else:
                        draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt)
                x += 30
                if k + 1 == kol[0]:
                    # print('uf')
                    y += 17
        if i != 0:
            y += 30
        x = q
        for j in range(kol[0]):
            background.paste(img, (x, y))
            x += 30
            if j == 0:
                # print(x)
                draw_text.text((q - 20, y), alphabet[i], fill=('#1C0606'), font=fnt2)
            # if j == 0:
                # for z in range(0, kol[1] + 1, 1):
                #     ya += 25
                #     draw_text.text((13, ya), alphabet[z], fill=('#1C0606'), font=fnt2)

                #     if z == kol[1]:
                #         x+=30


    # offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    # background.paste(img, (10, 10))
    path = f'C:/Users/HP/PycharmProjects/TAS/create_sample/{id}_white_out.png'
    background.show()
    background.save(path)
    return path

create_white_square(0000000, [30, 5])
