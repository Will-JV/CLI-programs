%初期化
Initpuma3d

%分割数
num = 100; 

%座標
Px = [0,0,500,500,0];
Py = [900,900,900,900,900];
Pz = [0,500,500,0,0];

for i = 1:5
    [theta1,theta2,theta3,theta4,theta5,theta6] = pumaIK(Px(i),Py(i),Pz(i));
    if i==1
        pumaANI(theta1,theta2,theta3,0,0,0,num,'n')
    else
        pumaANI(theta1,theta2,theta3,0,0,0,num,'y')
    end
end


