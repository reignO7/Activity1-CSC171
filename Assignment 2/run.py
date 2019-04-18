from flask import Flask, render_template
import bfs

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():


    bfs.shuffler()
    initialState = bfs.initial_state
    randomizedState = bfs.randomized_state
    print("initial state: " + str(initialState))
    bfs.bfs(initialState)
    moves = bfs.backtrace()
    print(moves)

    return render_template('index.html', initial=initialState, moves=moves)

app.run(debug=True)
