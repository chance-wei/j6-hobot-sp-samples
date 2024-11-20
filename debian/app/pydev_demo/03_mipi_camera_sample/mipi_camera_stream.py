import sys, os, time
sys.path.append("/usr/lib")
import libsrcampy

if __name__ == '__main__':
    cam = libsrcampy.Camera()
    ret = cam.open_cam(0, -1, 30, 1080, 1920, 1920, 1080)
    time.sleep(3)
    enc = libsrcampy.Encoder()
    ret = enc.encode(0, 1, 1920, 1080)

    ret = libsrcampy.bind(cam, enc)
   
    fo = open("encode.h264", "wb+")

    a = 0
    while a < 100:
        img = enc.get_img()

        if img is not None:
            fo.write(img)
            print("encode write image success count: %d" % a)
        else:
            print("encode write image failed count: %d" % a)
        a = a + 1
    fo.close()
    ret = libsrcampy.unbind(cam, enc)

    enc.close()
    cam.close_cam()
