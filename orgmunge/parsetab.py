
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATIMESTAMP COMMENT COOKIE DRAWER ITIMESTAMP METADATA NEWLINE PRIORITY SCHEDULING SEPARATOR SPACE STARS TAGS TEXT TODOorg_file : metadata org_tree\n                | non_metadata_body_text SEPARATOR org_tree\n                | metadata non_metadata_body_text SEPARATOR org_tree\n                | metadata non_metadata_body_text SEPARATOR \n                | metadata\n                | org_tree\n                | emptymetadata : METADATA SEPARATOR\n                | METADATA NEWLINEorg_tree : heading\n                | heading SEPARATOR\n                | org_tree heading SEPARATOR\n                | org_tree headingheading : headline NEWLINE contents\n               | headline SEPARATORheadline : STARS SPACE comment todo priority title cookie tagscomment : COMMENT SPACE\n               | emptytodo : TODO SPACE\n            | emptypriority : PRIORITY SPACE\n                | emptytitle : TEXT \n             | title SPACE TEXT\n             | title SPACEcookie : COOKIE SPACE\n              | COOKIE\n              | emptytags : TAGS\n            | emptycontents : scheduling drawers bodyscheduling_data : SCHEDULING SPACE any_timestamp NEWLINE\n                       | SCHEDULING SPACE any_timestamp SEPARATOR\n                       | SCHEDULING SPACE any_timestamp SPACE\n                       | scheduling_data SCHEDULING SPACE any_timestamp NEWLINE\n                       | scheduling_data SCHEDULING SPACE any_timestamp SEPARATOR\n                       | scheduling_data SCHEDULING SPACE any_timestamp SPACEscheduling : scheduling_data\n                  | emptyany_timestamp : ATIMESTAMP\n                     | ITIMESTAMPdrawer_data : DRAWER NEWLINE\n                   | DRAWER SEPARATOR\n                   | drawer_data DRAWER NEWLINE\n                   | drawer_data DRAWER SEPARATORdrawers : drawer_data\n               | emptybody : body_text\n            | emptynon_metadata_body_text : TEXT\n                              | SPACE\n                              | any_timestamp\n                              | non_metadata_body_text TEXT\n                              | non_metadata_body_text SPACE\n                              | non_metadata_body_text special_token\n                              | non_metadata_body_text NEWLINEspecial_token : SCHEDULING\n                     | COOKIE\n                     | PRIORITY\n                     | TODO\n                     | any_timestamp\n                     | COMMENT\n                     | TAGSbody_text : TEXT\n                 | SPACE\n                 | METADATA\n                 | special_token\n                 | body_text TEXT\n                 | body_text SPACE\n                 | body_text special_token\n                 | body_text METADATA\n                 | body_text NEWLINEempty :'
    
