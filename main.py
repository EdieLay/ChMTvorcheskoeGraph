import plotly.graph_objs as go
import pandas as pd

def main():
    with open('C:/Users/user/source/repos/ChMTvorcheskoe1/ChMTvorcheskoe2/points.txt', 'r') as f:
        n = int(f.readline())
        print(n)
        x = f.readline().split()
        x = list(map(lambda el: float(el), x))
        print(x)
        fx = f.readline().split()
        fx = list(map(lambda el: float(el), fx))
        print(fx)
        #px = f.readline().split()
        #px = list(map(lambda el: float(el), px))
        #print(px)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=fx, mode='lines+markers', name='f(x)'))
        #fig.add_trace(go.Scatter(x=x, y=px, mode='markers', name='P(x)'))
        fig.show()

if __name__ == '__main__':
    main()

