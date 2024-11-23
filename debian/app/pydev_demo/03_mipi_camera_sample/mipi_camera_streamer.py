import sys, os, time
sys.path.append("/usr/lib")
import libsrcampy

if __name__ == '__main__':
    cam = libsrcampy.Camera()
    ret = cam.open_cam(0, -1, 30, [1920, 1280], [1080, 720])
    print("Camera open_cam return:%d" % ret)

    enc = libsrcampy.Encoder()
    enc.encode(0, 1, 1920, 1080)
    libsrcampy.bind(cam, enc)

    enc1 = libsrcampy.Encoder()
    enc1.encode(1, 1, 1280, 720)
    ret = libsrcampy.bind(cam, enc1)

    fo = open("encode.h264", "wb+")
    fo1 = open("encode1.h264", "wb+")
    a = 0
    while a < 100:
        img = enc.get_img()
        img1 = enc1.get_img()
        if img is not None:
            fo.write(img)
            fo1.write(img1)
            print("encode write image success count: %d" % a)
        else:
            print("encode write image failed count: %d" % a)
        a = a + 1

    fo.close()
    fo1.close()

    libsrcampy.unbind(cam, enc)
    libsrcampy.unbind(cam, enc1)

    enc1.close()
    enc.close()
    cam.close_cam()
    print("test_camera_streamer done!!!")