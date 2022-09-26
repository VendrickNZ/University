from mimetypes import knownfiles
import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def forward_deduce(kb):
    knowledge_base = list(clauses(kb))
    c = set()
    total_size = 0
    checking = True
    all_body_in_c = True

    while checking:
        for clause in knowledge_base:
            if len(clause[1]) == 0:
                if clause[0] not in c:
                    c.add(clause[0])
            else:
                all_body_in_c = True
                for i in range(len(clause[1])):
                    #print(clause[0], clause[1][i], c, clause[0] in c, clause[1][i] in c)
                    if clause[0] in c or clause[1][i] not in c:
                        all_body_in_c = False
                if all_body_in_c:
                    c.add(clause[0])
        total_size += 1
        if total_size > len(c):
            checking = False
    return c


kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

print(", ".join(sorted(forward_deduce(kb))))


kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))



kb = ""
print(", ".join(sorted(forward_deduce(kb))))


kb = """
a.
z.
"""
print(", ".join(sorted(forward_deduce(kb))))

kb = """
wet :- is_raining.
wet :- sprinkler_is_going.
wet.
"""

print(len(forward_deduce(kb)))