%        Inverse Kinematics (T-shaped Manipulator・3 Links)         %

close all
clear
clc

links = zeros(3,1);
a = zeros(3,1);                   % X-Offset
alpha = zeros(3,1);               % X-Torsion angle
alpha(2)=pi/2;
alpha(3)=-pi/2;
d = zeros(3,1);                   % Z-Displacement
d(1) = 400; 
d(3)=100;
theta = zeros(3,1);               % Z-Rotation angle
final_point = diag([1 1 1 1]);
%........................................................................%
%                               手先位置の入力                             %
%........................................................................% 

fprintf("Please specify the arm's end coordinates\n\n" );
x = input('X-coordinates: ');
y = input('Y-coordinates: ');
z = input('Z-coordinates: ');

%........................................................................%
%                               逆運動学の計算                             %
%........................................................................%

r = ((x^2)+(y^2)+(z-400)^2-(100^2))^(1/2); 
th1 = atan2(y,x);
a2 = ((x^2)+(y^2)+(z-400)^2)^(1/2);
th2 = asin(r/a2) - atan2((x^2+y^2)^(1/2),z-400);


%........................................................................%
%                               軸の表示                                  %
%........................................................................% 
a(3)=r; 
theta(1)=th1; 
theta(2)=th2;

axis([-600 600 -600 600 -600 600])                %Spacial Perimeter
hold all
quiver3(0,0,0,0,0,100,'b','LineWidth',1)
quiver3(0,0,0,0,100,0,'b','LineWidth',1)
quiver3(0,0,0,100,0,0,'b','LineWidth',1)
text(0,0,100,'Z','Color','r')
text(0,100,0,'Y','Color','r')
text(100,0,0,'X','Color','r')
view(30,30)
set(gca, 'LineWidth',2, 'XGrid','on', 'GridLineStyle','--')

for i = 1:3
    links(i) = i;
    final_point = final_point * transx(a(i)) * rotx(alpha(i)) * transz(d(i)) * rotz(theta(i));

    hold all
    quiver3(final_point(1,4),final_point(2,4),final_point(3,4),100*final_point(1,1),100*final_point(1,2),100*final_point(1,3),'b','LineWidth',1)
    quiver3(final_point(1,4),final_point(2,4),final_point(3,4),100*final_point(2,1),100*final_point(2,2),100*final_point(2,3),'b','LineWidth',1)
    quiver3(final_point(1,4),final_point(2,4),final_point(3,4),100*final_point(3,1),100*final_point(3,2),100*final_point(3,3),'b','LineWidth',1)
    text(100*final_point(1,1)+final_point(1,4),100*final_point(1,2)+final_point(2,4),100*final_point(1,3)+final_point(3,4),'X'+string(i),'Color','r')
    text(100*final_point(2,1)+final_point(1,4),100*final_point(2,2)+final_point(2,4),100*final_point(2,3)+final_point(3,4),'Y'+string(i),'Color','r')
    text(100*final_point(3,1)+final_point(1,4),100*final_point(3,2)+final_point(2,4),100*final_point(3,3)+final_point(3,4),'Z'+string(i),'Color','r')

    view(30,30)
    set(gca, 'LineWidth',2, 'XGrid','on', 'GridLineStyle','--')
end

%.........................................................................%
%                             データの出力                                  %
%.........................................................................%

fprintf('\n')
fprintf('..................　　結果　　.....................')
fprintf('\n\n')
fprintf('θ1 = %e\n',th1)
fprintf('θ2 = %e\n\n',th2)
disp(table(links,a,alpha,d,theta))
final_point


%.........................................................................%
%                             　　間数 　　　                               %
%.........................................................................%
function tx = transx(a)
    tx = diag([1 1 1 1]);
    tx(1,4) = a;
end

function tz = transz(a)
    tz = diag([1 1 1 1]);
    tz(3,4) = a;
end

function rx = rotx(t)    % rotz=(rotation x), t=(theta)
    ct = cos(t);
    st = sin(t);
    rx = [1 0 0 0;
        0 ct -st 0;
        0 st ct 0
        0 0 0 1];
end

function ry = roty(t)    % rotz=(rotation y), t=(theta)
    ct = cos(t);
    st = sin(t);
    ry = [ct 0 st 0;
        0 1 0 0;
        -st 0 ct 0
        0 0 0 1];
end

function rz = rotz(t)    % rotz=(rotation z), t=(theta)
    ct = cos(t);
    st = sin(t);
    rz = [ct -st 0 0;
        st ct 0 0;
        0 0 1 0
        0 0 0 1];
end

