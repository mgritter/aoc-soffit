import sys
import aoc.input as input
import networkx as nx
import traceback
import os.path

from soffit.display import drawSvg
import soffit.application as soffit
import time

def has_edge( g, n, edge_tag ):
    for i,j,t in g.out_edges( n, 'tag' ):
        if t == edge_tag:
            return j
    return None

def make_video( iteration, g ):
    return

    g = g.copy()
    for n,t in g.nodes.data( 'tag' ):
        if t == 'cursor':
            g.nodes[n]['color'] = 'red'
    drawSvg( g, "aoc{:03d}.svg".format( iteration ),
             program="dot" )

class StepReport(object):
    def __init__( self, id, grammar ):
        self.id = id
        self.grammar = grammar

    def start( self ):
        self.start_time = time.monotonic()

    def stop( self, num_iter ):
        self.end_time = time.monotonic()
        self.num_iterations = num_iter

    def show( self ):
        print( "{:3d} {:20} {:6d} {:6.1f}s".format(
            self.id, self.grammar,
            self.num_iterations,
            self.end_time - self.start_time ) )
        
def execute_run_graph( g, path, verbose=True, outputdir="." ):
    start = [ n for n,t in g.nodes.data( 'tag' ) if t == "start" ]
    if len( start ) == 0:
        raise Exception( "No start node found." )
    if len( start ) > 1:
        raise Exception( "More than one start node." )

    drawSvg( g,
             os.path.join( outputdir, "execution-plan.svg"),
             program="dot" )
    
    curr = start[0]
    working_graph = None
    step_count = 1
    step_reports = []
    
    while True:
        g_n = has_edge( g, curr, 'grammar' )
        grammar = None
        if g_n is not None:
            grammar_name = g.nodes[g_n]['tag']
            if verbose:
                print( "Executing grammar", grammar_name )

            grammar = soffit.loadGrammar( os.path.join( path, grammar_name ) )
            if verbose:
                print( "Grammar has", len( grammar.rules), "rules." )
            if working_graph is None:
                working_graph = grammar.start.to_directed()
            
            i_n = has_edge( g, curr, 'input' )
            if i_n is not None:
                if verbose:
                    print( "Loading input type", g.nodes[i_n]['tag'] )
                if g.nodes[i_n]['tag'] == 'multiline':
                    with open( sys.argv[2], "r" ) as f:
                        input.add_multiline_input_to_graph( f, working_graph )
                elif g.nodes[i_n]['tag'] == 'text':
                    with open( sys.argv[2], "r" ) as f:
                        input.add_input_to_graph( f, working_graph )

            curr_step = StepReport( step_count, grammar_name )
            step_count += 1
            step_reports.append( curr_step )
            curr_step.start()
            
            a = soffit.ApplicationState(
                initialGraph = working_graph,
                grammar = grammar,
                callback = make_video
            )
            a.verbose = verbose
            if verbose:
                print( "Running grammar" )
            try:
                a.run( 1000000 )
                curr_step.stop( a.iteration )
                drawSvg( a.graph,
                         os.path.join( outputdir, "after-step-{}.svg".format( curr_step.id ) ),
                         program="neato",
                         dotFile=os.path.join( outputdir, "after-step-{}.dot".format( curr_step.id ) ) )
            except KeyboardInterrupt:
                print( "Interupted!" )
                return a.graph
            
            working_graph = a.graph
        else:
            raise Exception( "No grammar found." )

        n_n = has_edge( g, curr, "next" )
        if n_n is None:
            break

        curr = n_n

    print( "-" * 80 )

    print( "{:3} {:20} {:6} {:6}".format( "", "Grammar", "Steps", "Time" ) ) 
    for s in step_reports:
        s.show()
        
    return working_graph    

def show_output_as_string( g ):
    outputs = [ n for n,t in g.nodes.data( 'tag' ) if t == 'output' ]
    header = False
    for o in outputs:
        line = has_edge( g, o, 'output' )        
        while line is not None:
            text = []
            curr = has_edge( g, line, 'next_char' )
            while curr is not None:
                text.append( g.nodes[curr]['tag'] )
                curr = has_edge( g, curr, 'next_char' )
            if not header:
                print( "-" * 80 )
                header = True                
            print( "".join( text ) )
            line = has_edge( g, line, 'next_line' )
    
def main():
    if len( sys.argv ) < 3:
        print( "Usage: python -m aoc.main <rungraph> <input> [<outputdir>]" )
        return

    outputdir = "."
    if len( sys.argv ) >= 4:
        outputdir = sys.argv[3]
        
    grammar = soffit.loadGrammar( sys.argv[1] )
    try:
        g = execute_run_graph( grammar.start,
                               os.path.dirname( sys.argv[1] ),
                               outputdir = outputdir)

        drawSvg( g,
                 os.path.join( outputdir, "aoc.svg" ),
                 program="dot",
                 dotFile=os.path.join( outputdir, "aoc.dot" ) )

        show_output_as_string( g )        
    except Exception as e:
        traceback.print_exc()
        

if __name__ == "__main__":
    main()

