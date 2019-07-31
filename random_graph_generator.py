import random
from subprocess import call


class RandomGraphGenerator(object):

    def __init__(self):

        self.options = {'directed': False,
                        'min_node_amount':10,
                        'max_node_amount':70,
                        'min_connection_amount': 2,
                        'max_connection_amount':10}

        self.graph_name = "test_graph"
        self.node_amount = 0
        self.connection_amount_range = (0, 0)

    def new_graph(self):
        self.new_amounts()
        nodes, connections = self.generate_graph()
        lines = self.dot_language_from(nodes, connections)
        self.write_to(lines, "graph")
        self.render_graph("graph")

    def new_tree(self):
        self.new_amounts()
        nodes, connections = self.generate_tree()
        lines = self.dot_language_from(nodes, connections)
        self.write_to(lines, "tree")
        self.render_graph("tree")

    def new_amounts(self):
        self.node_amount = random.randint(self.options['min_node_amount'], self.options['max_node_amount'])
        self.connection_amount_range = (self.options['min_connection_amount'], random.choice(range(self.options['min_connection_amount'] + 1, self.options['max_connection_amount'])))

    def generate_tree(self):
        # Create Tree
        node_count = 1
        nodes = ["Root"]

        connections = []

        while node_count < self.node_amount:
            random.shuffle(nodes)
            current_node = nodes.pop(0)
            children_amount = random.randint(self.connection_amount_range[0], self.connection_amount_range[1])
            for n in range(children_amount):
                node_count += 1
                children_name = "N" + str(node_count)
                nodes.append(children_name)

                connections.append((current_node, children_name))
            
            if len(nodes) == 0:
                nodes.append(current_node)
        
        return nodes, connections

    def generate_graph(self):
        connections = set()

        nodes = {}
        for n in range(self.node_amount):
            nodes["N" + str(n)] = random.randint(self.connection_amount_range[0], self.connection_amount_range[1])
            
        for key in nodes.keys():
            while nodes[key] > 0:
                next_node = random.choice(list(nodes.keys()))
                if nodes[next_node] > 0:
                    nodes[next_node] -= 1
                    nodes[key] -= 1
                    connections.add((key, next_node))
        return nodes.keys(), connections

    def dot_language_from(self, nodes, connections):
        """Parse nodes and connection array to a dot language lines"""

        # Set language symbols
        connection_symbol = "--"
        graph_type = "graph"

        if self.options['directed']:
            connection_symbol = "->"
            graph_type = "digraph"

        # Create dot language lines
        output_lines = []
        # Headline
        output_lines.append(graph_type + " " + self.graph_name + " {\n")
        # Line containing all nodes
        node_line = "\t"
        for node in nodes:
            node_line += node + "; "
        node_line += "\n"
        
        output_lines.append(node_line)
        
        # One line per connection
        for connection in connections:
            output_lines.append("\t" + connection[0] + connection_symbol + connection[1] + ";\n")
        output_lines.append("}")

        return output_lines

    def write_to(self, lines, filename):
        with open("static/" + filename, 'w') as f:
            f.writelines(lines)

    def render_graph(self, dot_file):
        """Call extern bash script to render all graph visualizations"""
        call('~/my_data/projects/programming/flask_tree/render.sh {}'.format(dot_file), shell=True)

