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
            [(252.0, 141.0, 89.0), (255.0, 255.0, 191.0), (145.0, 191.0, 219.0)]
        )

    def test_to_hsl(self):
        scales = cl.to_hsl(cl.scales['3']['div']['RdYlBu'])
        self.assertEqual(
            scales,
            ['hsl(19.0, 96.0%, 67.0%)', 'hsl(60.0, 100.0%, 87.0%)',
             'hsl(203.0, 51.0%, 71.0%)']
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
