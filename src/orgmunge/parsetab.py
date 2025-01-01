
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATIMESTAMP COMMENT COOKIE DRAWER ITIMESTAMP METADATA NEWLINE PRIORITY SCHEDULING SEPARATOR SPACE STARS TAGS TEXT TODOorg_file : metadata org_tree\n| non_metadata_body_text SEPARATOR org_tree\n| non_metadata_body_text SEPARATOR\n| metadata non_metadata_body_text SEPARATOR org_tree\n| metadata non_metadata_body_text SEPARATOR \n| metadata\n| org_tree\n| SEPARATOR\n| emptymetadata : METADATA SEPARATOR\n| METADATA NEWLINEorg_tree : heading\n| heading SEPARATOR\n| org_tree heading SEPARATOR\n| org_tree headingheading : headline NEWLINE contents\n| headline SEPARATORheadline : STARS SPACE comment todo priority title cookie tagscomment : COMMENT SPACE\n| emptytodo : TODO SPACE\n| emptypriority : PRIORITY SPACE\n| emptytitle : TEXT \n| TODO\n| title TODO\n| title TEXT\n| title SPACE TEXT\n| title SPACE TODO\n| title SPACE\n| emptycookie : COOKIE SPACE\n| COOKIE\n| emptytags : TAGS\n| emptycontents : scheduling drawers bodyscheduling_data : SCHEDULING SPACE any_timestamp NEWLINE\n| SCHEDULING SPACE any_timestamp SEPARATOR\n| SCHEDULING SPACE any_timestamp SPACE\n| scheduling_data SCHEDULING SPACE any_timestamp NEWLINE\n| scheduling_data SCHEDULING SPACE any_timestamp SEPARATOR\n| scheduling_data SCHEDULING SPACE any_timestamp SPACEscheduling : scheduling_data\n| emptyany_timestamp : ATIMESTAMP\n| ITIMESTAMPdrawer_data : DRAWER NEWLINE\n| DRAWER SEPARATOR\n| drawer_data DRAWER NEWLINE\n| drawer_data DRAWER SEPARATORdrawers : drawer_data\n| emptybody : body_text\n| emptynon_metadata_body_text : TEXT\n| SPACE\n| any_timestamp\n| non_metadata_body_text TEXT\n| non_metadata_body_text SPACE\n| non_metadata_body_text special_token\n| non_metadata_body_text NEWLINEspecial_token : SCHEDULING\n| COOKIE\n| PRIORITY\n| TODO\n| any_timestamp\n| COMMENT\n| TAGSbody_text : TEXT\n| SPACE\n| METADATA\n| special_token\n| body_text TEXT\n| body_text SPACE\n| body_text special_token\n| body_text METADATA\n| body_text NEWLINEempty :'
    
