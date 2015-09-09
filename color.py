import math

class Color:
    def __init__(self, rgb = None, hsv = None, hexStr=None):
        rgbTuple = rgb
        if hsv is not None:
            h, s, v = hsv
            r, g, b = (0,0,0)

            h /= 60.0
            i = math.floor(h)
            f = h - i
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))

            if i == 0:
                r = v
                g = t
                b = p
            elif i == 1:
                r = q
                g = v
                b = p
            elif i == 2:
                r = p
                g = v
                b = t
            elif i == 3:
                r = p
                g = q
                b = v
            elif i == 4:
                r = t
                g = p
                b = v
            else:
                r = v
                g = p
                b = q
            rgbTuple = (r, g, b)
        elif hexStr is not None:
            # Split into components
            hexStr = hexStr.strip('#')

            rComp = 0
            gComp = 0
            bComp = 0

            if len(hexStr) == 3:
                rComp = hexStr[0] * 2
                gComp = hexStr[1] * 2
                bComp = hexStr[2] * 2
            else:
                rComp = hexStr[0:2]
                gComp = hexStr[2:4]
                bComp = hexStr[4:6]

            r = int(rComp, 16) / 255.0
            g = int(gComp, 16) / 255.0
            b = int(bComp, 16) / 255.0

            rgbTuple = (r,g,b)

        r, g, b = rgbTuple
        self.r = r
        self.g = g
        self.b = b
