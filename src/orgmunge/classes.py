#!/usr/bin/env python3

import re
from typing import Optional, List, Union, Tuple, Dict
from datetime import datetime as dt
from datetime import timedelta
from functools import reduce
from operator import add
from math import floor
from .lexer import Lexer 

ORG_TIME_FORMAT_NO_TIME = '%Y-%m-%d %a'
ORG_TIME_FORMAT = ORG_TIME_FORMAT_NO_TIME + ' %H:%M'

class Cookie:
    def __init__(self, text: str):
        """Cookies can be of type 'precent' (e.g. [5%])
        or 'progress' (e.g. [2/3]). Both types store
        their state as 2 numbers: m is the number of completed items
        and n is the total number. In the case of a perecent-type Cookie
        n is set to 100.
        """
        if re.search(r'%', text):
            self._cookie_type = 'percent'
            match = re.search(r'\[(.+)%\]', text)
            if match:
                self._m = int(match.group(1))
                if self._m > 100:
                    raise ValueError(f'Meaningless cookie value: {m}%')
            else:
                self._m = 0
            self._n = 100
        elif re.search(r'/', text):
            self._cookie_type = 'progress'
            match = re.search(r'\[(.*)/(.*)\]', text)
            m = int(match.group(1)) if match.group(1) != '' else 0
            n = int(match.group(2)) if match.group(2) != '' else 0
            self._m, self._n = m, n
        else:
            self._cookie_type = None
            self._m = 0
            self._n = 0
        if self._m > self._n:
            raise ValueError(f'Meaningless cookie value: {m}/{n}')

    @property
    def cookie_type(self):
        return self._cookie_type

    @cookie_type.setter
    def cookie_type(self, new_type: str):
        if new_type != self.cookie_type:
            if new_type == 'percent':
                self._m = int(self.m/self.n * 100)
                self._n = 100
            elif new_type == 'progress':
                # m and n are already defined. Nothing needs to be done
                pass
            else:
                raise ValueError(f'Unknown cookie type {new_type}')
            self._cookie_type = new_type

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f'Cookie progress can only be an integer, {value} passed.')
        elif value > self.n:
            raise ValueError(f"Can't have cookie progress set to {value} > {self.n}")
        else:
            self._m = value

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f'Cookie final value can only be an integer, {value} passed.')
        elif value < self.m:
            raise ValueError(f"Can't have cookie final value set to {value} < {self.m}")
        else:
            self._n = value

    def __repr__(self):
        return f'[{self.m}/{self.n}]' if self.cookie_type == 'progress' else f'[{self.m}%]'
            
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class Priority:
    allowed_values = ['A', 'B', 'C']
    def _parse_priority(self, p: str):
        match = re.search(r"^\[#(.)\]", p)
        return match.group(1) if match else p

    def __init__(self, priority_text: Optional[str]):
        p = self._parse_priority(priority_text) if priority_text is not None else priority_text
        self.priority = p

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value: Optional[str]):
        if value in self.allowed_values or value is None: # Allow None to remove priority
            self._priority = value
        else:
            raise ValueError(f"Priority must be one of {self.allowed_values}; {value} passed")

    def _raise(self):
        if self.priority is None:
            self.priority = self.allowed_values[0]
        idx = self.allowed_values.index(self.priority)
        self.priority = self.allowed_values[(idx + 1) % len(self.allowed_values)]

    def _lower(self):
        if self.priority is None:
            self.priority = self.allowed_values[-1]
        idx = self.allowed_values.index(self.priority)
        self.priority = self.allowed_values[(idx - 1) % len(self.allowed_values)]

    def __repr__(self):
        return f'[#{self.priority}]' if self.priority is not None else ''
            
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class Headline:
    def __init__(self, todos, level: str, comment: bool = False,
               todo: Optional[str] = None, priority: Optional[str] = None,
               title: str = "", cookie: Optional[str] = None, tags: Optional[List[str]] = None):
        self._level = len(re.sub(r'\s+', '', level)) # Number of leading asterisks
        self._comment = comment
        self._todo = todo
        self._priority = Priority(priority)
        self.title = title
        self._cookie = cookie if cookie is None else Cookie(cookie)
        self.tags = tags
        self._todo_states = list(todos['todo_states'].values())
        self._done_states = list(todos['done_states'].values())
        self._todo_keywords = {**todos['todo_states'], **todos['done_states']}
    @property
    def done(self):
        return self._is_done()

    @done.setter
    def done(self, _):
        raise AttributeError("Can't set the 'done' attribute")

    def _is_done(self):
        if self.todo is None or self.todo in self._todo_states:
            return False
        elif self.todo in self._done_states:
            return True
        else:
            raise ValueError(f"Uncategorized todo state {self.todo}")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f"Can only set headline level to an integer value, {value} passed.")
        self._level = value

    def promote(self, n: int = 1):
        level = self.level - n
        self.level = max(level, 1)

    def demote(self, n: int = 1):
        self.level += n

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError('The "comment" property must be a boolean!')
        self._comment = value

    def toggle_comment(self):
        self.comment = not(self.comment)

    def comment_out(self):
        self.comment = True

    def uncomment(self):
        self.comment = False

    @property
    def todo(self):
        return self._todo

    @todo.setter
    def todo(self, value: Optional[str]):
        if value not in self._todo_states and value not in self._done_states and value is not None:
            possible_states = set.union(self._todo_states, self._done_states)
            raise ValueError(f"Todo keyword has to be one of {','.join(possible_states)} or None, {value} passed.")
        else:
            self._todo = value

    @property
    def cookie(self):
        return self._cookie

    @cookie.setter
    def cookie(self, value: Cookie):
        if not isinstance(value, Cookie):
            raise ValueError("Can only set cookie to an instance of the Cookie class.")
        else:
            self._cookie = value

    def raise_priority(self):
        self.priority._raise()

    def lower_priority(self):
        self.priority._lower()

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value: Optional[str]):
        self._priority = Priority(value)

    def __repr__(self):
        priority = f'{self.priority}' + (' ' if str(self.priority) != '' else '')
        comment = "COMMENT " if self.comment else ""
        todo = f"{self.todo} " if self.todo else ""
        cookie = ' ' + str(self.cookie) if self.cookie else ""
        tags = f"    :{':'.join(self.tags)}:" if self.tags else ""
        return f"{'*' * self.level} {todo}{comment}{priority}{self.title}{cookie}{tags}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class TimeStamp:
    def __init__(self, timestamp_str: str):
        is_active = re.search(Lexer.ATIMESTAMP, timestamp_str)
        is_inactive = re.search(Lexer.ITIMESTAMP, timestamp_str)
        self._active = True if is_active else False
        match = is_active if self._active else is_inactive
        date, day_of_week, start_time, end_time, repeater, deadline_warn = match.groups()
        self._start_time = self._to_datetime([date, day_of_week, start_time])
        if end_time:
            end_time = re.sub(r'^-', '', end_time)
            self._end_time = self._to_datetime([date, day_of_week, end_time]) 
        else:
            self._end_time = None
        self._repeater = repeater
        self._deadline_warn = deadline_warn

    def _to_datetime(self, date_components: List[str]) -> dt:
        if date_components[-1] is None:
            dt_format = ORG_TIME_FORMAT_NO_TIME
            date_components = date_components[:-1]
        else:
            dt_format = ORG_TIME_FORMAT
        self._dt_format = dt_format
        return dt.strptime(' '.join(date_components), dt_format)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value: Union[str, dt, None]):
        if value is None:
            self._start_time = self.start_time.strftime(ORG_TIME_FORMAT_NO_TIME)
            t = None
        elif isinstance(value, str):
            t = dt.strptime(' '.join([self.start_time.strftime(ORG_TIME_FORMAT_NO_TIME), value]), ORG_TIME_FORMAT)
        elif isinstance(value, dt):
            if self.end_time and (value.year != self.end_time.year or value.month != self.end_time.month or value.day != self.end_time.day):
                raise ValueError('The start time for a timestamp must have the same date as the end time')
            else:
                t = value
        else:
            raise TypeError(f"Can't set timestamp start time from value of type {type(value)}!")
        if t and self.end_time and t > self.end_time:
            raise ValueError("Start time must be before end time")
        elif t:
            self._start_time = t

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        if isinstance(value, bool):
            self._active = value
        else:
            raise TypeError("The active property of timestamps needs to be a Boolean.")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value: Union[str, dt, None]):
        if value is None:
            self._end_time = None
            t = None
        elif isinstance(value, str):
            t = dt.strptime(' '.join([self.end_time.strftime(ORG_TIME_FORMAT_NO_TIME), value]), ORG_TIME_FORMAT)
        elif isinstance(value, dt):
            if value.year != self.start_time.year or value.month != self.start_time.month or value.day != self.start_time.day:
                raise ValueError('The end time for a timestamp must have the same date as the start time')
            else:
                t = value
        else:
            raise TypeError(f"Can't set timestamp end time from value of type {type(value)}!")
        if t and t < self.start_time:
            raise ValueError("End time must be after start time.")
        elif t:
            self._end_time = t

    @property
    def repeater(self):
        return self._repeater

    @repeater.setter
    def repeater(self, value: Optional[str]):
        if value is None:
            self._repeater = None
        elif re.search(r'^[.+]?\+[0-9]+[hdwmy]', value):
            self._repeater = value
        else:
            raise ValueError(f"Repeaters must start with .+, ++ or +, followed by an integer and one of h, d, w, m or y. Can't work with {value}.")

    @property
    def deadline_warn(self):
        return self._deadline_warn

    @deadline_warn.setter
    def deadline_warn(self, value: Optional[str]):
        if value is None:
            self._deadline_warn = None
        elif re.search(r'^-[0-9]+[hdwmy]', value):
            self._deadline_warn = value
        else:
            raise ValueError(f"Special deadline warnings must start with -, followed by an integer and one of h, d, w, m or y. Can't work with {value}.")
    def __repr__(self):
        ldelim = '<' if self.active else '['
        rdelim = '>' if self.active else ']'
        timestamp = self.start_time.strftime(self._dt_format)
        if self.end_time:
            timestamp += f'-{self.end_time.strftime("%H:%M")}'
        if self.repeater:
            timestamp += f'{self.repeater}'    
        if self.deadline_warn:
            timestamp += f'{self.deadline_warn}'
        return ldelim + timestamp + rdelim

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class Scheduling:
    _closed = None
    _scheduled = None
    _deadline = None

    # Helper class to group together common getter and setter code for all keywords
    class Keyword:
        def __init__(self, attr: str):
            self.attr = '_' + attr
        def __get__(self, obj, _):
            # The third argument doesn't matter. The caller needs to pass
            # in a keyword name to getattr and that gets passed on to this function
            # but it's not needed since each Keyword instance stores its keyword in
            # the attr attribute.
            return getattr(obj, self.attr)
        def __set__(self, obj, value):
            if value is None:
                setattr(obj, self.attr, None)
            elif isinstance(value, TimeStamp):
                if self.attr == '_closed':
                    value.active = False
                    value.end_time = value.repeater = value.deadline_warn = None
                if self.attr == '_scheduled' or self.attr == '_deadline':
                    value.active = True
                if self.attr != '_deadline':
                    value.deadline_warn = None
                setattr(obj, self.attr, value)
            else:
                raise TypeError(f"The timestamp value for a Scheduling keyword must be an instance of the TimeStamp class.")
    valid_keywords = ['closed', 'scheduled', 'deadline']
    def __init__(self, keyword: Optional[str] = None, timestamp: Optional[TimeStamp] = None):
        if keyword is not None and timestamp is not None:
            canonical_keyword = re.sub(r':\s*$', '', keyword).lower()
            if canonical_keyword not in self.valid_keywords:
                raise ValueError(f'Scheduling keyword must be one of {self.valid_keywords}, got {canonical_keyword}')
            else:
                if isinstance(timestamp, TimeStamp):
                    setattr(self, canonical_keyword, timestamp)
                else:
                    raise TypeError("The timestamp value for a Scheduling keyword must be an instance of the TimeStamp class")

    # Define this so the parser can add together multiple scheduling keywords:
    def __add__(self, other):
        for keyword in self.valid_keywords:
            if getattr(self, keyword) and getattr(other, keyword):
                raise ValueError(f"Can't merge two Scheduling types when both of them have the {keyword} property set.") 
            else:
                result = Scheduling()
                for keyword in self.valid_keywords:
                    setattr(result, keyword, getattr(self, keyword) or getattr(other, keyword) or None)
                return result

    CLOSED = closed = Keyword('closed')
    SCHEDULED = scheduled = Keyword('scheduled')
    DEADLINE = deadline = Keyword('deadline')

    def __repr__(self):
        data = [f'{keyword.upper()}: {getattr(self, keyword)}' for keyword in self.valid_keywords if getattr(self, keyword) is not None]
        return ' '.join(data)
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class Drawer:
    def __init__(self, drawer_string: str):
        self.name = re.sub(r':', '', drawer_string.split('\n')[0])
        self.contents = drawer_string.strip().split('\n')[1:-1]
    def __repr__(self):
        contents = "\n".join(self.contents)
        return f''':{self.name}:
{contents}
:END:
'''    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
class Clocking:
    def __init__(self, start_time: str, end_time: Optional[str] = None):
        self._start_time = dt.strptime(start_time, ORG_TIME_FORMAT)
        if end_time is not None:
            self._end_time = dt.strptime(end_time, ORG_TIME_FORMAT)
        else:
            self._end_time = None
        self._duration = None

    def _set_time(self, property: str, value: str):
        try:
            datetime_obj = dt.strptime(value, ORG_TIME_FORMAT)
            setattr(self, property, datetime_obj)
        except ValueError:
            raise ValueError(f"Time string {value} doesn't match expected org time format {ORG_TIME_FORMAT}")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value: str):
        self._set_time('_start_time', value)
        
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value: Optional[str]):
        if value is None:
            self._end_time = value
        else:
            self._set_time('_end_time', value)
        
    def _display_delta(self, time_delta: timedelta) -> str:
        total_seconds = time_delta.total_seconds()
        if total_seconds < 0:
            return f'-{self._display_delta(timedelta(seconds=-total_seconds))}'
        m, s = total_seconds/60, total_seconds%60
        if s > 30: m += 1 # Round minutes up
        h, m = m/60, m%60
        hours, minutes = [floor(x) for x in (h, m)]
        return f'{hours}:{minutes:02d}'

    @property
    def duration(self):
        if self.end_time is None:
            return self._display_delta(dt.now() - self.start_time)
        else:
            return self._display_delta(self.end_time - self.start_time)

    @duration.setter
    def duration(self, _):
        raise TypeError("Can't set the duration for a clocking object! Set the start and/or end time instead.")

    @property
    def duration_seconds(self):
        if self.end_time is None:
            return (dt.now() - self.start_time).seconds
        else:
            return (self.end_time - self.start_time).seconds

    @duration_seconds.setter
    def duration_seconds(self, _):
        raise TypeError("Can't set the duration for a clocking object! Set the start and/or end time instead.")

    def __repr__(self):
        if self.end_time is None:
            return f'[{self.start_time.strftime(ORG_TIME_FORMAT)}]'
        else:
            return f'[{self.start_time.strftime(ORG_TIME_FORMAT)}]--[{self.end_time.strftime(ORG_TIME_FORMAT)}] =>  {self.duration}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)

    def __lt__(self, other):
        return 
