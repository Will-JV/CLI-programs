%some plotting
axis([0 2 0 2 0 2])
hold all
quiver3(0,0,0,0,0,max(1),'b','LineWidth',1)
quiver3(0,0,0,0,max(1),0,'b','LineWidth',1)
quiver3(0,0,0,max(1),0,0,'b','LineWidth',1)
text(0,0,max(zlim),'Z','Color','r')
text(0,max(ylim),0,'Y','Color','r')
text(max(xlim),0,0,'X','Color','r')
axis equal
view(30,30)
set(gca, 'LineWidth',2, 'XGrid','on', 'GridLineStyle','--')
