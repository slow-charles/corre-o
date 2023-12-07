import os
import cv2

path = "Images"

images = []

for file in os.listdir("Images"):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpeg', '.jfif']:  # Corrigindo o formato jpeg para '.jpeg'
        file_name = path + '/' + file
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape

size = (width, height)

out = cv2.VideoWriter('pordosol.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(0, count - 1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()  # Corrigindo a chamada para o método release()
print("concluído")