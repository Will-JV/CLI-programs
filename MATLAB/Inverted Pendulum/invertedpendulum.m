
%Inverted pendulum model

close all;%グラフを消す
%*************************************
%** 初期値の設定 **
%*************************************
global m M Mu_x Mu_o l J G; %グローバル変数を定義
TIME = 50;            %シミュレーション時間
DELTA = 0.01;         %刻み幅
INIT_POS = pi/180*10; %振り子の初期角度　10
m = 1.0;              %振り子の質量
M = 2.0;              %台車の質量
Mu_x = 0.2;           %台車の粘性抵抗系数 0.2
Mu_o = 0.01;          %回転軸回りの粘性抵抗係数 0.01
l =1.0;               %振り子の長さの半分
J = (m)*l*l/3;        %振り子の重心まわりの慣性モーメント
G = 9.8;              %重力加速度
%***********************************
%*********ゲインの設定**************
%***********************************
Kp  = 300;     %振り子の比例ゲイン
Ki  = 300;     %振り子の積分ゲイン
Kd  = 300;     %振り子の微分ゲイン

Kpx = 3;     %台車の比例ゲイン
Kix = 0;     %台車の積分ゲイン
Kdx = 0;     %台車の微分ゲイン
%***********************************
%***********************************
%*************************************
Posx=linspace(1,TIME/DELTA+1,TIME/DELTA+1); Posx(1)=0; %描画のため　高さの配列の初期化
theta=linspace(1,TIME/DELTA+1,TIME/DELTA+1); theta(1)=INIT_POS; %描画のため　高さの配列の初期化
time=linspace(1,TIME/DELTA+1,TIME/DELTA+1); time(1)=0; %描画のため　高さの配列の初期化
%*************************************

x1=0.0; x2=0.0; y1=INIT_POS; y2=0.0; F=0;
e1=0.0; e2=0.0; sum_e1=0.0; sum_e2=0.0; t=0.0; d1=0.0; d2=0.0; old_e1=0.0; old_e2=0.0;
h=DELTA; tf=TIME/DELTA;

%***********************************
%******計算しているのはここから******
%***********************************  
for i = 1:tf
%********************************************
%***********ルンゲ・クッタ法の式**************
%********************************************
  k1_1 = h*func1(x1, x2, y1, y2);
  k1_2 = h*func2(x1, x2, y1, y2, F);
  k1_3 = h*func3(x1, x2, y1, y2);
  k1_4 = h*func4(x1, x2, y1, y2, F);

  k2_1 = h*func1(x1+k1_1/2, x2+k1_2/2, y1+k1_3/2, y2+k1_4/2);
  k2_2 = h*func2(x1+k1_1/2, x2+k1_2/2, y1+k1_3/2, y2+k1_4/2, F);
  k2_3 = h*func3(x1+k1_1/2, x2+k1_2/2, y1+k1_3/2, y2+k1_4/2);
  k2_4 = h*func4(x1+k1_1/2, x2+k1_2/2, y1+k1_3/2, y2+k1_4/2, F);

  k3_1 = h*func1(x1+k2_1/2, x2+k2_2/2, y1+k2_3/2, y2+k2_4/2);
  k3_2 = h*func2(x1+k2_1/2, x2+k2_2/2, y1+k2_3/2, y2+k2_4/2, F);
  k3_3 = h*func3(x1+k2_1/2, x2+k2_2/2, y1+k2_3/2, y2+k2_4/2);
  k3_4 = h*func4(x1+k2_1/2, x2+k2_2/2, y1+k2_3/2, y2+k2_4/2, F);

  k4_1 = h*func1(x1+k3_1, x2+k3_2, y1+k3_3, y2+k3_4);
  k4_2 = h*func2(x1+k3_1, x2+k3_2, y1+k3_3, y2+k3_4, F);
  k4_3 = h*func3(x1+k3_1, x2+k3_2, y1+k3_3, y2+k3_4);
  k4_4 = h*func4(x1+k3_1, x2+k3_2, y1+k3_3, y2+k3_4, F);

  x1 = x1+(k1_1+2.0*k2_1+2.0*k3_1+k4_1)/6.0;
  x2 = x2+(k1_2+2.0*k2_2+2.0*k3_2+k4_2)/6.0;

  y1 = y1+(k1_3+2.0*k2_3+2.0*k3_3+k4_3)/6.0;
  y2 = y2+(k1_4+2.0*k2_4+2.0*k3_4+k4_4)/6.0;

    
  e1 = (0 - x1); %台車の目標位置と現在位置との差  目標位置　0
  e2 = (0 - y1); %振り子の目標位置と現在位置との差　目標位置　0

  sum_e1 = (sum_e1 + e1)/(1/h);  %台車の偏差の累積値
  sum_e2 = (sum_e2 + e2)/(1/h);  %振り子の偏差の累積値

  d1 = (e1 - old_e1);      %台車の前回の偏差との差
  d2 = (e2 - old_e2);      %振り子の前回のの偏差との差

    %操作量 Ｕの計算
    %台車の操作量の計算
  Up1 = Kpx * e1;           %台車の比例制御の操作量 ゲイン Kp
  Ui1 = Kix * sum_e1;       %台車の積分制御の操作量 ゲイン Ki
  Ud1 = Kdx * d1;           %台車の微分制御の操作量 ゲイン Kd
  U1  = Up1 + Ui1 + Ud1;    %台車の制御量  

  %振り子の操作量の計算
  Up2 = Kp * e2;            %振り子の比例制御の操作量 ゲイン Kp
  Ui2 = Ki * sum_e2;        %振り子の積分制御の操作量 ゲイン Ki
  Ud2 = Kd * d2;            %振り子の微分制御の操作量 ゲイン Kd
  U2  = Up2 + Ui2 + Ud2;    %振り子の制御量  

  F = -(U1 + U2);         %操作量を決定　　台車にあたえる力を計算　
  old_e1 = e1;              %old_e1は一つ前の台車の位置
  old_e2 = e2;              %old_e2は一つ前の振り子の角度
  t = t + h;
  Posx(i+1) = x1;
  theta(i+1) = y1;
  time(i+1) = t;
