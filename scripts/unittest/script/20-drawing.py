def unittest(data_path, temp_path):
    import sensor
    sensor.reset()
    sensor.set_framesize(sensor.QVGA)
    sensor.set_pixformat(sensor.GRAYSCALE)
    img = sensor.snapshot().clear()
    img.set_pixel(img.width()//2+50, 120, 255)
    img.set_pixel(img.width()//2-50, 120, 255)
    img.draw_line([img.width()//2-50, 50, img.width()//2+50, 50])
    img.draw_rectangle([img.width()//2-25, img.height()//2-25, 50, 50])
    img.draw_circle(img.width()//2, img.height()//2, 40)
    img.draw_string(11, 10, "HelloWorld!")
    img.draw_cross(img.width()//2, img.height()//2)
    sensor.flush()
    img.difference(data_path+"/drawing.pgm")
    stats = img.get_statistics()
    return (stats.max() == 0) and (stats.min() == 0)
