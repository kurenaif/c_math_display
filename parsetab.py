
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'E5080439A5D84E59E01937A3B1BDC6D8'
    
_lr_action_items = {'LPAREN':([0,1,8,9,10,11,12,],[1,1,1,1,1,1,1,]),'TIMES':([2,4,5,6,13,14,15,17,18,19,],[-6,-8,-7,12,-9,12,12,-5,-4,-10,]),'$end':([2,3,4,5,6,13,14,15,17,18,19,],[-6,0,-8,-7,-3,-9,-1,-2,-5,-4,-10,]),'LBRACKET':([4,],[10,]),'VARIABLE':([0,1,8,9,10,11,12,],[4,4,4,4,4,4,4,]),'RPAREN':([2,4,5,6,7,13,14,15,17,18,19,],[-6,-8,-7,-3,13,-9,-1,-2,-5,-4,-10,]),'NUMBER':([0,1,8,9,10,11,12,],[5,5,5,5,5,5,5,]),'MINUS':([2,3,4,5,6,7,13,14,15,16,17,18,19,],[-6,9,-8,-7,-3,9,-9,-1,-2,9,-5,-4,-10,]),'PLUS':([2,3,4,5,6,7,13,14,15,16,17,18,19,],[-6,8,-8,-7,-3,8,-9,-1,-2,8,-5,-4,-10,]),'DIVIDE':([2,4,5,6,13,14,15,17,18,19,],[-6,-8,-7,11,-9,11,11,-5,-4,-10,]),'RBRACKET':([2,4,5,6,13,14,15,16,17,18,19,],[-6,-8,-7,-3,-9,-1,-2,19,-5,-4,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'factor':([0,1,8,9,10,11,12,],[2,2,2,2,2,17,18,]),'expression':([0,1,10,],[3,7,16,]),'term':([0,1,8,9,10,],[6,6,14,15,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','yacc.py',9),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','yacc.py',13),
  ('expression -> term','expression',1,'p_expression_term','yacc.py',17),
  ('term -> term TIMES factor','term',3,'p_term_times','yacc.py',21),
  ('term -> term DIVIDE factor','term',3,'p_term_div','yacc.py',25),
  ('term -> factor','term',1,'p_term_factor','yacc.py',29),
  ('factor -> NUMBER','factor',1,'p_factor_num','yacc.py',33),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','yacc.py',37),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_param','yacc.py',41),
  ('factor -> VARIABLE LBRACKET expression RBRACKET','factor',4,'p_factor_array','yacc.py',45),
]
