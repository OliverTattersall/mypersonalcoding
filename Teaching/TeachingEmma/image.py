import skimage.io as io
image = io.imread("20201017_163457.jpg")

n_row, n_col, colours = image.shape

for i in range(n_row):
    for j in range(n_col):
        if (i//100) %2 == (j//100) %2:
            image[i,j] = (0,0,0)



io.imsave("quiz.jpg", image)