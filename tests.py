import unittest

import colorlover as cl


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
             'height:20px;width:20px;display:inline-block;"></div>'
             '<div style="background-color:rgb(255,255,191);'
             'height:20px;width:20px;display:inline-block;"></div>'
             '<div style="background-color:rgb(145,191,219);'
             'height:20px;width:20px;display:inline-block;"></div>')
        )

    def test_flipper(self):
        flipped = cl.flipper()['div']['3']['RdYlBu']
        self.assertEqual(
            flipped,
            ['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
        )


if __name__ == '__main__':
    unittest.main()
