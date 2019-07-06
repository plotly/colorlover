import unittest

import colorlover as cl


rgb_hsl_colors = {
            (0, 0, 0): 	(0, 0, 0),  # Black
            (255, 255, 255): 	(0, 0, 100),  # White
            (255, 0, 0): 	(0, 100, 50),  # Red
            (0, 255, 0): 	(120, 100, 50),  # Lime
            (0, 0, 255): 	(240, 100, 50),  # Blue
            (255, 255, 0): 	(60, 100, 50),  # Yellow
            (0, 255, 255): 	(180, 100, 50),  # Cyan
            (255, 0, 255): 	(300, 100, 50),  # Magenta
            (192, 192, 192): 	(0, 0, 75),  # Silver
            (128, 128, 128): 	(0, 0, 50),  # Gray
            (128, 0, 0): 	(0, 100, 25),  # Maroon
            (128, 128, 0): 	(60, 100, 25),  # Olive
            (0, 128, 0): 	(120, 100, 25),  # Green
            (128, 0, 128): 	(300, 100, 25),  # Purple
            (0, 128, 128): 	(180, 100, 25),  # Teal
            (0, 0, 128): 	(240, 100, 25),  # Navy
            (20, 30, 128): 	(234, 72, 29)  # Near navy
}

test_colors = {
    'rgb': ['rgb(252, 141, 89)', 'rgb(255, 255, 191)', 'rgb(145, 191, 219)'],
    'hsl': ['hsl(19,96,67)', 'hsl(60,100,87)','hsl(203,51,71)'],
    'hex': ['#fc8d59', '#ffffbf', '#91bfdb'],
    'numeric': [(252, 141, 89), (255, 255, 191), (145, 191, 219)],
}


class UsageTests(unittest.TestCase):
    def test_scales(self):
        scales = cl.scales['3']['div']['RdYlBu']
        self.assertEqual(
            scales,
            ['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)'])

    def test_to_numeric(self):
        scales = cl.to_numeric(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            scales,
            [(252, 141, 89),
             (255, 255, 191), (145, 191, 219)]
        )

    def test_to_hex(self):
        scales = cl.to_hex(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            scales,
            test_colors.get('hex')
        )

    def test_to_hsl(self):
        scales = cl.to_hsl(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            scales,
            ['hsl(19, 96%, 67%)', 'hsl(60, 100%, 87%)',
             'hsl(203, 51%, 71%)']
        )

    def test_to_rgb(self):
        scales = cl.to_rgb(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            scales,
            ['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
        )

    def test_to_html(self):
        html = cl.to_html(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            html,
            ('<div style="background-color:rgb(252,141,89);'
             'height:20px;width:20px;margin-bottom:0px;display:inline-block;"></div>'
             '<div style="background-color:rgb(255,255,191);'
             'height:20px;width:20px;margin-bottom:0px;display:inline-block;"></div>'
             '<div style="background-color:rgb(145,191,219);'
             'height:20px;width:20px;margin-bottom:0px;display:inline-block;"></div>')
        )

    def test_flipper(self):
        flipped = cl.flipper()['div']['3']['RdYlBu']
        self.assertEqual(
            flipped,
            ['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
        )

    def test_rgb_to_hsl(self):
        # Make sure interpolating a colorscale to the same length does nothing
        # but change colorspace from hsl to rgb
        for rgb, expected_hsl in rgb_hsl_colors.items():
            hsl = cl.rgb_to_hsl(rgb)
            self.assertEqual(hsl, expected_hsl)


if __name__ == '__main__':
    unittest.main()
