import sys
import aoc.input as input
import networkx as nx
import traceback
import os.path

from soffit.display import drawSvg
import soffit.application as soffit

def has_edge( g, n, edge_tag ):
    for i,j,t in g.out_edges( n, 'tag' ):
        if t == edge_tag:
            return j
    return None

def make_video( iteration, g ):
    g = g.copy()
    for n,t in g.nodes.data( 'tag' ):
        if t == 'cursor':
            g.nodes[n]['color'] = 'red'
    drawSvg( g, "aoc{:03d}.svg".format( iteration ),
             program="dot" )
    
def execute_run_graph( g, path, verbose=True ):
    start = [ n for n,t in g.nodes.data( 'tag' ) if t == "start" ]
    if len( start ) == 0:
        raise Exception( "No start node found." )
    if len( start ) > 1:
        raise Exception( "More than one start node." )
    
    curr = start[0]
    working_graph = None
    
    while True:
        g_n = has_edge( g, curr, 'grammar' )
        grammar = None
        if g_n is not None:
            if verbose:
                print( "Loading grammar", g.nodes[g_n]['tag'] )
            # FIXME: interpret relative to main
            grammar = soffit.loadGrammar( os.path.join( path, g.nodes[g_n]['tag'] ) )
            if working_graph is None:
                working_graph = grammar.start.to_directed()
            
            i_n = has_edge( g, curr, 'input' )
            if i_n is not None:
                if verbose:
                    print( "Loading input type", g.nodes[i_n]['tag'] )
                if g.nodes[i_n]['tag'] == 'multiline':
                    with open( sys.argv[2], "r" ) as f:
                        input.add_multiline_input_to_graph( f, working_graph )

            a = soffit.ApplicationState(
                initialGraph = working_graph,
                grammar = grammar,
                callback = make_video
            )
            a.verbose = verbose
            if verbose:
                print( "Running grammar" )                
            a.run( 1000 )
            working_graph = a.graph
        else:
            raise Exception( "No grammar found." )

        n_n = has_edge( g, curr, "next" )
        if n_n is None:
            break

        curr = n_n
        
    return working_graph    

def main():
    if len( sys.argv ) < 3:
        print( "Usage: python -m aoc.main <rungraph> <input>" )
        return

    grammar = soffit.loadGrammar( sys.argv[1] )
    try:
        g = execute_run_graph( grammar.start, os.path.dirname( sys.argv[1] ) )

        drawSvg( g, "aoc.svg",
                 program="dot",
                 dotFile="aoc.dot" )
    except Exception as e:
        traceback.print_exc()
        

if __name__ == "__main__":
    main()

