from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    # Matrix A: 2x3
    A = [[4, 5, 6],
         [7, 8, 9]]

    # Matrix B: 3x2
    B = [[1, 2],
         [3, 4],
         [5, 6]]

    # Result matrix: 2x2
    result = [[0, 0],
              [0, 0]]

    # Matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    # Convert the matrix to a list of lists
    result_list = [list(row) for row in result]

    # Return the matrix as JSON
    return jsonify(result=result_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)