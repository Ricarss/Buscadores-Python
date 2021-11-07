from bokeh.plotting  import figure, output_file, show
import random as rd

if __name__ == '__main__':

    f = figure()

    r = rd.randint(50,75)
    x = [val for val in range(-1*r,r)]
    y = [i**2 for i in x]

    f.line(x,y)
    
    output_file('prueba.html')

    show(f)
