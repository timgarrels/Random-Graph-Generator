from flask import Flask

from random_graph_generator import RandomGraphGenerator


app = Flask(__name__, static_url_path='')
graph_generator = RandomGraphGenerator()


@app.route("/tree", methods=['GET'])
def tree():
    """Generates a new tree and displays it in various render modes"""
    graph_generator.new_tree()

    return app.send_static_file("tree.html")

@app.route("/graph", methods=['GET'])
def graph():
    """Generates a new graph and displays it in various render modes"""
    graph_generator.new_graph()

    return app.send_static_file("graph.html")

@app.route("/files/graph", methods=['GET'])
def files_graph():
    """Serves the current graphviz file for the graph"""
    return app.send_static_file("graph")

@app.route("/files/tree", methods=['GET'])
def files_tree():
    """Serves the current graphviz file for the tree"""
    return app.send_static_file("tree")

def main():
    app.run()


if __name__ == "__main__":
    main()
