#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cv.h>
#include <highgui.h>

int main (int argc, char const* argv[])
{
    IplImage *img = 0;
    int height, width, step, channels;
    uchar *data;
    int i, j, k;

    if (argc < 2) {
        printf("Usage: main <image-file-name>\n");
        exit(0);
    }

    img = cvLoadImage(argv[1]);
    if (!img) {
        printf("Could not load image file %s\n", argv[1]);
        exit(0);
    }

    height      = img->height;
    width       = img->width;
    step        = img->widthStep;
    channels    = img->nChannels;
    data        = (uchar *)img->imageData;
    printf("Processing a %dx%d image with %d channels\n", width, height, channels);

    cvNamedWindow("mainwin", CV_WINDOW_AUTOSIZE);
    cvMoveWindow("mainwin", 100, 100);

    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {
            for (k = 0; k < channels; k++) {
                data[i*step + j*channels + k] = 255 - data[i*step + j*channels + k];
            }
        }
    }

    cvShowImage("mainwin", img);
    cvWaitKey(0);

    cvReleaseImage(&img);

    return 0;
}