_lr_action_items = {'SEPARATOR':([0,4,7,8,9,10,11,12,13,14,17,18,20,21,22,23,24,25,26,27,28,29,30,34,35,36,40,41,42,43,45,47,49,50,51,52,55,57,58,59,60,61,62,63,64,65,66,67,68,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,],[5,19,31,-57,-58,-59,33,-47,-48,35,37,38,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-17,-80,-16,-80,-45,-46,-80,-20,-80,-53,-54,68,-80,-22,-19,-38,-55,-56,-71,-72,-73,-74,81,-49,-50,85,-80,-24,-21,-75,-76,-77,-78,-79,-51,-52,93,-41,-39,-40,-80,-25,-26,-32,-23,-44,-42,-43,-31,-80,-27,-28,-34,-35,-29,-30,-18,-36,-37,-33,]),'METADATA':([0,12,13,24,25,26,27,28,29,30,34,41,42,43,49,50,51,60,62,63,64,65,67,68,75,76,77,78,79,80,81,83,84,85,91,92,93,],[7,-47,-48,-64,-65,-66,-67,-68,-69,-70,-80,-80,-45,-46,64,-53,-54,78,-71,-72,-73,-74,-49,-50,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'TEXT':([0,2,4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,41,42,43,45,47,49,50,51,55,57,58,60,62,63,64,65,67,68,71,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,93,94,96,97,100,101,],[8,8,20,-57,-58,-59,-47,-48,20,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-10,-11,-80,-80,-80,-45,-46,-80,-20,62,-53,-54,-80,-22,-19,75,-71,-72,-73,-74,-49,-50,87,-24,-21,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,97,-25,-26,-32,-23,-44,-42,-43,100,-27,-28,-29,-30,]),'SPACE':([0,2,4,8,9,10,12,13,15,17,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,41,42,43,44,45,46,47,49,50,51,53,55,56,57,58,60,62,63,64,65,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,100,101,],[9,9,21,-57,-58,-59,-47,-48,36,21,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-10,-11,-80,-80,-80,-45,-46,54,-80,58,-20,63,-53,-54,69,-80,74,-22,-19,76,-71,-72,-73,-74,-49,-50,83,-80,90,-24,-21,-75,-76,-77,-78,-79,-51,-52,91,-41,-39,-40,94,-25,-26,-32,-23,-44,-42,-43,-31,-27,-28,105,-29,-30,]),'$end':([0,1,2,3,5,6,11,12,13,16,18,19,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,48,49,50,51,59,60,61,62,63,64,65,67,68,75,76,77,78,79,80,81,83,84,85,91,92,93,],[-80,0,-6,-7,-8,-9,-12,-47,-48,-1,-15,-3,-64,-65,-66,-67,-68,-69,-70,-10,-11,-13,-80,-17,-5,-14,-2,-16,-80,-45,-46,-4,-80,-53,-54,-38,-55,-56,-71,-72,-73,-74,-49,-50,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'ATIMESTAMP':([0,2,4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,31,32,34,41,42,43,49,50,51,54,60,62,63,64,65,67,68,69,75,76,77,78,79,80,81,83,84,85,91,92,93,],[12,12,12,-57,-58,-59,-47,-48,12,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-10,-11,-80,-80,-45,-46,12,-53,-54,12,12,-71,-72,-73,-74,-49,-50,12,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'ITIMESTAMP':([0,2,4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,31,32,34,41,42,43,49,50,51,54,60,62,63,64,65,67,68,69,75,76,77,78,79,80,81,83,84,85,91,92,93,],[13,13,13,-57,-58,-59,-47,-48,13,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-10,-11,-80,-80,-45,-46,13,-53,-54,13,13,-71,-72,-73,-74,-49,-50,13,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'STARS':([0,2,3,11,12,13,16,18,19,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,48,49,50,51,59,60,61,62,63,64,65,67,68,75,76,77,78,79,80,81,83,84,85,91,92,93,],[15,15,15,-12,-47,-48,15,-15,15,-64,-65,-66,-67,-68,-69,-70,-10,-11,-13,-80,-17,15,-14,15,-16,-80,-45,-46,15,-80,-53,-54,-38,-55,-56,-71,-72,-73,-74,-49,-50,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'NEWLINE':([4,7,8,9,10,12,13,14,17,20,21,22,23,24,25,26,27,28,29,30,36,45,47,52,55,57,58,60,62,63,64,65,66,70,71,73,74,75,76,77,78,79,82,86,87,88,89,90,94,95,96,97,98,99,100,101,102,103,104,105,],[23,32,-57,-58,-59,-47,-48,34,23,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-80,-20,67,-80,-22,-19,79,-71,-72,-73,-74,80,84,-80,-24,-21,-75,-76,-77,-78,-79,92,-80,-25,-26,-32,-23,-31,-80,-27,-28,-34,-35,-29,-30,-18,-36,-37,-33,]),'SCHEDULING':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,41,42,43,49,50,51,60,62,63,64,65,67,68,75,76,77,78,79,80,81,83,84,85,91,92,93,],[24,-57,-58,-59,-47,-48,24,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,44,-80,53,-46,24,-53,-54,24,-71,-72,-73,-74,-49,-50,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'COOKIE':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,36,41,42,43,45,47,49,50,51,55,57,58,60,62,63,64,65,67,68,71,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,93,94,96,97,100,101,],[25,-57,-58,-59,-47,-48,25,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-80,-80,-45,-46,-80,-20,25,-53,-54,-80,-22,-19,25,-71,-72,-73,-74,-49,-50,-80,-24,-21,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,98,-25,-26,-32,-23,-44,-42,-43,-31,-27,-28,-29,-30,]),'PRIORITY':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,36,41,42,43,45,47,49,50,51,55,57,58,60,62,63,64,65,67,68,74,75,76,77,78,79,80,81,83,84,85,91,92,93,],[26,-57,-58,-59,-47,-48,26,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-80,-80,-45,-46,-80,-20,26,-53,-54,72,-22,-19,26,-71,-72,-73,-74,-49,-50,-21,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'TODO':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,36,41,42,43,45,47,49,50,51,55,57,58,60,62,63,64,65,67,68,71,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,93,94,96,97,100,101,],[27,-57,-58,-59,-47,-48,27,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-80,-80,-45,-46,56,-20,27,-53,-54,-80,-22,-19,27,-71,-72,-73,-74,-49,-50,88,-24,-21,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,96,-25,-26,-32,-23,-44,-42,-43,101,-27,-28,-29,-30,]),'COMMENT':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,36,41,42,43,49,50,51,60,62,63,64,65,67,68,75,76,77,78,79,80,81,83,84,85,91,92,93,],[29,-57,-58,-59,-47,-48,29,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,46,-80,-45,-46,29,-53,-54,29,-71,-72,-73,-74,-49,-50,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-44,-42,-43,]),'TAGS':([4,8,9,10,12,13,17,20,21,22,23,24,25,26,27,28,29,30,34,36,41,42,43,45,47,49,50,51,55,57,58,60,62,63,64,65,67,68,71,73,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,],[30,-57,-58,-59,-47,-48,30,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-80,-80,-80,-45,-46,-80,-20,30,-53,-54,-80,-22,-19,30,-71,-72,-73,-74,-49,-50,-80,-24,-21,-75,-76,-77,-78,-79,-51,-52,-41,-39,-40,-80,-25,-26,-32,-23,-44,-42,-43,-31,103,-27,-28,-34,-35,-29,-30,-33,]),'DRAWER':([34,41,42,43,50,67,68,80,81,83,84,85,91,92,93,],[-80,52,-45,-46,66,-49,-50,-51,-52,-41,-39,-40,-44,-42,-43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'org_file':([0,],[1,]),'metadata':([0,],[2,]),'org_tree':([0,2,19,37,],[3,16,39,48,]),'non_metadata_body_text':([0,2,],[4,17,]),'empty':([0,34,36,41,45,49,55,71,86,95,],[6,43,47,51,57,61,73,89,99,104,]),'any_timestamp':([0,2,4,17,49,54,60,69,],[10,10,28,28,28,70,28,82,]),'heading':([0,2,3,16,19,37,39,48,],[11,11,18,18,11,11,18,18,]),'headline':([0,2,3,16,19,37,39,48,],[14,14,14,14,14,14,14,14,]),'special_token':([4,17,49,60,],[22,22,65,77,]),'contents':([34,],[40,]),'scheduling':([34,],[41,]),'scheduling_data':([34,],[42,]),'comment':([36,],[45,]),'drawers':([41,],[49,]),'drawer_data':([41,],[50,]),'todo':([45,],[55,]),'body':([49,],[59,]),'body_text':([49,],[60,]),'priority':([55,],[71,]),'title':([71,],[86,]),'cookie':([86,],[95,]),'tags':([95,],[102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> org_file","S'",1,None,None,None),
  ('org_file -> metadata org_tree','org_file',2,'p_org_file','parser.py',14),
  ('org_file -> non_metadata_body_text SEPARATOR org_tree','org_file',3,'p_org_file','parser.py',15),
  ('org_file -> non_metadata_body_text SEPARATOR','org_file',2,'p_org_file','parser.py',16),
  ('org_file -> metadata non_metadata_body_text SEPARATOR org_tree','org_file',4,'p_org_file','parser.py',17),
  ('org_file -> metadata non_metadata_body_text SEPARATOR','org_file',3,'p_org_file','parser.py',18),
  ('org_file -> metadata','org_file',1,'p_org_file','parser.py',19),
  ('org_file -> org_tree','org_file',1,'p_org_file','parser.py',20),
  ('org_file -> SEPARATOR','org_file',1,'p_org_file','parser.py',21),
  ('org_file -> empty','org_file',1,'p_org_file','parser.py',22),
  ('metadata -> METADATA SEPARATOR','metadata',2,'p_metadata','parser.py',42),
  ('metadata -> METADATA NEWLINE','metadata',2,'p_metadata','parser.py',43),
  ('org_tree -> heading','org_tree',1,'p_org_tree','parser.py',47),
  ('org_tree -> heading SEPARATOR','org_tree',2,'p_org_tree','parser.py',48),
  ('org_tree -> org_tree heading SEPARATOR','org_tree',3,'p_org_tree','parser.py',49),
  ('org_tree -> org_tree heading','org_tree',2,'p_org_tree','parser.py',50),
  ('heading -> headline NEWLINE contents','heading',3,'p_heading','parser.py',62),
  ('heading -> headline SEPARATOR','heading',2,'p_heading','parser.py',63),
  ('headline -> STARS SPACE comment todo priority title cookie tags','headline',8,'p_headline','parser.py',70),
  ('comment -> COMMENT SPACE','comment',2,'p_comment','parser.py',75),
  ('comment -> empty','comment',1,'p_comment','parser.py',76),
  ('todo -> TODO SPACE','todo',2,'p_todo','parser.py',80),
  ('todo -> empty','todo',1,'p_todo','parser.py',81),
  ('priority -> PRIORITY SPACE','priority',2,'p_priority','parser.py',85),
  ('priority -> empty','priority',1,'p_priority','parser.py',86),
  ('title -> TEXT','title',1,'p_title','parser.py',90),
  ('title -> TODO','title',1,'p_title','parser.py',91),
  ('title -> title TODO','title',2,'p_title','parser.py',92),
  ('title -> title TEXT','title',2,'p_title','parser.py',93),
  ('title -> title SPACE TEXT','title',3,'p_title','parser.py',94),
  ('title -> title SPACE TODO','title',3,'p_title','parser.py',95),
  ('title -> title SPACE','title',2,'p_title','parser.py',96),
  ('title -> empty','title',1,'p_title','parser.py',97),
  ('cookie -> COOKIE SPACE','cookie',2,'p_cookie','parser.py',102),
  ('cookie -> COOKIE','cookie',1,'p_cookie','parser.py',103),
  ('cookie -> empty','cookie',1,'p_cookie','parser.py',104),
  ('tags -> TAGS','tags',1,'p_tags','parser.py',108),
  ('tags -> empty','tags',1,'p_tags','parser.py',109),
  ('contents -> scheduling drawers body','contents',3,'p_contents','parser.py',116),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp NEWLINE','scheduling_data',4,'p_scheduling_data','parser.py',120),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp SEPARATOR','scheduling_data',4,'p_scheduling_data','parser.py',121),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp SPACE','scheduling_data',4,'p_scheduling_data','parser.py',122),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp NEWLINE','scheduling_data',5,'p_scheduling_data','parser.py',123),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp SEPARATOR','scheduling_data',5,'p_scheduling_data','parser.py',124),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp SPACE','scheduling_data',5,'p_scheduling_data','parser.py',125),
  ('scheduling -> scheduling_data','scheduling',1,'p_scheduling','parser.py',134),
  ('scheduling -> empty','scheduling',1,'p_scheduling','parser.py',135),
  ('any_timestamp -> ATIMESTAMP','any_timestamp',1,'p_any_timestamp','parser.py',139),
  ('any_timestamp -> ITIMESTAMP','any_timestamp',1,'p_any_timestamp','parser.py',140),
  ('drawer_data -> DRAWER NEWLINE','drawer_data',2,'p_drawer_data','parser.py',144),
  ('drawer_data -> DRAWER SEPARATOR','drawer_data',2,'p_drawer_data','parser.py',145),
  ('drawer_data -> drawer_data DRAWER NEWLINE','drawer_data',3,'p_drawer_data','parser.py',146),
  ('drawer_data -> drawer_data DRAWER SEPARATOR','drawer_data',3,'p_drawer_data','parser.py',147),
  ('drawers -> drawer_data','drawers',1,'p_drawers','parser.py',162),
  ('drawers -> empty','drawers',1,'p_drawers','parser.py',163),
  ('body -> body_text','body',1,'p_body','parser.py',167),
  ('body -> empty','body',1,'p_body','parser.py',168),
  ('non_metadata_body_text -> TEXT','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',172),
  ('non_metadata_body_text -> SPACE','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',173),
  ('non_metadata_body_text -> any_timestamp','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',174),
  ('non_metadata_body_text -> non_metadata_body_text TEXT','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',175),
  ('non_metadata_body_text -> non_metadata_body_text SPACE','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',176),
  ('non_metadata_body_text -> non_metadata_body_text special_token','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',177),
  ('non_metadata_body_text -> non_metadata_body_text NEWLINE','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',178),
  ('special_token -> SCHEDULING','special_token',1,'p_special_token','parser.py',182),
  ('special_token -> COOKIE','special_token',1,'p_special_token','parser.py',183),
  ('special_token -> PRIORITY','special_token',1,'p_special_token','parser.py',184),
  ('special_token -> TODO','special_token',1,'p_special_token','parser.py',185),
  ('special_token -> any_timestamp','special_token',1,'p_special_token','parser.py',186),
  ('special_token -> COMMENT','special_token',1,'p_special_token','parser.py',187),
  ('special_token -> TAGS','special_token',1,'p_special_token','parser.py',188),
  ('body_text -> TEXT','body_text',1,'p_body_text','parser.py',192),
  ('body_text -> SPACE','body_text',1,'p_body_text','parser.py',193),
  ('body_text -> METADATA','body_text',1,'p_body_text','parser.py',194),
  ('body_text -> special_token','body_text',1,'p_body_text','parser.py',195),
  ('body_text -> body_text TEXT','body_text',2,'p_body_text','parser.py',196),
  ('body_text -> body_text SPACE','body_text',2,'p_body_text','parser.py',197),
  ('body_text -> body_text special_token','body_text',2,'p_body_text','parser.py',198),
  ('body_text -> body_text METADATA','body_text',2,'p_body_text','parser.py',199),
  ('body_text -> body_text NEWLINE','body_text',2,'p_body_text','parser.py',200),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',204),
]
