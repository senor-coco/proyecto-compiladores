
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'instruccionesALL ALTER AND AS ASC AVG BEGIN BIGINT BIGSERIAL BIT BOOL BOOLEAN BOX BY BYTEA CADENA CHAR CHARACTER CHECK CIDR CIRCLE COMA COMMIT CONSTRAINT COUNT CREATE DATABASE DATE DECIMAL DEFAULT DELETE DESC DIFERENTE DISTINCT DIVISION DOS_PUNTOS DOUBLE_PRECISION DROP END FLOAT4 FLOAT8 FOREIGN FROM FUNCTION GRANT GROUP HAVING IDENTIFICADOR IGUAL IN INDEX INET INSERT INT INT2 INT4 INT8 INTEGER INTERVAL INTO IS JOIN KEY LIMIT LINE LSEG MACADDR MAS MAX MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MIN MODULO MONEY MULTIPLICACION NOT NULL NUMERIC NUMERO OFFSET ON OR ORDER PARDER PARIZQ PATH POINT POLYGON PRIMARY PROCEDURE PUNTO PUNTOCOMA REAL REFERENCES REVOKE ROLLBACK SELECT SERIAL SERIAL4 SERIAL8 SET SMALLINT SUM TABLE TEXT TIME TIMESTAMP TIMESTAMPTZ TIMETZ TRIGGER UNION UNIQUE UPDATE USE VALUES VARBIT VARCHAR VARYING VIEW WHEREinstrucciones : instrucciones instruccion\n                     | instruccioninstruccion : crear_db\n                   | usar_db\n                   | crear_tabla\n                   | eliminar_tabla\n                   | insertar_datos\n                   | consulta_datos\n                   | modificar_datos\n                   | eliminar_datos\n                   | transaccioncrear_db : CREATE DATABASE IDENTIFICADOR PUNTOCOMAusar_db : USE IDENTIFICADOR PUNTOCOMAcrear_tabla : CREATE TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ definiciones PARDER PUNTOCOMAeliminar_tabla : DROP TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMAdefiniciones : definiciones COMA definicion\n                    | definiciondefinicion : columna\n                  | primary_key\n                  | foreign_keycolumna : IDENTIFICADOR tipos_datos atributosprimary_key : PRIMARY KEY PARIZQ IDENTIFICADOR PARDERforeign_key : FOREIGN KEY PARIZQ IDENTIFICADOR PARDER REFERENCES IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ IDENTIFICADOR PARDERtipos_datos : BIGINT\n                   | INTEGER\n                   | DECIMAL\n                   | CHARACTER VARYING PARIZQ NUMERO PARDER\n                   | CHARACTER VARYING\n                   | CHAR\n                   | VARCHAR PARIZQ NUMERO PARDER\n                   | TEXTatributos : NOT NULL\n                 | NULL\n                 | insertar_datos : INSERT INTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ identificadores PARDER VALUES listas_valores PUNTOCOMAlistas_valores : listas_valores COMA PARIZQ valores PARDER\n                      | PARIZQ valores PARDERidentificadores : identificadores COMA IDENTIFICADOR\n                       | IDENTIFICADORvalores : valores COMA valor\n               | valorvalor : NUMERO\n             | CADENA\n             | expresionconsulta_datos : SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR joins group_by having order_by limit PUNTOCOMA\n                      | SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMAseleccion : seleccion COMA IDENTIFICADOR\n                 | IDENTIFICADOR\n                 | agregacionjoins : joins join\n             | joinjoin : JOIN IDENTIFICADOR PUNTO IDENTIFICADOR ON IDENTIFICADOR operador IDENTIFICADORagregacion : SUM PARIZQ IDENTIFICADOR PARDER\n                  | COUNT PARIZQ IDENTIFICADOR PARDER\n                  | AVG PARIZQ IDENTIFICADOR PARDER\n                  | MAX PARIZQ IDENTIFICADOR PARDER\n                  | MIN PARIZQ IDENTIFICADOR PARDERgroup_by : GROUP BY IDENTIFICADOR\n                | having : HAVING condicion\n              | order_by : ORDER BY IDENTIFICADOR\n                | ORDER BY IDENTIFICADOR ASC\n                | ORDER BY IDENTIFICADOR DESC\n                | limit : LIMIT NUMERO\n             | modificar_datos : UPDATE IDENTIFICADOR PUNTO IDENTIFICADOR SET asignaciones WHERE condiciones PUNTOCOMAasignaciones : asignaciones COMA asignacion\n                    | asignacionasignacion : IDENTIFICADOR IGUAL valoreliminar_datos : DELETE FROM IDENTIFICADOR PUNTO IDENTIFICADOR WHERE condiciones PUNTOCOMAcondiciones : condiciones operador_logico condicion\n                   | condicioncondicion : IDENTIFICADOR operador valor\n                 | IDENTIFICADOR operador PARIZQ consulta_datos PARDERoperador_logico : AND\n                       | ORoperador : IGUAL\n                | DIFERENTE\n                | MAYORQUE\n                | MENORQUE\n                | MAYORIGUAL\n                | MENORIGUALexpresion : valor MAS valor\n                 | valor MENOS valor\n                 | valor MULTIPLICACION valor\n                 | valor DIVISION valortransaccion : BEGIN PUNTOCOMA\n                   | COMMIT PUNTOCOMA\n                   | ROLLBACK PUNTOCOMA'
    
