import networkx as nx
from networkx.algorithms.operators.binary import disjoint_union

def input_node_generator():
    input_node = 1
    while True:
        yield "INPUT" + str( input_node )
        input_node += 1


def add_input_to_graph( f, g ):
    if not nx.is_directed( g ):
        raise Exception( "single line input graph must be directed." )

    ng = input_node_generator()
    g.add_node( "INPUT", tag="input" )
    last_char = "INPUT"

    # Should be just one line in the file
    line = next( f )
    line = line.strip()

    for c in line:
        n = next( ng )
        g.add_node( n, tag=c )
        g.add_edge( last_char, n, tag="next_char" )
        last_char = n
    

    end = next( ng )
    g.add_node( end, tag="end_of_input" )
    g.add_edge( last_char, end, tag="next_char" )

def add_dot_to_graph( f, g ):
    unique_strings = {}
    
    g2 = nx.DiGraph( nx.drawing.nx_pydot.read_dot( f ) )
    for n in g2.nodes:
        if 'label' in g2.nodes[n]:
            tag = g2.nodes[n]['label']
            if tag[0] == '"':
                tag = tag[1:-1]
            if tag in unique_strings:
                tag = unique_strings[tag]
            else:
                unique_strings[tag] = tag    
            g2.nodes[n]['tag'] = tag
            del g2.nodes[n]['label']
        to_delete = g2.nodes[n].keys()
        for k in list( to_delete ):
            if k != 'tag':
                del g2.nodes[n][k]

    for e in g2.edges:
        if 'label' in g2.edges[e]:
            tag = g2.edges[e]['label']
            if tag[0] == '"':
                tag = tag[1:-1]
            if tag in unique_strings:
                tag = unique_strings[tag]
            else:
                unique_strings[tag] = tag    
            g2.edges[e]['tag'] = tag
            del g2.edges[e]['label']
            

    to_delete = g2.graph.keys()
    for k in list( to_delete ):
        del g2.graph[k]

    return nx.disjoint_union( g, g2 )
    
def add_multiline_input_to_graph( f, g ):
    if not nx.is_directed( g ):
        raise Exception( "Multiline input graph must be directed." )
        
    input_node = 1
    
    g.add_node( "INPUT", tag="input" )
    last_line = "INPUT"
    
    def next_node():
        nonlocal input_node
        label =  "INPUT" + str( input_node )
        input_node += 1
        return label
    
    for line in f:
        curr_line = next_node()
        
        g.add_node( curr_line, tag="line" )
        g.add_edge( last_line, curr_line, tag="next_line" )
        
        last_char = curr_line
        for char in line:
            # Don't include newlines
            if char == "\n":
                break

            curr_char = next_node()
            g.add_node( curr_char, tag=char )
            g.add_edge( last_char, curr_char, tag="next_char" )
            last_char = curr_char
            
        g.add_edge( last_char, curr_line, tag="end_of_line" )
        last_line = curr_line

    end_node = next_node()
    g.add_node( end_node, tag="end_of_input" )
    g.add_edge( last_line, end_node, tag="end_of_input" )

    return g
            
        
    
    
