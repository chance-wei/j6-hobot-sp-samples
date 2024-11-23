import sys, os, time
sys.path.append("/usr/lib")
import libsrcampy

if __name__ == '__main__':
    cam = libsrcampy.Camera()
    ret = cam.open_cam(0, -1, 30, 1920, 1080)
    a = 0
    while a < 10:
        img = cam.get_img(2)
        outimg = 'output%d.yuv' % a
        fo = open(outimg, "wb")
        fo.write(img)
        fo.close()
        print("write image success count: %d" % a)
        a = a + 1

    cam.close_cam()
    print("test_camera_dump done!!!")