_lr_action_items = {'CREATE':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[12,12,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'USE':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[13,13,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'DROP':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[14,14,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'INSERT':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[15,15,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'SELECT':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,163,188,200,],[16,16,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,16,-35,-45,]),'UPDATE':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[17,17,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'DELETE':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[18,18,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'BEGIN':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[19,19,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'COMMIT':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[20,20,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'ROLLBACK':([0,1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[21,21,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,22,38,39,40,43,55,80,98,138,147,161,188,200,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,-89,-90,-91,-13,-12,-15,-46,-72,-14,-68,-35,-45,]),'DATABASE':([12,],[23,]),'TABLE':([12,14,],[24,26,]),'IDENTIFICADOR':([13,16,17,23,24,26,27,37,46,47,48,49,50,51,52,53,56,57,58,67,71,77,79,81,86,100,102,103,116,120,132,133,134,135,136,137,139,140,141,149,150,154,155,156,192,193,196,209,210,214,],[25,29,36,41,42,44,45,54,59,60,61,62,63,64,65,66,68,69,70,78,82,83,87,95,104,124,104,83,87,152,-79,-80,-81,-82,-83,-84,104,-77,-78,168,169,104,175,176,202,203,204,212,213,215,]),'INTO':([15,],[27,]),'SUM':([16,],[31,]),'COUNT':([16,],[32,]),'AVG':([16,],[33,]),'MAX':([16,],[34,]),'MIN':([16,],[35,]),'FROM':([18,28,29,30,60,72,73,74,75,76,],[37,46,-48,-49,-47,-53,-54,-55,-56,-57,]),'PUNTOCOMA':([19,20,21,25,41,69,82,97,99,105,106,115,121,122,126,127,128,129,153,162,164,171,172,174,175,177,178,179,180,190,194,197,201,202,207,208,211,212,],[38,39,40,43,55,80,98,-59,-51,138,-74,147,-61,-50,-42,-43,-44,161,-65,-75,-73,188,-67,-60,-58,-85,-86,-87,-88,200,-76,-37,-66,-62,-63,-64,-36,-52,]),'COMA':([28,29,30,60,72,73,74,75,76,84,85,88,89,90,91,92,95,96,107,108,109,110,112,114,125,126,127,128,130,142,144,145,148,152,165,171,177,178,179,180,183,184,186,187,195,197,205,206,211,216,],[47,-48,-49,-47,-53,-54,-55,-56,-57,103,-70,116,-17,-18,-19,-20,-39,120,-34,-24,-25,-26,-29,-31,-71,-42,-43,-44,-69,-21,-33,-28,-16,-38,-32,189,-85,-86,-87,-88,-30,-22,198,-41,-27,-37,-40,198,-36,-23,]),'PARIZQ':([31,32,33,34,35,68,70,113,117,118,131,132,133,134,135,136,137,145,151,189,213,],[48,49,50,51,52,79,81,146,149,150,163,-79,-80,-81,-82,-83,-84,166,170,199,214,]),'PUNTO':([36,42,44,45,54,59,124,204,],[53,56,57,58,67,71,156,210,]),'PARDER':([61,62,63,64,65,88,89,90,91,92,95,96,98,107,108,109,110,112,114,126,127,128,142,144,145,148,152,165,167,168,169,177,178,179,180,181,182,183,184,186,187,195,200,205,206,215,216,],[72,73,74,75,76,115,-17,-18,-19,-20,-39,119,-46,-34,-24,-25,-26,-29,-31,-42,-43,-44,-21,-33,-28,-16,-38,-32,183,184,185,-85,-86,-87,-88,194,195,-30,-22,197,-41,-27,-45,-40,211,216,-23,]),'SET':([66,],[77,]),'WHERE':([78,84,85,125,126,127,128,130,177,178,179,180,],[86,102,-70,-71,-42,-43,-44,-69,-85,-86,-87,-88,]),'PRIMARY':([79,116,],[93,93,]),'FOREIGN':([79,116,],[94,94,]),'JOIN':([82,97,99,122,212,],[100,100,-51,-50,-52,]),'IGUAL':([83,104,203,],[101,132,132,]),'BIGINT':([87,],[108,]),'INTEGER':([87,],[109,]),'DECIMAL':([87,],[110,]),'CHARACTER':([87,],[111,]),'CHAR':([87,],[112,]),'VARCHAR':([87,],[113,]),'TEXT':([87,],[114,]),'KEY':([93,94,],[117,118,]),'GROUP':([97,99,122,212,],[123,-51,-50,-52,]),'HAVING':([97,99,121,122,175,212,],[-59,-51,154,-50,-58,-52,]),'ORDER':([97,99,121,122,126,127,128,153,162,174,175,177,178,179,180,194,212,],[-59,-51,-61,-50,-42,-43,-44,173,-75,-60,-58,-85,-86,-87,-88,-76,-52,]),'LIMIT':([97,99,121,122,126,127,128,153,162,172,174,175,177,178,179,180,194,202,207,208,212,],[-59,-51,-61,-50,-42,-43,-44,-65,-75,191,-60,-58,-85,-86,-87,-88,-76,-62,-63,-64,-52,]),'NUMERO':([101,131,132,133,134,135,136,137,146,157,158,159,160,166,170,191,198,199,],[126,126,-79,-80,-81,-82,-83,-84,167,126,126,126,126,182,126,201,126,126,]),'CADENA':([101,131,132,133,134,135,136,137,157,158,159,160,170,198,199,],[127,127,-79,-80,-81,-82,-83,-84,127,127,127,127,127,127,127,]),'DIFERENTE':([104,203,],[133,133,]),'MAYORQUE':([104,203,],[134,134,]),'MENORQUE':([104,203,],[135,135,]),'MAYORIGUAL':([104,203,],[136,136,]),'MENORIGUAL':([104,203,],[137,137,]),'AND':([105,106,126,127,128,129,162,164,177,178,179,180,194,],[140,-74,-42,-43,-44,140,-75,-73,-85,-86,-87,-88,-76,]),'OR':([105,106,126,127,128,129,162,164,177,178,179,180,194,],[141,-74,-42,-43,-44,141,-75,-73,-85,-86,-87,-88,-76,]),'NOT':([107,108,109,110,112,114,145,183,195,],[143,-24,-25,-26,-29,-31,-28,-30,-27,]),'NULL':([107,108,109,110,112,114,143,145,183,195,],[144,-24,-25,-26,-29,-31,165,-28,-30,-27,]),'VARYING':([111,],[145,]),'VALUES':([119,],[151,]),'BY':([123,173,],[155,192,]),'MAS':([125,126,127,128,162,177,178,179,180,187,205,],[157,-42,-43,-44,157,157,157,157,157,157,157,]),'MENOS':([125,126,127,128,162,177,178,179,180,187,205,],[158,-42,-43,-44,158,158,158,158,158,158,158,]),'MULTIPLICACION':([125,126,127,128,162,177,178,179,180,187,205,],[159,-42,-43,-44,159,159,159,159,159,159,159,]),'DIVISION':([125,126,127,128,162,177,178,179,180,187,205,],[160,-42,-43,-44,160,160,160,160,160,160,160,]),'ON':([176,],[193,]),'REFERENCES':([185,],[196,]),'ASC':([202,],[207,]),'DESC':([202,],[208,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'instruccion':([0,1,],[2,22,]),'crear_db':([0,1,],[3,3,]),'usar_db':([0,1,],[4,4,]),'crear_tabla':([0,1,],[5,5,]),'eliminar_tabla':([0,1,],[6,6,]),'insertar_datos':([0,1,],[7,7,]),'consulta_datos':([0,1,163,],[8,8,181,]),'modificar_datos':([0,1,],[9,9,]),'eliminar_datos':([0,1,],[10,10,]),'transaccion':([0,1,],[11,11,]),'seleccion':([16,],[28,]),'agregacion':([16,],[30,]),'asignaciones':([77,],[84,]),'asignacion':([77,103,],[85,130,]),'definiciones':([79,],[88,]),'definicion':([79,116,],[89,148,]),'columna':([79,116,],[90,90,]),'primary_key':([79,116,],[91,91,]),'foreign_key':([79,116,],[92,92,]),'identificadores':([81,],[96,]),'joins':([82,],[97,]),'join':([82,97,],[99,122,]),'condiciones':([86,102,],[105,129,]),'condicion':([86,102,139,154,],[106,106,164,174,]),'tipos_datos':([87,],[107,]),'group_by':([97,],[121,]),'valor':([101,131,157,158,159,160,170,198,199,],[125,162,177,178,179,180,187,205,187,]),'expresion':([101,131,157,158,159,160,170,198,199,],[128,128,128,128,128,128,128,128,128,]),'operador':([104,203,],[131,209,]),'operador_logico':([105,129,],[139,139,]),'atributos':([107,],[142,]),'having':([121,],[153,]),'listas_valores':([151,],[171,]),'order_by':([153,],[172,]),'valores':([170,199,],[186,206,]),'limit':([172,],[190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','parser.py',13),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','parser.py',14),
  ('instruccion -> crear_db','instruccion',1,'p_instruccion','parser.py',21),
  ('instruccion -> usar_db','instruccion',1,'p_instruccion','parser.py',22),
  ('instruccion -> crear_tabla','instruccion',1,'p_instruccion','parser.py',23),
  ('instruccion -> eliminar_tabla','instruccion',1,'p_instruccion','parser.py',24),
  ('instruccion -> insertar_datos','instruccion',1,'p_instruccion','parser.py',25),
  ('instruccion -> consulta_datos','instruccion',1,'p_instruccion','parser.py',26),
  ('instruccion -> modificar_datos','instruccion',1,'p_instruccion','parser.py',27),
  ('instruccion -> eliminar_datos','instruccion',1,'p_instruccion','parser.py',28),
  ('instruccion -> transaccion','instruccion',1,'p_instruccion','parser.py',29),
  ('crear_db -> CREATE DATABASE IDENTIFICADOR PUNTOCOMA','crear_db',4,'p_crear_db','parser.py',35),
  ('usar_db -> USE IDENTIFICADOR PUNTOCOMA','usar_db',3,'p_usar_db','parser.py',40),
  ('crear_tabla -> CREATE TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ definiciones PARDER PUNTOCOMA','crear_tabla',9,'p_crear_tabla','parser.py',45),
  ('eliminar_tabla -> DROP TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMA','eliminar_tabla',6,'p_eliminar_tabla','parser.py',50),
  ('definiciones -> definiciones COMA definicion','definiciones',3,'p_definiciones_lista','parser.py',55),
  ('definiciones -> definicion','definiciones',1,'p_definiciones_lista','parser.py',56),
  ('definicion -> columna','definicion',1,'p_definicion','parser.py',64),
  ('definicion -> primary_key','definicion',1,'p_definicion','parser.py',65),
  ('definicion -> foreign_key','definicion',1,'p_definicion','parser.py',66),
  ('columna -> IDENTIFICADOR tipos_datos atributos','columna',3,'p_columna','parser.py',71),
  ('primary_key -> PRIMARY KEY PARIZQ IDENTIFICADOR PARDER','primary_key',5,'p_primary_key','parser.py',76),
  ('foreign_key -> FOREIGN KEY PARIZQ IDENTIFICADOR PARDER REFERENCES IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ IDENTIFICADOR PARDER','foreign_key',12,'p_foreign_key','parser.py',81),
  ('tipos_datos -> BIGINT','tipos_datos',1,'p_tipos_datos','parser.py',86),
  ('tipos_datos -> INTEGER','tipos_datos',1,'p_tipos_datos','parser.py',87),
  ('tipos_datos -> DECIMAL','tipos_datos',1,'p_tipos_datos','parser.py',88),
  ('tipos_datos -> CHARACTER VARYING PARIZQ NUMERO PARDER','tipos_datos',5,'p_tipos_datos','parser.py',89),
  ('tipos_datos -> CHARACTER VARYING','tipos_datos',2,'p_tipos_datos','parser.py',90),
  ('tipos_datos -> CHAR','tipos_datos',1,'p_tipos_datos','parser.py',91),
  ('tipos_datos -> VARCHAR PARIZQ NUMERO PARDER','tipos_datos',4,'p_tipos_datos','parser.py',92),
  ('tipos_datos -> TEXT','tipos_datos',1,'p_tipos_datos','parser.py',93),
  ('atributos -> NOT NULL','atributos',2,'p_atributos','parser.py',103),
  ('atributos -> NULL','atributos',1,'p_atributos','parser.py',104),
  ('atributos -> <empty>','atributos',0,'p_atributos','parser.py',105),
  ('insertar_datos -> INSERT INTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ identificadores PARDER VALUES listas_valores PUNTOCOMA','insertar_datos',11,'p_insertar_datos','parser.py',110),
  ('listas_valores -> listas_valores COMA PARIZQ valores PARDER','listas_valores',5,'p_listas_valores','parser.py',115),
  ('listas_valores -> PARIZQ valores PARDER','listas_valores',3,'p_listas_valores','parser.py',116),
  ('identificadores -> identificadores COMA IDENTIFICADOR','identificadores',3,'p_identificadores','parser.py',124),
  ('identificadores -> IDENTIFICADOR','identificadores',1,'p_identificadores','parser.py',125),
  ('valores -> valores COMA valor','valores',3,'p_valores','parser.py',132),
  ('valores -> valor','valores',1,'p_valores','parser.py',133),
  ('valor -> NUMERO','valor',1,'p_valor','parser.py',140),
  ('valor -> CADENA','valor',1,'p_valor','parser.py',141),
  ('valor -> expresion','valor',1,'p_valor','parser.py',142),
  ('consulta_datos -> SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR joins group_by having order_by limit PUNTOCOMA','consulta_datos',12,'p_consulta_datos','parser.py',147),
  ('consulta_datos -> SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMA','consulta_datos',7,'p_consulta_datos','parser.py',148),
  ('seleccion -> seleccion COMA IDENTIFICADOR','seleccion',3,'p_seleccion','parser.py',156),
  ('seleccion -> IDENTIFICADOR','seleccion',1,'p_seleccion','parser.py',157),
  ('seleccion -> agregacion','seleccion',1,'p_seleccion','parser.py',158),
  ('joins -> joins join','joins',2,'p_joins','parser.py',166),
  ('joins -> join','joins',1,'p_joins','parser.py',167),
  ('join -> JOIN IDENTIFICADOR PUNTO IDENTIFICADOR ON IDENTIFICADOR operador IDENTIFICADOR','join',8,'p_join','parser.py',174),
  ('agregacion -> SUM PARIZQ IDENTIFICADOR PARDER','agregacion',4,'p_agregacion','parser.py',178),
  ('agregacion -> COUNT PARIZQ IDENTIFICADOR PARDER','agregacion',4,'p_agregacion','parser.py',179),
  ('agregacion -> AVG PARIZQ IDENTIFICADOR PARDER','agregacion',4,'p_agregacion','parser.py',180),
  ('agregacion -> MAX PARIZQ IDENTIFICADOR PARDER','agregacion',4,'p_agregacion','parser.py',181),
  ('agregacion -> MIN PARIZQ IDENTIFICADOR PARDER','agregacion',4,'p_agregacion','parser.py',182),
  ('group_by -> GROUP BY IDENTIFICADOR','group_by',3,'p_group_by','parser.py',186),
  ('group_by -> <empty>','group_by',0,'p_group_by','parser.py',187),
  ('having -> HAVING condicion','having',2,'p_having','parser.py',194),
  ('having -> <empty>','having',0,'p_having','parser.py',195),
  ('order_by -> ORDER BY IDENTIFICADOR','order_by',3,'p_order_by','parser.py',202),
  ('order_by -> ORDER BY IDENTIFICADOR ASC','order_by',4,'p_order_by','parser.py',203),
  ('order_by -> ORDER BY IDENTIFICADOR DESC','order_by',4,'p_order_by','parser.py',204),
  ('order_by -> <empty>','order_by',0,'p_order_by','parser.py',205),
  ('limit -> LIMIT NUMERO','limit',2,'p_limit','parser.py',214),
  ('limit -> <empty>','limit',0,'p_limit','parser.py',215),
  ('modificar_datos -> UPDATE IDENTIFICADOR PUNTO IDENTIFICADOR SET asignaciones WHERE condiciones PUNTOCOMA','modificar_datos',9,'p_modificar_datos','parser.py',223),
  ('asignaciones -> asignaciones COMA asignacion','asignaciones',3,'p_asignaciones_lista','parser.py',228),
  ('asignaciones -> asignacion','asignaciones',1,'p_asignaciones_lista','parser.py',229),
  ('asignacion -> IDENTIFICADOR IGUAL valor','asignacion',3,'p_asignacion','parser.py',236),
  ('eliminar_datos -> DELETE FROM IDENTIFICADOR PUNTO IDENTIFICADOR WHERE condiciones PUNTOCOMA','eliminar_datos',8,'p_eliminar_datos','parser.py',241),
  ('condiciones -> condiciones operador_logico condicion','condiciones',3,'p_condiciones_lista','parser.py',246),
  ('condiciones -> condicion','condiciones',1,'p_condiciones_lista','parser.py',247),
  ('condicion -> IDENTIFICADOR operador valor','condicion',3,'p_condicion','parser.py',254),
  ('condicion -> IDENTIFICADOR operador PARIZQ consulta_datos PARDER','condicion',5,'p_condicion','parser.py',255),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','parser.py',262),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','parser.py',263),
  ('operador -> IGUAL','operador',1,'p_operador','parser.py',267),
  ('operador -> DIFERENTE','operador',1,'p_operador','parser.py',268),
  ('operador -> MAYORQUE','operador',1,'p_operador','parser.py',269),
  ('operador -> MENORQUE','operador',1,'p_operador','parser.py',270),
  ('operador -> MAYORIGUAL','operador',1,'p_operador','parser.py',271),
  ('operador -> MENORIGUAL','operador',1,'p_operador','parser.py',272),
  ('expresion -> valor MAS valor','expresion',3,'p_expresion','parser.py',277),
  ('expresion -> valor MENOS valor','expresion',3,'p_expresion','parser.py',278),
  ('expresion -> valor MULTIPLICACION valor','expresion',3,'p_expresion','parser.py',279),
  ('expresion -> valor DIVISION valor','expresion',3,'p_expresion','parser.py',280),
  ('transaccion -> BEGIN PUNTOCOMA','transaccion',2,'p_transaccion','parser.py',285),
  ('transaccion -> COMMIT PUNTOCOMA','transaccion',2,'p_transaccion','parser.py',286),
  ('transaccion -> ROLLBACK PUNTOCOMA','transaccion',2,'p_transaccion','parser.py',287),
]
