import sys, os, time
sys.path.append("/usr/lib")
import libsrcampy

if __name__ == '__main__':
    vps = libsrcampy.Camera()
    ret = vps.open_vps(1, 1, 1920, 1080, 1280, 720)
    print("Camera vps return:%d" % ret)

    fin = open("input_1080p.yuv", "rb")
    img = fin.read()
    fin.close()
    vps.set_img(img)

    fo = open("output_scale.img", "wb+")
    img = vps.get_img(2, 1280, 720)
    if img is not None:
        fo.write(img)
        print("encode write image success")
    else:
        print("encode write image failed")
    fo.close()

    vps.close_cam()
    print("test_camera_scale done!!!")