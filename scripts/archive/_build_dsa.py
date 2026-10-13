import json, pathlib

root = pathlib.Path('/home/user/studyfeed')
cards = json.loads((root / 'src/lib/data/cards.json').read_text())

subs = {
 'CSCA411-M1-01': [('Data item and field','A single value is a data item; a field is one named place that stores a value inside a record.'),('Record and file','A record groups related items about one entity; a file is a collection of similar records.'),('Primitive and non-primitive structures','Primitive structures hold single values such as int or char, while non-primitive structures are built from them, such as arrays and lists.'),('Linear and non-linear structures','Linear structures arrange elements in a sequence, while non-linear structures such as trees and graphs arrange them in levels or networks.'),('Static and dynamic structures','Static structures have a fixed size decided at compile time; dynamic structures grow and shrink at run time.'),('Operations on data structures','Insertion, deletion, traversal, searching, sorting and merging are the standard operations performed on any structure.')],
 'CSCA411-M1-02': [('Finiteness','The algorithm must end after a limited number of steps.'),('Definiteness','Every step must be unambiguous and precisely stated.'),('Input and output','Zero or more inputs are supplied and at least one output is produced.'),('Effectiveness','Each step must be basic enough to be carried out in finite time.')],
 'CSCA411-M1-03': [('Keywords used in pseudocode','READ, PRINT, IF-ELSE, WHILE, FOR, REPEAT and RETURN express control flow in plain words.'),('Rules for writing pseudocode','One statement per line, indentation for nesting and no dependence on the syntax of any language.'),('Algorithm versus flowchart versus program','A flowchart uses symbols, pseudocode uses words and a program uses a real language - all three describe the same logic.')],
 'CSCA411-M1-04': [('Basic operation count','Count the operation that dominates, such as comparisons in a search or multiplications in a matrix product.'),('Growth rate','The way the operation count increases as n increases: constant, logarithmic, linear, quadratic or exponential.'),('Asymptotic analysis for large n','Constants and lower order terms are ignored because only the trend for large inputs matters.')],
 'CSCA411-M1-05': [('Fixed part','Memory for the program code, constants and simple variables that does not depend on the input size.'),('Variable part','Memory for the data structures whose size depends on the input, such as arrays or recursion frames.'),('Auxiliary space','Extra working memory used beyond the input itself, which is what "in-place" algorithms try to minimise.')],
 'CSCA411-M1-06': [('Best case','The input arrangement for which the algorithm finishes fastest, such as finding the target at the first position.'),('Average case','The expected cost over typical inputs, often calculated with probability assumptions.'),('Worst case','The input arrangement that forces the maximum work; it is the guarantee reported in most analyses.'),('Why the worst case is reported','It gives an upper limit that holds for every input, so it is the safest measure of performance.')],
 'CSCA411-M1-07': [('Definition of the upper bound','f(n) = O(g(n)) means f grows no faster than g times some constant for all sufficiently large n.'),('Dropping constants and lower terms','3n squared + 5n + 9 becomes O(n squared), because the highest order term decides the trend.'),('Common growth rates in increasing order','O(1) < O(log n) < O(n) < O(n log n) < O(n squared) < O(2 to the n).')],
 'CSCA411-M1-08': [('Omega notation (lower bound)','f(n) = Omega(g(n)) means f grows at least as fast as g, so g is the floor of the growth.'),('Theta notation (tight bound)','f(n) = Theta(g(n)) means f is bounded both above and below by g, so the growth rate is exact.'),('Roof, floor and room','Big-O is the roof, Omega is the floor and Theta is a room of exactly that size.')],
 'CSCA411-M1-09': [('One dimensional array','A single list of elements reached by one index, stored in consecutive memory locations.'),('Multidimensional array','A table-like array with two or more indices, such as a matrix with rows and columns.'),('Address calculation in row major and column major order','Row major stores a row at a time so address = base + (i * columns + j) * size; column major stores a column at a time.'),('Operations on arrays','Traversal, insertion, deletion, searching and sorting, where insertion and deletion need shifting.'),('Advantages and limitations','Constant time access by index is the advantage; fixed size and costly middle insertion are the limitations.')],
 'CSCA411-M1-10': [('Linear search','Compares the target with each element in turn; works on unsorted data and costs O(n).'),('Binary search','Repeatedly halves a sorted array; costs O(log n) but requires sorted input.'),('Complexity comparison','For a lakh records linear search may need a lakh comparisons while binary search needs about 17.'),('Which search to use','Use linear search for small or unsorted data and binary search for large sorted data.')]
}

def node_from_card(c, module):
    topic = {
        'id': c['id'],
        'title': c['topic'],
        'kind': 'topic',
        'definition': c['definition'],
        'children': [
            {'id': f"{c['id']}-s{i+1}", 'title': t, 'kind': 'subtopic', 'definition': d}
            for i, (t, d) in enumerate(subs.get(c['id'], []))
        ],
        'card': {
            'explanation': c['explanation'],
            'example': c['example'],
            'quiz': c['quiz'],
            'examTip': c['examTip'],
            'verified': c['verified']
        }
    }
    return topic

m1 = [node_from_card(c, 'I') for c in cards if c['module'] == 'I']
m1.sort(key=lambda t: t['id'])

m2m3 = json.loads((root / 'scripts/_dsa_m2m3.json').read_text())
m4m5 = json.loads((root / 'scripts/_dsa_m4m5.json').read_text())

doc = {
    'code': 'CSCA 411',
    'subject': 'Data Structures and Algorithms',
    'semester': 1,
    'modules': [
        {'module': 'I', 'title': 'Foundations: Data Structures, Algorithms and Arrays',
         'topics': m1},
        *m2m3,
        *m4m5
    ]
}

out = root / 'src/lib/data/tree/CSCA411.json'
out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
print('wrote', out, out.stat().st_size, 'bytes')
