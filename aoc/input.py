import networkx as nx
 
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
            
        
    
    