_lr_action_items = {'METADATA':([0,11,12,23,24,25,26,27,28,29,33,40,41,42,48,49,50,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[6,-40,-41,-57,-58,-59,-60,-61,-62,-63,-73,-73,-38,-39,63,-46,-47,77,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'TEXT':([0,2,4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,30,31,33,35,40,41,42,44,46,48,49,50,54,56,57,59,61,62,63,64,66,67,70,72,73,74,75,76,77,78,79,80,82,83,84,87,88,89,90,91,],[7,7,19,-50,-51,-52,-40,-41,19,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-8,-9,-73,-73,-73,-38,-39,-73,-18,61,-46,-47,-73,-20,-17,74,-64,-65,-66,-67,-42,-43,86,-22,-19,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-21,-37,-35,-36,95,]),'SPACE':([0,2,4,7,8,9,11,12,14,16,19,20,21,22,23,24,25,26,27,28,29,30,31,33,40,41,42,43,45,48,49,50,52,55,59,61,62,63,64,66,67,69,71,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,91,93,95,],[8,8,20,-50,-51,-52,-40,-41,35,20,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-8,-9,-73,-73,-38,-39,53,57,62,-46,-47,68,73,75,-64,-65,-66,-67,-42,-43,82,87,-68,-69,-70,-71,-72,-44,-45,88,-34,-32,-33,91,-23,-37,-35,-36,-25,99,-24,]),'$end':([0,1,2,3,5,10,11,12,15,17,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,47,48,49,50,58,59,60,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[-73,0,-5,-6,-7,-10,-40,-41,-1,-13,-57,-58,-59,-60,-61,-62,-63,-8,-9,-11,-73,-15,-4,-12,-2,-14,-73,-38,-39,-3,-73,-46,-47,-31,-48,-49,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'ATIMESTAMP':([0,2,4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,30,31,33,40,41,42,48,49,50,53,59,61,62,63,64,66,67,68,74,75,76,77,78,79,80,82,83,84,88,89,90,],[11,11,11,-50,-51,-52,-40,-41,11,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-8,-9,-73,-73,-38,-39,11,-46,-47,11,11,-64,-65,-66,-67,-42,-43,11,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'ITIMESTAMP':([0,2,4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,30,31,33,40,41,42,48,49,50,53,59,61,62,63,64,66,67,68,74,75,76,77,78,79,80,82,83,84,88,89,90,],[12,12,12,-50,-51,-52,-40,-41,12,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-8,-9,-73,-73,-38,-39,12,-46,-47,12,12,-64,-65,-66,-67,-42,-43,12,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'STARS':([0,2,3,10,11,12,15,17,18,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,47,48,49,50,58,59,60,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[14,14,14,-10,-40,-41,14,-13,14,-57,-58,-59,-60,-61,-62,-63,-8,-9,-11,-73,-15,14,-12,14,-14,-73,-38,-39,14,-73,-46,-47,-31,-48,-49,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'SEPARATOR':([4,6,7,8,9,10,11,12,13,16,17,19,20,21,22,23,24,25,26,27,28,29,33,34,39,40,41,42,48,49,50,51,58,59,60,61,62,63,64,65,66,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,91,92,93,94,95,96,97,98,99,],[18,30,-50,-51,-52,32,-40,-41,34,36,37,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,-15,-14,-73,-38,-39,-73,-46,-47,67,-31,-48,-49,-64,-65,-66,-67,80,-42,-43,84,-68,-69,-70,-71,-72,-44,-45,90,-34,-32,-33,-73,-23,-37,-35,-36,-25,-73,-27,-28,-24,-16,-29,-30,-26,]),'NEWLINE':([4,6,7,8,9,11,12,13,16,19,20,21,22,23,24,25,26,27,28,29,51,59,61,62,63,64,65,69,74,75,76,77,78,81,85,86,91,92,93,94,95,96,97,98,99,],[22,31,-50,-51,-52,-40,-41,33,22,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,66,78,-64,-65,-66,-67,79,83,-68,-69,-70,-71,-72,89,-73,-23,-25,-73,-27,-28,-24,-16,-29,-30,-26,]),'SCHEDULING':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,40,41,42,48,49,50,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[23,-50,-51,-52,-40,-41,23,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,43,-73,52,-39,23,-46,-47,23,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'COOKIE':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,40,41,42,48,49,50,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,85,86,88,89,90,91,95,],[24,-50,-51,-52,-40,-41,24,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,-73,-38,-39,24,-46,-47,24,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,93,-23,-37,-35,-36,-25,-24,]),'PRIORITY':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,35,40,41,42,44,46,48,49,50,54,56,57,59,61,62,63,64,66,67,73,74,75,76,77,78,79,80,82,83,84,88,89,90,],[25,-50,-51,-52,-40,-41,25,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,-73,-73,-38,-39,-73,-18,25,-46,-47,71,-20,-17,25,-64,-65,-66,-67,-42,-43,-19,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'TODO':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,35,40,41,42,44,46,48,49,50,57,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[26,-50,-51,-52,-40,-41,26,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,-73,-73,-38,-39,55,-18,26,-46,-47,-17,26,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'COMMENT':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,35,40,41,42,48,49,50,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,88,89,90,],[28,-50,-51,-52,-40,-41,28,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,45,-73,-38,-39,28,-46,-47,28,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-37,-35,-36,]),'TAGS':([4,7,8,9,11,12,16,19,20,21,22,23,24,25,26,27,28,29,33,40,41,42,48,49,50,59,61,62,63,64,66,67,74,75,76,77,78,79,80,82,83,84,85,86,88,89,90,91,92,93,94,95,99,],[29,-50,-51,-52,-40,-41,29,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-73,-73,-38,-39,29,-46,-47,29,-64,-65,-66,-67,-42,-43,-68,-69,-70,-71,-72,-44,-45,-34,-32,-33,-73,-23,-37,-35,-36,-25,97,-27,-28,-24,-26,]),'DRAWER':([33,40,41,42,49,66,67,79,80,82,83,84,88,89,90,],[-73,51,-38,-39,65,-42,-43,-44,-45,-34,-32,-33,-37,-35,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'org_file':([0,],[1,]),'metadata':([0,],[2,]),'org_tree':([0,2,18,36,],[3,15,38,47,]),'non_metadata_body_text':([0,2,],[4,16,]),'empty':([0,33,35,40,44,48,54,85,92,],[5,42,46,50,56,60,72,94,98,]),'any_timestamp':([0,2,4,16,48,53,59,68,],[9,9,27,27,27,69,27,81,]),'heading':([0,2,3,15,18,36,38,47,],[10,10,17,17,10,10,17,17,]),'headline':([0,2,3,15,18,36,38,47,],[13,13,13,13,13,13,13,13,]),'special_token':([4,16,48,59,],[21,21,64,76,]),'contents':([33,],[39,]),'scheduling':([33,],[40,]),'scheduling_data':([33,],[41,]),'comment':([35,],[44,]),'drawers':([40,],[48,]),'drawer_data':([40,],[49,]),'todo':([44,],[54,]),'body':([48,],[58,]),'body_text':([48,],[59,]),'priority':([54,],[70,]),'title':([70,],[85,]),'cookie':([85,],[92,]),'tags':([92,],[96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> org_file","S'",1,None,None,None),
  ('org_file -> metadata org_tree','org_file',2,'p_org_file','parser.py',10),
  ('org_file -> non_metadata_body_text SEPARATOR org_tree','org_file',3,'p_org_file','parser.py',11),
  ('org_file -> metadata non_metadata_body_text SEPARATOR org_tree','org_file',4,'p_org_file','parser.py',12),
  ('org_file -> metadata non_metadata_body_text SEPARATOR','org_file',3,'p_org_file','parser.py',13),
  ('org_file -> metadata','org_file',1,'p_org_file','parser.py',14),
  ('org_file -> org_tree','org_file',1,'p_org_file','parser.py',15),
  ('org_file -> empty','org_file',1,'p_org_file','parser.py',16),
  ('metadata -> METADATA SEPARATOR','metadata',2,'p_metadata','parser.py',30),
  ('metadata -> METADATA NEWLINE','metadata',2,'p_metadata','parser.py',31),
  ('org_tree -> heading','org_tree',1,'p_org_tree','parser.py',35),
  ('org_tree -> heading SEPARATOR','org_tree',2,'p_org_tree','parser.py',36),
  ('org_tree -> org_tree heading SEPARATOR','org_tree',3,'p_org_tree','parser.py',37),
  ('org_tree -> org_tree heading','org_tree',2,'p_org_tree','parser.py',38),
  ('heading -> headline NEWLINE contents','heading',3,'p_heading','parser.py',50),
  ('heading -> headline SEPARATOR','heading',2,'p_heading','parser.py',51),
  ('headline -> STARS SPACE comment todo priority title cookie tags','headline',8,'p_headline','parser.py',58),
  ('comment -> COMMENT SPACE','comment',2,'p_comment','parser.py',62),
  ('comment -> empty','comment',1,'p_comment','parser.py',63),
  ('todo -> TODO SPACE','todo',2,'p_todo','parser.py',67),
  ('todo -> empty','todo',1,'p_todo','parser.py',68),
  ('priority -> PRIORITY SPACE','priority',2,'p_priority','parser.py',72),
  ('priority -> empty','priority',1,'p_priority','parser.py',73),
  ('title -> TEXT','title',1,'p_title','parser.py',77),
  ('title -> title SPACE TEXT','title',3,'p_title','parser.py',78),
  ('title -> title SPACE','title',2,'p_title','parser.py',79),
  ('cookie -> COOKIE SPACE','cookie',2,'p_cookie','parser.py',83),
  ('cookie -> COOKIE','cookie',1,'p_cookie','parser.py',84),
  ('cookie -> empty','cookie',1,'p_cookie','parser.py',85),
  ('tags -> TAGS','tags',1,'p_tags','parser.py',89),
  ('tags -> empty','tags',1,'p_tags','parser.py',90),
  ('contents -> scheduling drawers body','contents',3,'p_contents','parser.py',97),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp NEWLINE','scheduling_data',4,'p_scheduling_data','parser.py',101),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp SEPARATOR','scheduling_data',4,'p_scheduling_data','parser.py',102),
  ('scheduling_data -> SCHEDULING SPACE any_timestamp SPACE','scheduling_data',4,'p_scheduling_data','parser.py',103),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp NEWLINE','scheduling_data',5,'p_scheduling_data','parser.py',104),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp SEPARATOR','scheduling_data',5,'p_scheduling_data','parser.py',105),
  ('scheduling_data -> scheduling_data SCHEDULING SPACE any_timestamp SPACE','scheduling_data',5,'p_scheduling_data','parser.py',106),
  ('scheduling -> scheduling_data','scheduling',1,'p_scheduling','parser.py',115),
  ('scheduling -> empty','scheduling',1,'p_scheduling','parser.py',116),
  ('any_timestamp -> ATIMESTAMP','any_timestamp',1,'p_any_timestamp','parser.py',120),
  ('any_timestamp -> ITIMESTAMP','any_timestamp',1,'p_any_timestamp','parser.py',121),
  ('drawer_data -> DRAWER NEWLINE','drawer_data',2,'p_drawer_data','parser.py',125),
  ('drawer_data -> DRAWER SEPARATOR','drawer_data',2,'p_drawer_data','parser.py',126),
  ('drawer_data -> drawer_data DRAWER NEWLINE','drawer_data',3,'p_drawer_data','parser.py',127),
  ('drawer_data -> drawer_data DRAWER SEPARATOR','drawer_data',3,'p_drawer_data','parser.py',128),
  ('drawers -> drawer_data','drawers',1,'p_drawers','parser.py',143),
  ('drawers -> empty','drawers',1,'p_drawers','parser.py',144),
  ('body -> body_text','body',1,'p_body','parser.py',148),
  ('body -> empty','body',1,'p_body','parser.py',149),
  ('non_metadata_body_text -> TEXT','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',153),
  ('non_metadata_body_text -> SPACE','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',154),
  ('non_metadata_body_text -> any_timestamp','non_metadata_body_text',1,'p_non_metadata_body_text','parser.py',155),
  ('non_metadata_body_text -> non_metadata_body_text TEXT','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',156),
  ('non_metadata_body_text -> non_metadata_body_text SPACE','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',157),
  ('non_metadata_body_text -> non_metadata_body_text special_token','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',158),
  ('non_metadata_body_text -> non_metadata_body_text NEWLINE','non_metadata_body_text',2,'p_non_metadata_body_text','parser.py',159),
  ('special_token -> SCHEDULING','special_token',1,'p_special_token','parser.py',163),
  ('special_token -> COOKIE','special_token',1,'p_special_token','parser.py',164),
  ('special_token -> PRIORITY','special_token',1,'p_special_token','parser.py',165),
  ('special_token -> TODO','special_token',1,'p_special_token','parser.py',166),
  ('special_token -> any_timestamp','special_token',1,'p_special_token','parser.py',167),
  ('special_token -> COMMENT','special_token',1,'p_special_token','parser.py',168),
  ('special_token -> TAGS','special_token',1,'p_special_token','parser.py',169),
  ('body_text -> TEXT','body_text',1,'p_body_text','parser.py',173),
  ('body_text -> SPACE','body_text',1,'p_body_text','parser.py',174),
  ('body_text -> METADATA','body_text',1,'p_body_text','parser.py',175),
  ('body_text -> special_token','body_text',1,'p_body_text','parser.py',176),
  ('body_text -> body_text TEXT','body_text',2,'p_body_text','parser.py',177),
  ('body_text -> body_text SPACE','body_text',2,'p_body_text','parser.py',178),
  ('body_text -> body_text special_token','body_text',2,'p_body_text','parser.py',179),
  ('body_text -> body_text METADATA','body_text',2,'p_body_text','parser.py',180),
  ('body_text -> body_text NEWLINE','body_text',2,'p_body_text','parser.py',181),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',185),
]
