
num = 100; % home to start, and end to home ani steps

for t = 0:.1:7*pi
    Px = 30*t*sin(t);
    Py = 900;
    Pz = 30*t*cos(t);

    [theta1,theta2,theta3,theta4,theta5,theta6] = pumaIK(Px,Py,Pz);
    if t==0 %move to start of demo
        pumaANI(theta1,theta2,theta3,theta4,theta5,theta6,num,'y')
    end
    % Theta 4, 5 & 6 are zero due to plotting at wrist origen.
    pumaANI(theta1,theta2,theta3,0,0,0,n,'y')
end

pumaANI(90,-90,-90,0,0,0,num,'n'); %ホームポジションに戻る　まっすぐな姿勢
