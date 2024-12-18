from PIL import Image, ImageFilter
#1 - так можно узнать основные данные об исходном изображении.Размер,расширение, формат, вес.
# original = Image.open('pictures/img_6.jpg')
# print(original.format, original.size, original.mode)

#2- меняем размер изображения
# size = (128,128)
# original = Image.open('pictures/img_6.jpg')
# original.thumbnail(size)
# original.save('pictures/img_7.jpg')#и создаем переменную для сейва результата, что бы убедится в нем
# original.show()#открываем


#3 накладываем фильтры на изображение
# original = Image.open('pictures/img_6.jpg')
# img = original.filter(ImageFilter.BLUR)#делаем размытие
# img.save('pictures/img_8.jpg')
# img.show()

#конвертируем изображение
img = Image.open('pictures/img_6.jpg')
new_img = 'pictures/img_6.jpg'#указываем новый формат
img.save(new_img)



