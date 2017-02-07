# colorlover

Color scales for humans

IPython notebook: https://plot.ly/ipython-notebooks/color-scales/

```
import colorlover as cl
from IPython.display import HTML
HTML(cl.to_html( cl.flipper()['seq']['3'] ))
```

![alt tag](http://i.imgur.com/XUUYEKy.png)


## Install

```
sudo pip install colorlover
```

## IPython notebook (demo)

https://plot.ly/ipython-notebooks/color-scales/

## Docs

### cl.scales

All of the color scales in colorlover

```
>>> import colorlover as cl
>>> cl.scales['3']['div']['RdYlBu']

['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
```

### cl.to_numeric( scale ) 

Converts scale of RGB or HSL strings to list of tuples with RGB integer values

```
>>> cl.to_numeric( cl.scales['3']['div']['RdYlBu'] )

[(252.0, 141.0, 89.0), (255.0, 255.0, 191.0), (145.0, 191.0, 219.0)]
```

### cl.to_hsl( scale ) 

Converts a string RGB or numeric RGB colorscale to HSL

```
>>> cl.to_hsl( cl.scales['3']['div']['RdYlBu'] )

['hsl(19.0, 96.0%, 67.0%)', 'hsl(60.0, 100.0%, 87.0%)', 'hsl(203.0, 51.0%, 71.0%)']
```

### cl.to_rgb( scale )

Convert an HSL or numeric RGB color scale to string RGB color scale

```
>>> cl.to_rgb( cl.scales['3']['div']['RdYlBu'] )

['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
```

### cl.to_html( scale )

Traverse color scale dictionary and return available color scales as HTML string

```
>>> cl.to_html( cl.scales['3']['div']['RdYlBu'] )

'<div style="background-color:rgb(252,141,89);height:20px;width:20px;display:inline-block;"></div><div style="background-color:rgb(255,255,191);height:20px;width:20px;display:inline-block;"></div><div style="background-color:rgb(145,191,219);height:20px;width:20px;display:inline-block;"></div>'
```

### cl.flipper( scale=None )

Return the inverse of the color scale dictionary cl.scale

```
>>> cl.flipper()['div']['3']['RdYlBu']

['rgb(252,141,89)', 'rgb(255,255,191)', 'rgb(145,191,219)']
```

### cl.interp( scale, r )

def interp(scl, r):

Interpolate a color scale "scale" to a new one with length "r" 

```
# fun usage in IPython notebook
from IPython.display import HTML
HTML( to_html( to_hsl( interp( cl.scales['11']['qual']['Paired'], 5000 ) ) ) )
```

## All colors in cl.scales

```
# (in IPython notebook)
from IPython.display import HTML
HTML(cl.to_html( cl.scales ))
```