class Heading:
    def __init__(self, headline: Headline, contents: Tuple[Scheduling, List[Drawer], str]):
        self._headline = headline
        self._scheduling, self._drawers, self.body = contents
        self._children = []
        self._parent = None
        self._sibling = None
        self._inherited_properties = dict()
        if self.body:
            self.timestamps = [TimeStamp(t[0]) for t in re.findall(fr'({Lexer.ATIMESTAMP}|{Lexer.ITIMESTAMP})', self.body)]
        if self._drawers:
            properties_drawer = [d for d in self._drawers if d.name == 'PROPERTIES']
            if properties_drawer:
                self._properties = self._get_properties_dict(properties_drawer[0].contents)
            else:
                self._properties = dict()
        else:
            self._properties = dict()

    def __getattr__(self, attr):
        # So that things like self.todo and self.title, etc... will work
        if self.headline:
            return getattr(self.headline, attr)
        else:
            raise AttributeError(f'Heading class has no attribute {attr}')

    def _parse_clock_line(self, line: str) -> Clocking:
        m = re.search(fr'CLOCK:\s*(?P<start>{Lexer.ITIMESTAMP})(?:--(?P<end>{Lexer.ITIMESTAMP}))?', line)
        if m is not None:
            start_time = re.sub(r'[\[\]]', '', m.group("start"))
            if m.group("end"):
                end_time = re.sub(r'[\[\]]', '', m.group("end"))
            else:
                end_time = None
        else:
            raise ValueError(f"Unable to parse {line} as clocking information")
        return Clocking(start_time, end_time)

    def _get_clocking_info(self) -> List[Clocking]:
        if not self.drawers:
            return []
        logbook = self.get_drawer_by_name('LOGBOOK')
        if logbook:
            return [self._parse_clock_line(l) for l in logbook.contents if re.search(r'^\s*CLOCK:', l)]
        else:
            return []

    def _get_properties_dict(self, contents: List[str]) -> Dict[str, str]:
        return {k: v for (k, v) in [re.search(r':([^:]+):\s+(.*)', line).groups()
                                    for line in contents]} 

    def _get_properties_string(self) -> str:
        return "\n".join([f":{k}:{' '*7}{v}" for k, v in self.properties.items()])

    @property
    def inherited_properties(self):
        if not self._inherited_properties:
            if self.parent:
                self._inherited_properties = {**self.parent.inherited_properties, **self.parent.properties}
        return self._inherited_properties

    @inherited_properties.setter
    def inherited_properties(self, _):
        raise AttributeError("Can't set the inherited properties of a heading")
    
    @property
    def tags(self):
        self_tags = self.headline.tags or []
        parent_tags = (self.parent.tags if self.parent else None) or []
        return list(set(self_tags + parent_tags))

    @tags.setter
    def tags(self, _):
        raise AttributeError("Can't set the tags of a heading, use headline instead.")
    
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, val: Dict[str, str]):
        if type(val) is not dict:
            raise TypeError("Heading properties must be given in the form of a dict")
        else:
            self._properties = dict()
            for key in val:
                self._properties[key] = val[key]

    def get_all_properties(self) -> Dict[str, str]:
        return {**self.inherited_properties, **self.properties}

    def clocking(self, include_children: bool = False) -> List[Clocking]:
        "Return the clocking information of the given headline and possibly its children."
        own_clocking = self._get_clocking_info()
        if include_children and self.children != []:
            return own_clocking + reduce(add, [c.clocking(include_children=True) for c in self.children])
        else:
            return own_clocking

    def get_drawer_by_name(self, name: str) -> Optional[Drawer]:
        "Return the named drawer if it exists, or None if it doesn't"
        try:
            return next(d for d in (self.drawers or []) if d.name == name)
        except StopIteration:
            return None

    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, value: Headline):
        if not isinstance(value, Headline):
            raise TypeError(f"Org headline must be of type {Headline}. Can't work with {type(value)}.")
        else:
            self._headline = value

    @property
    def scheduling(self):
        return self._scheduling

    @scheduling.setter
    def scheduling(self, value: Optional[Scheduling]):
        if value is None:
            self._scheduling = None
        elif not isinstance(value, Scheduling):
            raise TypeError(f"Scheduling information must be of type {Scheduling}. Can't work with {type(value)}.")
        else:
            self._scheduling = value

    @property
    def drawers(self):
        updated_properties_drawer = Drawer(f""":PROPERTIES:
{self._get_properties_string()}
:END:""") 
        if self._drawers:
            if self._drawers[0].name == 'PROPERTIES':
                self._drawers = [updated_properties_drawer] + self._drawers[1:]
        elif self.properties:
            self._drawers = [updated_properties_drawer]
        return self._drawers

    @drawers.setter
    def drawers(self, value: Optional[List[Drawer]]):
        if value is None:
            self._drawers = None
        else:
            types = {type(d) for d in value if type(d) is not Drawer}
            if types:
                raise TypeError(f"Drawer information must be of type {Drawer}. Found these value types instead: {' '.join(types)}.")
            else:
                self._drawers = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if value is None:
            self._children = None
        else:
            types = {type(d) for d in value if type(d) is not Heading}
            if types:
                raise TypeError(f"Child headings must all be of type {Heading}. Found these value types instead: {' '.join(types)}.")
            else:
                self._children = value

    def add_child(self, heading, new: bool = False):
        heading.parent = self
        if not isinstance(heading, Heading):
            raise TypeError(f"Child heading must be of type {Heading}. Can't work with {type(heading)}!")
        if new:
            if self.children:
                self.children.append(heading)
            else:
                self.children = [heading]
        else:
            # This is the case where a heading that's been promoted needs to be adopted by another heading
            if self.children:
                if heading.sibling:
                    try:
                        idx = self.children.index(heading.sibling) 
                        self.children = self.children[:idx + 1] + [heading] + self.children[idx+1:]
                    except ValueError:
                        raise ValueError("Incorrect promotion: grandparent doesn't have original parent in children!")
                else: # This is the case where a heading that's been demoted needs to be adopted by its sibling
                    self.children = [heading] + self.children    
            else:
                self.children = [heading]

    def remove_child(self, child):
        if self.children:
            self.children = [c for c in self.children if c is not child]

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if value is None:
            self._parent = None
        elif not isinstance(value, Heading):
            raise TypeError(f"Parent heading must be of type {Heading}. Can't work with {type(value)}.")
        else:
            self._parent = value

    @property
    def sibling(self):
        return self._sibling

    @sibling.setter
    def sibling(self, value):
        if value is None:
            self._sibling = None
        elif not isinstance(value, Heading):
            raise TypeError(f"Sibling heading must be of type {Heading}. Can't work with {type(value)}.")
        else:
            self._sibling = value

    @property
    def level(self):
        return self.headline.level

    @level.setter
    def level(self, value: int):
        self.headline.level = value

    def promote(self):
        if self.children:
            raise ValueError('Incorrect promotion: heading has children that would be orphaned. Did you mean promote_tree?')
        self.headline.promote()
        self.sibling = self.parent
        idx = self.sibling.children.index(self)
        next_siblings = self.sibling.children[idx + 1:]
        if next_siblings:
            next_siblings[0].sibling = None
            for s in next_siblings:
                s.parent = self
        self.children = next_siblings
        self.sibling.remove_child(self)
        for s in next_siblings:
            self.sibling.remove_child(s)
        self.sibling.parent.add_child(self)
        
    def promote_tree(self):
        children = self.children
        self.promote()
        if children:
            for child in children:
                child.promote_tree()

    def demote(self):
        if not self.sibling:
            raise ValueError('Incorrect demotion: heading has no sibling to adopt it.')
        self.headline.demote()
        idx = self.parent.children.index(self)
        try:
            next_sibling = self.parent.children[idx + 1]
            next_sibling.sibling = self.sibling
        except IndexError:
            pass
        self.parent.remove_child(self)
        self.parent = self.sibling
        if self.parent.children:
            self.sibling = self.parent.children[-1]
        else:
            self.sibling = None
        self.parent.add_child(self)
        if self.children:
            self.children[0].sibling = self
            for child in self.children:
                self.parent.add_child(child)
        self.children = None

    def demote_tree(self):
        children = self.children
        self.demote()
        if children:
            for child in children:
                child.demote_tree()

    def get_path(self):
        "Returns the full path of the current heading as a list of headings"
        if self.parent.title == 'ROOT':
            return [self]
        else:
            return  self.parent.get_path() + [self]

    def __repr__(self):
        scheduling = str(self.scheduling) + "\n" if self.scheduling else ""
        drawers = "".join(d.__str__() for d in self.drawers) if self.drawers else ""
        body = str(self.body) + "\n" if self.body else ""
        if len(body) > 80:
            body = body[:77].strip() + "...\n"
        children = ''.join([c.__str__() for c in self.children]) if self.children else ''
        return f'{self.headline}\n{scheduling}{drawers}{body}{children}'

    def __str__(self):
        scheduling = str(self.scheduling) + "\n" if self.scheduling else ""
        drawers = "".join(d.__str__() for d in self.drawers) if self.drawers else ""
        body = str(self.body) + "\n" if self.body else ""
        children = ''.join([c.__str__() for c in self.children]) if self.children else ''
        return f'{self.headline}\n{scheduling}{drawers}{body}{children}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