end
  %********************************************
  %***********ルンゲ・クッタ法の式** ここまで***
  %********************************************

%描画　アニメーションのための準備
clf;%グラフを消す
fig=figure(1);
fig.ToolBar = 'none';
fig.Color = 'white';
radii =30;
axis([-1000 1000 -1000 1900]);%グラフの軸設定　x軸:-1000から1000  y軸:-100から1900
objx=rectangle('Position',[Posx(1)-100 0 200 100],'FaceColor',[0 1 1]);%四角を描画
objr1=rectangle('Position',[Posx(1)-radii*3 -radii radii*2 radii*2],'FaceColor',[1 1 0],'Curvature',[1 1]);% 四角の角を丸くして円を描く
objr2=rectangle('Position',[Posx(1)+radii -radii radii*2 radii*2],'FaceColor',[1 1 0],'Curvature',[1 1]);% 四角の角を丸くして円を描く
line([-2000 2000],[-radii -radii],'LineWidth', 3,'Color','black');%黒い線を描画　
line([0 0],[-100 0],'LineWidth', 3,'Color','black');%黒い線を描画　
text(10,-100,'0','FontSize',14);
text(-1000,1000,'TIME','FontSize',14);
objt=text(-500,1000,num2str(tf),'FontSize',14);
objl=line('XData',[Posx(1) Posx(1)+l*1000*sin(theta(1))],'YData',[100 100+l*1000*cos(theta(1))],'LineWidth', 5);

ax = gca;%軸を再定義
ax.XAxis.Visible = 'off';%X軸のメモリを表示させない
ax.YAxis.Visible = 'off';%Y軸のメモリを表示させない
axis equal;

%実際のアニメーション
for i=1:tf
        objx.Position=[Posx(i)*1000-100 0 200 100];
        objr1.Position=[Posx(i)*1000-radii*3 -radii radii*2 radii*2];
        objr2.Position=[Posx(i)*1000+radii -radii radii*2 radii*2];
        objl.XData=[Posx(i)*1000 Posx(i)*1000+l*1000*sin(theta(i))];
        objl.YData=[100 100+l*1000*cos(theta(i))];
        objt.String=num2str(i/100,5);
        drawnow;
end

%-----------グラフの作成---------------------------%
figure(2);
plot(time,theta);
legend('θ');
title('Inverted Pendulum Controller');
xlabel('t');
ylabel('Angle');
%------------------------------------------------%
%***********************************/
%********* 関数の設定 ***************/
%**********************************/
function r=func1(x1,x2,y1,y2)
  r=x2;
end

function r=func2(x1,x2,y1,y2,F)
    global m M Mu_x Mu_o l J G; %グローバル変数を定義
   r=((J+m*(l^2))*F-Mu_x*(J+m*(l^2))*x2+Mu_o*m*l*cos(y1)*y2+(J+m*(l^2))*m*l*sin(y1)*(y2^2)-(m^2)*(l^2)*G*sin(y1)*cos(y1))/(J*(m+M)+M*m*(l^2)+(m^2)*(l^2)*(sin(y1)^2));
end

function r=func3(x1,x2,y1,y2)
    r=y2;
end

function r=func4(x1,x2,y1,y2,F)
    global m M Mu_x Mu_o l J G; %グローバル変数を定義
       r=(-m*l*cos(y1)*F+Mu_x*m*l*cos(y1)*x2-Mu_o*(m+M)*y2-(m^2)*(l^2)*sin(y1)*cos(y1)*(y2^2)+(m+M)*m*l*G*sin(y1))/(J*(m+M)+M*m*(l^2)+(m^2)*(l^2)*(sin(y1)^2));
end
