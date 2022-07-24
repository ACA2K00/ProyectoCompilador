
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSINT FLOAT PRINT NAME INUM FNUMinit : statementstatement : declarations statement\n                 | print statement\n                 | emptyempty :type : INT\n            | FLOATdeclarations  : declaration_type_name\n                     | declaration_assign_expression\n                     | declaration_fulldeclaration_type_name : type NAMEdeclaration_assign_expression : NAME "=" expressiondeclaration_full : type NAME "=" expressionprint : PRINT expressionexpression : expression "+" expression\n                  | expression "-" expression\n                  | expression "*" expression\n                  | expression "/" expressionexpression : "-" expression %prec UMINUSexpression : "(" expression ")"expression : INUM\n                  | FNUMexpression : NAME'
    
_lr_action_items = {'PRINT':([0,3,4,6,7,8,16,19,20,21,22,28,31,32,33,34,35,36,37,],[9,9,9,-8,-9,-10,-14,-21,-22,-23,-11,-19,-12,-15,-16,-17,-18,-20,-13,]),'$end':([0,1,2,3,4,5,6,7,8,14,15,16,19,20,21,22,28,31,32,33,34,35,36,37,],[-5,0,-1,-5,-5,-4,-8,-9,-10,-2,-3,-14,-21,-22,-23,-11,-19,-12,-15,-16,-17,-18,-20,-13,]),'NAME':([0,3,4,6,7,8,9,10,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,],[11,11,11,-8,-9,-10,21,22,-6,-7,-14,21,21,-21,-22,-23,-11,21,21,21,21,21,-19,21,-12,-15,-16,-17,-18,-20,-13,]),'INT':([0,3,4,6,7,8,16,19,20,21,22,28,31,32,33,34,35,36,37,],[12,12,12,-8,-9,-10,-14,-21,-22,-23,-11,-19,-12,-15,-16,-17,-18,-20,-13,]),'FLOAT':([0,3,4,6,7,8,16,19,20,21,22,28,31,32,33,34,35,36,37,],[13,13,13,-8,-9,-10,-14,-21,-22,-23,-11,-19,-12,-15,-16,-17,-18,-20,-13,]),'-':([9,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[17,25,17,17,-21,-22,-23,17,17,17,17,17,-19,25,17,25,-15,-16,-17,-18,-20,25,]),'(':([9,17,18,23,24,25,26,27,30,],[18,18,18,18,18,18,18,18,18,]),'INUM':([9,17,18,23,24,25,26,27,30,],[19,19,19,19,19,19,19,19,19,]),'FNUM':([9,17,18,23,24,25,26,27,30,],[20,20,20,20,20,20,20,20,20,]),'=':([11,22,],[23,30,]),'+':([16,19,20,21,28,29,31,32,33,34,35,36,37,],[24,-21,-22,-23,-19,24,24,-15,-16,-17,-18,-20,24,]),'*':([16,19,20,21,28,29,31,32,33,34,35,36,37,],[26,-21,-22,-23,-19,26,26,26,26,-17,-18,-20,26,]),'/':([16,19,20,21,28,29,31,32,33,34,35,36,37,],[27,-21,-22,-23,-19,27,27,27,27,-17,-18,-20,27,]),')':([19,20,21,28,29,32,33,34,35,36,],[-21,-22,-23,-19,36,-15,-16,-17,-18,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'statement':([0,3,4,],[2,14,15,]),'declarations':([0,3,4,],[3,3,3,]),'print':([0,3,4,],[4,4,4,]),'empty':([0,3,4,],[5,5,5,]),'declaration_type_name':([0,3,4,],[6,6,6,]),'declaration_assign_expression':([0,3,4,],[7,7,7,]),'declaration_full':([0,3,4,],[8,8,8,]),'type':([0,3,4,],[10,10,10,]),'expression':([9,17,18,23,24,25,26,27,30,],[16,28,29,31,32,33,34,35,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> statement','init',1,'p_init','ly_calc.py',57),
  ('statement -> declarations statement','statement',2,'p_statement','ly_calc.py',63),
  ('statement -> print statement','statement',2,'p_statement','ly_calc.py',64),
  ('statement -> empty','statement',1,'p_statement','ly_calc.py',65),
  ('empty -> <empty>','empty',0,'p_empty','ly_calc.py',73),
  ('type -> INT','type',1,'p_type_specifier','ly_calc.py',77),
  ('type -> FLOAT','type',1,'p_type_specifier','ly_calc.py',78),
  ('declarations -> declaration_type_name','declarations',1,'p_declarations','ly_calc.py',83),
  ('declarations -> declaration_assign_expression','declarations',1,'p_declarations','ly_calc.py',84),
  ('declarations -> declaration_full','declarations',1,'p_declarations','ly_calc.py',85),
  ('declaration_type_name -> type NAME','declaration_type_name',2,'p_declaration_type_name','ly_calc.py',89),
  ('declaration_assign_expression -> NAME = expression','declaration_assign_expression',3,'p_declaration_assign_expression','ly_calc.py',94),
  ('declaration_full -> type NAME = expression','declaration_full',4,'p_declaration_full','ly_calc.py',98),
  ('print -> PRINT expression','print',2,'p_print','ly_calc.py',102),
  ('expression -> expression + expression','expression',3,'p_unary_operator','ly_calc.py',107),
  ('expression -> expression - expression','expression',3,'p_unary_operator','ly_calc.py',108),
  ('expression -> expression * expression','expression',3,'p_unary_operator','ly_calc.py',109),
  ('expression -> expression / expression','expression',3,'p_unary_operator','ly_calc.py',110),
  ('expression -> - expression','expression',2,'p_expression_uminus','ly_calc.py',114),
  ('expression -> ( expression )','expression',3,'p_direct_declarator','ly_calc.py',119),
  ('expression -> INUM','expression',1,'p_expression_number','ly_calc.py',124),
  ('expression -> FNUM','expression',1,'p_expression_number','ly_calc.py',125),
  ('expression -> NAME','expression',1,'p_expression_name','ly_calc.py',129),
]
