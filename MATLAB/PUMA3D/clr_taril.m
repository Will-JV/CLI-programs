handles = getappdata(0,'patch_h');           %
Tr = handles(9);
%
setappdata(0,'xtrail',0); % used for trail tracking.
setappdata(0,'ytrail',0); % used for trail tracking.
setappdata(0,'ztrail',0); % used for trail tracking.
%
set(Tr,'xdata',0,'ydata',0,'zdata',0);
