from flask import Flask, render_template
import astar
import time

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():

    astar.shuffler()
    initialState = astar.initial_state
    print(initialState)
    sec = time.time()
    a, b = astar.ast(initialState)
    sec_astar = round(time.time()-sec, 6)
    moves = astar.backtrace2()
    print(str(moves)+": astar")
    sec2 = time.time()
    c, d = astar.bfs(initialState)
    sec_bfs = round(time.time()-sec2, 6)
    moves2 = astar.backtrace()
    print(str(moves2)+": bfs")
    print(sec_astar)
    print(sec_bfs)

    return render_template('index.html', initial=initialState, moves=moves, moves2=moves2, astar=b, bfs=d, sec_astar=sec_astar, sec_bfs=sec_bfs)

app.run(debug=True)